#!/usr/bin/env bash
# Build the web media in assets/media/ from the two project repositories.
#
#   PACKOFF=../packoff-pages WARDZERO=../wardzero PACKOFF_DOCS=../agibot-g2-humanoid-packoff-cell/docs/media \
#     tools/build_media.sh
#
# PACKOFF       checkout of the gh-pages branch of agibot-g2-humanoid-packoff-cell (static/ with the clips)
# PACKOFF_DOCS  docs/media of agibot-g2-humanoid-packoff-cell (storyboard, cell plan)
# WARDZERO      checkout of the wardzero repository (static/ with the clips)
#
# Needs ffmpeg with libx264 and python3 with Pillow.
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
PACKOFF="${PACKOFF:-$ROOT/../packoff-pages}"
PACKOFF_DOCS="${PACKOFF_DOCS:-$ROOT/../agibot-g2-humanoid-packoff-cell/docs/media}"
WARDZERO="${WARDZERO:-$ROOT/../wardzero}"
OUT="$ROOT/assets/media"
mkdir -p "$OUT/packoff" "$OUT/wardzero" "$OUT/home"

X264=(-c:v libx264 -preset slow -pix_fmt yuv420p -movflags +faststart -an)

# Home hero: the G1 walks a WardZero corridor, then the G2 drives into the pack-off cell.
# Segment A is the Isaac Sim panel of the WardZero backend clip, without the telemetry around it.
ffmpeg -v error -y \
  -ss 3 -t 10 -i "$WARDZERO/static/videos/04_isaac_backend.mp4" \
  -ss 1 -t 8 -i "$PACKOFF/static/videos/01_packing_overview.mp4" \
  -filter_complex "\
[0:v]crop=1312:738:44:38,scale=1280:720,fps=30,setsar=1,format=yuv420p[a];\
[1:v]scale=1280:720,fps=30,setsar=1,format=yuv420p[b];\
[a][b]xfade=transition=fade:duration=1:offset=9,fade=t=in:st=0:d=0.6,fade=t=out:st=16.4:d=0.6[v]" \
  -map "[v]" "${X264[@]}" -crf 27 "$OUT/home/hero.mp4"
# VP9 copy for browsers without H.264 (some Linux builds of Chromium)
ffmpeg -v error -y -i "$OUT/home/hero.mp4" -c:v libvpx-vp9 -b:v 0 -crf 40 -row-mt 1 -deadline good -cpu-used 2 -an "$OUT/home/hero.webm"
ffmpeg -v error -y -ss 6 -i "$OUT/home/hero.mp4" -frames:v 1 -q:v 3 "$OUT/home/hero.jpg"
# A clean still of the G1 in the corridor, without the telemetry panels, for cards
ffmpeg -v error -y -ss 19 -i "$WARDZERO/static/videos/04_isaac_backend.mp4" -frames:v 1 \
  -vf "crop=1312:738:44:38,scale=1280:720" -q:v 3 "$OUT/wardzero/g1_corridor.jpg"

# Pack-off cell clips are already web encoded on the project page.
for clip in 01_packing_overview 02_packing_head 03_teleop_replay 04_slam_nav; do
  cp "$PACKOFF/static/videos/$clip.mp4" "$OUT/packoff/$clip.mp4"
  cp "$PACKOFF/static/videos/$clip.jpg" "$OUT/packoff/$clip.jpg"
done

# WardZero clips are 1080p on the project page. Re-encode them at 720p for this site.
for clip in 01_hospital_environment 03_mujoco_world 04_isaac_backend 05_gait_training 06_mode_manager_teleop 07_slam_navigation; do
  ffmpeg -v error -y -i "$WARDZERO/static/videos/$clip.mp4" -vf scale=1280:-2 "${X264[@]}" -crf 27 "$OUT/wardzero/$clip.mp4"
done

python3 - "$PACKOFF" "$PACKOFF_DOCS" "$WARDZERO" "$OUT" <<'PY'
import shutil, sys
from pathlib import Path
from PIL import Image

packoff, docs, ward, out = map(Path, sys.argv[1:])

def jpg(src, dst, width=1600, quality=82):
    im = Image.open(src).convert("RGB")
    if im.width > width:
        im = im.resize((width, round(im.height * width / im.width)), Image.LANCZOS)
    im.save(dst, quality=quality, optimize=True, progressive=True)

# Pack-off cell stills
jpg(packoff / "static/images/cell_table.png", out / "packoff/cell_table.jpg")
jpg(packoff / "static/images/pilot_events.png", out / "packoff/pilot_events.jpg")
shutil.copy(packoff / "static/images/pilot_loss.png", out / "packoff/pilot_loss.png")
shutil.copy(docs / "packing_storyboard.jpg", out / "packoff/packing_storyboard.jpg")
shutil.copy(docs / "cell_plan.svg", out / "packoff/cell_plan.svg")

# WardZero stills and posters
for name in ["01_hospital_environment", "02_robot_model", "03_mujoco_world", "04_isaac_backend",
             "05_gait_training", "06_mode_manager_teleop", "07_slam_navigation"]:
    jpg(ward / f"static/videos/{name}.jpg", out / f"wardzero/{name}.jpg", width=1280)
for name in ["Cam_WardB1EnSuite", "Cam_Resus", "Fx_MainLiftBank", "Fx_StairDoor", "Cam_WardCorridor",
             "Cam_AEEntrance", "Cam_HospitalToWing", "Fx_WardEntranceDoors"]:
    jpg(ward / f"static/images/v2/{name}.jpg", out / f"wardzero/{name}.jpg", width=1280)
jpg(ward / "static/images/wing_plan.png", out / "wardzero/wing_plan.jpg", width=1280)

# Social preview image (1200 x 630) from the hero poster
im = Image.open(out / "home/hero.jpg").convert("RGB")
w, h = im.size
crop_h = round(w * 630 / 1200)
top = (h - crop_h) // 2
im.crop((0, top, w, top + crop_h)).resize((1200, 630), Image.LANCZOS).save(out / "home/og.jpg", quality=82)
PY

du -sh "$OUT"/*
