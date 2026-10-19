# Kyne Robotics

The website of Kyne Robotics: [kynerobotics.com](https://kynerobotics.com)

Kyne Robotics builds software that automates localised humanoid deployment. It adapts off-the-shelf humanoids,
such as the Unitree G1 and the AgiBot G2, to a specific site and trains them for the job, starting with a
simulation of the client's facility. Our engineers install and support the robots on site.

## Pages

| Page | File |
|---|---|
| Home | `index.html` |
| Services | `services.html` |
| Humanoid programmes | `programmes.html` |
| Technology | `technology.html` |
| Work | `work.html` |
| Case study: AgiBot G2 pack-off cell | `work-packoff-cell.html` |
| Case study: WardZero | `work-wardzero.html` |
| Company | `company.html` |
| Contact | `contact.html` |

## Run it locally

The site is plain HTML, CSS and JavaScript, with no build step.

```bash
python3 -m http.server 8000
```

Then open http://localhost:8000.

## How the repository is organised

| Path | Contents |
|---|---|
| `*.html` | One file per page |
| `partials/` | The shared header and footer |
| `assets/css/site.css` | All styles |
| `assets/js/site.js` | Navigation, video playback and the contact form |
| `assets/media/` | Images and video clips from our projects |
| `tools/` | Small scripts for maintaining the site |

The header and footer are kept in `partials/` and copied into every page with
`python3 tools/sync_partials.py`. `tools/build_media.sh` rebuilds the web versions of the project media, and
`tools/export_copy.py` collects the text of every page into `docs/COPY.md`.

## Credits

The images and clips are simulation renders from two of our projects:
[AgiBot G2 pack-off cell](https://github.com/Bkrakshith/agibot-g2-humanoid-packoff-cell) and
[WardZero](https://github.com/Bkrakshith/wardzero). They show third-party assets, which keep their own licences:

- AgiBot G2 robot model and GenieSimAssets: CC BY-NC-SA 4.0
- AgiBot Genie Sim: MPL 2.0
- Lightwheel SimReady assets: CC BY-NC 4.0
- NVIDIA Isaac for Healthcare assets: Apache 2.0
- NVIDIA Isaac Sim hospital building: NVIDIA Limited Use Content

Typefaces: Geist and Geist Mono, under the SIL Open Font License.

## Contact

hello@kynerobotics.com

Copyright © 2026 Kyne Robotics. All rights reserved.
