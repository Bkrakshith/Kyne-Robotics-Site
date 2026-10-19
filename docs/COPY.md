# Kyne Robotics website copy

Generated from the HTML pages by `tools/export_copy.py`. Edit the pages, then run the script again.
Shared navigation and footer text is listed once at the end.

---

## Page: Home (`index.html`)

Browser title: Kyne Robotics: humanoid deployment automation  
Meta description: Kyne Robotics builds software that automates localised humanoid deployment. It adapts Unitree, AgiBot and other off-the-shelf humanoids to your site and trains them for the job, and our engineers install them with you.

*HUMANOID DEPLOYMENT AUTOMATION*

### Off-the-shelf humanoids, trained for your floor

Unitree, AgiBot and other accessible humanoids are being bought, but out of the box they do very little. Kyne is software that adapts each robot to your site and trains it for the job, and our engineers install it with you.

[Start a programme]

[See our work]

Simulation: Unitree G1 in WardZero, AgiBot G2 in the pack-off cell

Pause video

*PLATFORMS AND TOOLS WE BUILD ON*

AgiBot G2 Unitree G1 NVIDIA Isaac Sim MuJoCo ROS 2 MoveIt 2 Nav2 Genie Sim PyTorch Foxglove

#### We make the humanoids you can buy today do useful work in your building

Kyne builds localised humanoid deployment automation: software that takes a robot from a simulated copy of your site to a tested skill on your floor, with our engineers on site for the last step.

*SELECTED WORK*

*MANUFACTURING*

##### AgiBot G2 pack-off cell: a wheeled humanoid packing sealed bags into cartons at the end of a line

[Read case study]

*HEALTHCARE*

##### WardZero: a simulated UK hospital, with fire doors and bed lifts, where a Unitree G1 trains before it meets patients

[Read case study]

*YOUR SITE*

##### Your facility: we build a simulated version of it and test the robot there before you buy one

[Start a programme]

#### From a simulated copy of your site to a robot on your floor

*OUR APPROACH*

Kyne pipeline

- 01 Site twin

- 02 Demonstrate

- 03 Train

- 04 Validate

- 05 Deploy

Every deployment starts in simulation. Our software builds a model of your site, generates the training data, trains the robot’s skills and tests them against the checks we will use on site. Only then does the robot come through your door.

Our software talks to the robot through the manufacturer's own interface from day one, so the code we test in simulation is the code we install.

[How we work]

*MEASURED IN OUR PROJECTS*

#### We measure what we build and we say where each number came from.

These figures come from our two showcase projects. Both run in simulation today, and each case study explains how the number was measured and what has not been tested yet.

*PILOT DATASET*

**20/20**

generated episodes ended with the bag in the carton. AgiBot G2 pack-off cell

*DRIVE-IN ACCURACY*

**0.57 cm**

final position error after a 2.0 m drive into the cell. AgiBot G2 pack-off cell

*MAP ACCURACY*

**99.6 %**

of mapped wall cells within 0.10 m of the true walls. WardZero

*PARALLEL TRAINING*

**2,048**

simulated robots learning at once on a single RTX 3070. WardZero

[Read the case studies]

#### We pick the robot that fits the task, and we will tell you when the right answer is a conveyor.

*WAYS TO WORK WITH US*

Programmes 01

A simulation study for a new humanoid programme

Services 02

Policy training with imitation and reinforcement learning

Services 03

Application software on the manufacturer's own interface

Services 04

On-site integration and commissioning, in person

#### Thinking about humanoids for your site? Start with a simulation of it.

Tell us about the building and the job. We will tell you which robot could do it, what the hard parts are and how to find out for sure.

[Talk to us]

[How a programme starts]

---

## Page: Services (`services.html`)

Browser title: Services: Kyne Robotics  
Meta description: Deployment software, policy training and on-site integration for off-the-shelf humanoids. Kyne Robotics takes a robot from its crate to a job on your floor.

*SERVICES*

### Everything between the crate and the job

Manufacturers ship capable hardware with a basic controller and an SDK. Getting that robot to pack a carton or cross a hospital ward is separate work. Our deployment software automates most of it, and our engineers do the rest in person.

#### Deployment software, with engineers alongside

The software automates the site model, the training data, the training and the tests for each site. Our team scopes the work, integrates the robot and supports it after go-live. If you already own a robot, we start wherever it is stuck.

> Waist first, then the arm. The G2 packing sequence from its own head camera, AgiBot G2 pack-off cell.

*01 APPLICATION SOFTWARE*

#### Task software that runs on the real robot

We write the logic for the job: where to pick, where to place, what to do with a reject and how to recover from a failed grasp. Every arm move goes through one motion server, which checks the full path against the robot's own body and the fixtures before a joint moves. Navigation runs on mapped zones with speed limits.

We build on the manufacturer's interface, such as the AgiBot GDK on the G2 and the low-level command interface on the Unitree G1. Code tested in simulation runs on the robot without a rewrite.

- Task state machines with tested failure paths

- Motion planning with collision and clearance checks

- Mapping, localisation and navigation

- A safety layer with a control lease, a watchdog, an emergency stop and speed zones

> Before and after training. Left: the policy before training falls after 1.0 s. Right: after 39 million steps it stands for the full 11 s test. WardZero, MuJoCo.

*02 POLICY TRAINING*

#### Policies trained on your task, with gates before they ship

Some skills are easier to learn than to program. We collect demonstrations by teleoperation or with a scripted generator, record synchronised camera, joint and command data, and train imitation policies such as ACT and behaviour cloning.

For locomotion and whole-body control we train with reinforcement learning in MuJoCo MJX, thousands of robots in parallel, then distil a teacher policy into a student that only uses the sensors the real robot has. Each stage has pass gates, and a policy reaches the robot only after it passes in simulation the tests it must pass on site.

- Teleoperation by keyboard, SpaceMouse or webcam

- Episode recording to HDF5 and LeRobot-style datasets

- Imitation learning: ACT and behaviour cloning

- Reinforcement learning with PPO, curricula and teacher-student distillation

> The details that decide a deployment. Ward entrance fire doors in WardZero. On site, we survey every door, lift and threshold the robot has to pass.

*03 ON-SITE INTEGRATION*

#### In person, on your site

A robot is finished when it works in your building with your people. We come to site to survey and map the space, set out the cell and the fixtures, and set speed zones and safety limits with your health and safety team.

We commission the robot against acceptance tests agreed with you before the work starts, train your operators and hand over with the test results. When your products or your layout change, we retrain and recommission.

- Site survey, mapping and cell layout

- Commissioning against agreed acceptance tests

- Operator training and handover

- Retraining for new products and layout changes

> A building as the robot sees it. The fast-physics version of the WardZero hospital, made from the same layout file as the photoreal scene.

*04 SIMULATION STUDIES*

#### Simulation studies for new humanoid programmes

If you are deciding whether humanoids fit your operation, we build a simulated version of your site, put candidate robots in it and run your tasks. You get reach, layout and cycle-time evidence and an architecture for the deployment before you buy hardware.

[How a programme starts]

*PLATFORMS*

#### We work with robots you can buy

We are not tied to a manufacturer. We choose the platform for the task and the building, and our software and training pipeline move with us from one robot to the next.

*WHEELED HUMANOIDS*

##### Dual arms on a stable base

Two arms, a waist and a wheeled base. Strong at stations, cells and flat floors, where the robot replaces a person standing at a table. Our reference platform is the AgiBot G2.

*BIPEDAL HUMANOIDS*

##### Legs and hands for buildings made for people

Legs for thresholds, ramps and tight rooms, with dexterous hands for doors and handling. Our reference platform is the Unitree G1 with BrainCo Revo2 hands.

*QUADRUPEDS*

##### Four legs for rounds and rough ground

Legged platforms for inspection rounds, carrying and uneven floors. The same simulation, training and safety pipeline applies, with the platform chosen to suit the route.

*HOW A PROJECT RUNS*

#### Five stages, each with something you can check

Every stage ends with evidence: a report, a recorded run or a passed test. You decide at each one whether to carry on.

01

**Scope**

We visit, walk the process with your team and agree the task and the acceptance tests.

02

**Simulate**

We model the site and the robot, then test reach, clearances and cycle time.

03

**Train**

We collect demonstrations, train the policies and gate them against the tests.

04

**Integrate**

We install on site, commission against the acceptance tests and train your operators.

05

**Support**

We watch the numbers, retrain when things change and extend to the next task.

#### Have a robot that is not doing its job yet?

Tell us what it is, where it works and what it should be doing. We will tell you what it needs.

[Talk to us]

[See our work]

---

## Page: Programmes (`programmes.html`)

Browser title: Start a humanoid programme: Kyne Robotics  
Meta description: Before you buy a humanoid, find out what it can do in your building. Kyne Robotics builds a simulated version of your site, tests candidate robots on your tasks and architects the deployment.

*HUMANOID PROGRAMMES*

### Start your humanoid programme in simulation

Before you buy a robot, find out what it can do in your building. We build a simulated version of your site, put candidate robots in it and run your tasks. You get evidence and an architecture before you sign a purchase order.

[Book a discovery call]

[What you get]

#### The problems that stop a robot deployment are physical and specific

An arm that cannot reach the far side of the table, or a fire door the robot cannot push. Simulation finds these while they are still cheap to fix.

*01*

##### Choose the right robot

Compare wheeled, bipedal and legged platforms on your tasks instead of their spec sheets.

*02*

##### Size the cell

Find reach limits, clearances and cycle times before anyone moves a conveyor or orders a fixture.

*03*

##### Find the hard parts early

Doors, lifts, shiny floors and people in corridors go into the model, and we test the robot against them.

*04*

##### Start training before delivery

Task software, demonstration data and policies from the study carry into the pilot, so the robot does not start from zero.

> A cell plan that came out of simulation. The U cell for the AgiBot G2, with every placement checked against the robot's reach.

*WHAT WE BUILD*

#### A working model of your site

We build the model from your drawings, photos and a day on site. One layout file generates the photoreal scene in NVIDIA Isaac Sim, the fast-physics world in MuJoCo and the maps, so all of them agree. A build check stops the model if furniture blocks a door or two objects overlap.

Then we add your products, your fixtures and the candidate robots, each running the same software it would run on site.

> A whole building, not only a cell. The WardZero hospital and surgical wing in Isaac Sim, path traced.

*WHAT WE TEST*

#### Your tasks, with every run recorded

We run reach studies, cycle-time runs and navigation through your doors and lifts. We inject failures, such as a dropped item, a blocked corridor or a lost signal, and check that the robot recovers or stops safely.

Every run is recorded, so each number in the report links back to the run that produced it.

*HOW A STUDY RUNS*

#### Five phases from first visit to pilot plan

The scope and timing depend on the site and the tasks. We agree both after the discovery phase, before the modelling starts.

01

**Discovery**

We visit, walk the process with your team and agree the tasks, the success measures and the constraints on safety, space and shifts.

02

**Site model**

We model the building, the fixtures, your products and the candidate robots.

03

**Trials**

Reach studies, cycle-time runs, navigation, failure cases and recovery, all recorded.

04

**Architecture**

Robot choice, cell layout, safety zones, links to your line control and warehouse systems, and the people around the robot.

05

**Pilot plan**

A plan for the first robot on your floor, with acceptance tests taken from the simulation.

*WHAT YOU GET*

#### Evidence you can take to a budget meeting

A study ends with a clear recommendation: which robot, in which layout, doing which tasks, with the numbers behind it. Sometimes the recommendation is a different kind of automation, and we say so.

- The simulated site, with your tasks set up in it

- Reach, clearance and cycle-time results for each candidate robot

- A robot shortlist with the reasons for each choice

- Cell layout drawings

- An integration and safety architecture

- Risks that simulation cannot settle, with a plan to test each one on hardware

- A pilot plan with acceptance tests

- Video of the robot doing your task in simulation, for your stakeholders

*WHAT SIMULATION CAN AND CANNOT TELL YOU*

Simulation answers reach, layout, cycle-time and navigation questions well. It is weaker on contact-rich handling of soft goods, such as bags of salad, and on how people behave around a robot in a busy space.

We flag those risks in the report and plan hardware tests for them early, so they do not surprise you in the pilot.

*WHERE WE HAVE DONE THIS*

*MANUFACTURING AND PACKING*

##### An end-of-line pack-off cell for a wheeled humanoid, with the full line around it

[Read case study]

*HEALTHCARE*

##### A hospital built to UK guidance, with fire doors and bed lifts that work in both simulators

[Read case study]

*QUESTIONS*

#### Before you start

**Q:** Do we need to have chosen a robot?

No. Choosing the robot is part of the study. We work with off-the-shelf humanoids from several manufacturers, including Unitree and AgiBot, and compare them on your tasks.

**Q:** What do you need from us?

Floor plans or drawings, photos of the area, samples or specifications of the products the robot will handle, a description of the process and a day on site with the people who run it.

**Q:** Can the study lead straight into a deployment?

Yes. Our deployment software carries the site model, the task software and the training data straight into the pilot, all built on the robot’s real interface from the start.

**Q:** What if the answer is that a humanoid is the wrong choice?

Then the report says so, and says what would work better. A clear no early on is a good outcome for a study.

**Q:** How do you handle our drawings and site data?

We treat them as confidential and agree terms with you before the study starts.

#### Start with a discovery call

A short call about your site, your tasks and what you want a robot to change. We will tell you whether a simulation study makes sense.

[Book a discovery call]

[Our technology]

---

## Page: Technology (`technology.html`)

Browser title: Technology: Kyne Robotics  
Meta description: One software stack from simulation to the real robot: the manufacturer's interface everywhere, one safety layer, one model of the site, and a training pipeline from demonstrations to gated policies.

*TECHNOLOGY*

### One stack from simulation to the real robot

Our deployment software runs the same automated pipeline for every site. The robot interface, the safety layer and the model of the site are shared between simulation and hardware, so a result in simulation means something on site.

*ARCHITECTURE*

#### Built so nothing is rewritten for deployment

The gap between simulation and a real robot is mostly software that changes on the way. We design the stack so the code you test is the code you install.

*01*

##### One robot interface

Our software talks to the robot through the manufacturer's interface in every environment. On the Unitree G1 the controller sends motor targets at 500 Hz and reads joint states, in MuJoCo, in Isaac Sim and on the robot. On the AgiBot G2, a simulated GDK lets GDK code run on the simulated cell unchanged.

*02*

##### One safety layer

Every input, from a teleoperator to a trained policy, asks a mode manager for control. A control lease, a watchdog, an emergency stop gate and speed zones decide what moves, and only one process ever sends joint commands.

*03*

##### One model of the site

One layout file generates the photoreal scene, the physics world, the colliders for the motion planner and the maps. A map made in one simulator is correct in the other, and a change to the site is made once.

*DEPLOYMENT AUTOMATION*

#### From demonstrations to a policy that has earned its place

01 Site model

**Model the site and the robot**

Generated from one layout file, with build checks for blocked doors and overlapping objects. The robot model comes from one source file for every simulator.

02 Demonstrate

**Show the robot the task**

Teleoperation from a keyboard over SSH, a SpaceMouse or a webcam with hand tracking, with no VR headset needed. Scripted generators randomise product positions and labels for volume.

03 Record

**Keep every frame in sync**

Head camera, depth, joint states and commands go to MCAP, then HDF5 and LeRobot-style datasets. The compressed profile records at about 1.1 MB/s, against 78 MB/s raw.

04 Train

**Learn the skill**

Imitation learning such as ACT and behaviour cloning for manipulation. PPO in MuJoCo MJX for locomotion and whole-body control, with 2,048 robots in parallel on one GPU and a teacher-student curriculum.

05 Validate

**Pass the gates**

Each training stage has pass gates, and validation uses whole held-out episodes. The trainer keeps the checkpoint that passes, not the last one.

06 Deploy

**Move to the robot**

Policies export to ONNX and run inside the same controller on every backend. The ROS 2 stack, with slam_toolbox, AMCL and Nav2, moves to the robot unchanged.

> A recorded demonstration, replayed from its data file. Commanded and measured arm joints agree within 0.0012 rad. AgiBot G2 pack-off cell.

*DATA*

#### Demonstrations you can audit

Every episode is a file you can open, replay and check. We redraw the robot from the recorded joints next to the camera frames, so a bad demonstration is caught before it reaches training.

The validation split uses complete episodes, so no frame of a validation episode leaks into the training data.

> The mode manager at work. In HOLD the robot ignores velocity keys, and it moves again only after an explicit resume. WardZero, ROS 2 on MuJoCo at 500 Hz.

*SAFETY*

#### Seven modes, one decision maker

The robot runs in one of seven modes, from DAMP, with the motors off, to HOLD, which stops it in place. A watchdog sets HOLD if the interface signal stops, and a hardware emergency stop has priority over every input.

Speed zones on the map set the maximum speed in each area, so the robot slows near doors and in busy corridors.

> Mapping while navigating. About 5.7 hours of simulated walking through the hospital and surgical wing, shown in 27 seconds. WardZero.

*AUTONOMY*

#### Standard navigation, measured against ground truth

We use standard ROS 2 packages where they are good enough, and they usually are: slam_toolbox for mapping, AMCL for localisation and Nav2 for planning. Because the simulated building is exact, we can measure the map: in WardZero, 99.6% of mapped wall cells sit within 0.10 m of the true walls.

*TOOLCHAIN*

#### What we build with

Open, widely used tools wherever we can, so your team can maintain what we leave behind. Everything runs headless in Docker, on a workstation or on cloud GPUs.

*SIMULATION*

- NVIDIA Isaac Sim

- AgiBot Genie Sim

- MuJoCo and MJX

*ROBOTICS*

- ROS 2 Jazzy

- MoveIt 2

- Nav2 and slam_toolbox

*LEARNING*

- PyTorch

- PPO on MuJoCo MJX

- ONNX for deployment

*DATA AND TOOLS*

- MCAP, HDF5, LeRobot format

- Foxglove

- Docker

#### See the pipeline on a real project

Both case studies show each stage, with the numbers and the limits.

[See our work]

[Talk to us]

---

## Page: Work (`work.html`)

Browser title: Work: Kyne Robotics  
Meta description: Two Kyne Robotics projects: an AgiBot G2 pack-off cell for an end-of-line packing station, and WardZero, a simulated UK hospital where a Unitree G1 trains.

*WORK*

### Two robots, two buildings, one pipeline

We built these projects to show how we work: a packing line in a factory and a hospital, with a wheeled humanoid in one and a bipedal humanoid in the other. Both are at the simulation stage, and each case study says exactly what has and has not been tested.

*MANUFACTURING*

*AGIBOT G2*

*GENIE SIM*

#### AgiBot G2 pack-off cell

A wheeled humanoid at the end of a packing line. It picks sealed bags from a table, packs them into cartons on a conveyor and sorts rejects into totes, inside a full end of line with a case erector, a case sealer and a palletiser.

20/20 pilot episodes with the bag in the carton 0.57 cm final error after a 2.0 m drive-in

[Read case study]

*HEALTHCARE*

*UNITREE G1*

*ISAAC SIM AND MUJOCO*

#### WardZero

A simulated hospital where robots train before they meet patients. It has a surgical wing, a ward and a small A&E built to UK hospital guidance, fire doors and bed lifts with physics, and a Unitree G1 that runs the same software in two simulators.

99.6% of mapped walls within 0.10 m 2,048 robots training in parallel on one GPU

[Read case study]

*WHAT THE TWO HAVE IN COMMON*

#### The same habits on every project

Different robots and different buildings, built the same way. These habits are what we bring to your site.

*01*

##### The real robot interface

The AgiBot GDK in the pack-off cell, the Unitree low-level interface in WardZero. No simulation-only shortcuts in the code that moves the robot.

*02*

##### Generated, checked environments

Each site comes from one generator file. Tests check reach, clearances and overlaps every time the site is rebuilt.

*03*

##### Honest numbers

Every figure has a method behind it, and every page has a status section that lists what is still untested.

*NEXT*

#### Your site could be the third project

We build a simulated version of your facility and test the robot in it before you commit to hardware.

[Start a programme]

#### Want to see a project in more detail?

We are happy to walk you through either one, including the parts that are not finished.

[Talk to us]

---

## Page: Case study: AgiBot G2 pack-off cell (`work-packoff-cell.html`)

Browser title: AgiBot G2 pack-off cell: Kyne Robotics  
Meta description: Case study: an AgiBot G2 wheeled humanoid packs sealed bags into cartons at the end of a packing line, in a full simulated end-of-line cell with teleoperation, data generation and training.

*CASE STUDY: MANUFACTURING*

### A humanoid at the end of a packing line

An AgiBot G2 picks sealed bags of salad and crisps from a table and packs them into cartons on a conveyor. Rejects go into totes in a sort rack.

Pause video

**Robot:**

AgiBot G2: wheeled base, waist, two 7-DoF arms, head RGB-D camera

**Task:**

Pack-off of flexible, sealed bags into cartons

**Simulator:**

AgiBot Genie Sim 3.2 on NVIDIA Isaac Sim 6.0.1

**Stage:**

Simulation. No test on a real G2 yet

*THE JOB*

#### A station the size of a person

Pack-off is still a manual job in many fresh-produce and snack factories. A person stands at the end of the line, takes pillow packs off a table, packs them into cartons and puts rejects aside.

The bags are soft, the products change and the station is built around a person. A wheeled humanoid with two arms fits into the same footprint, which makes pack-off a natural first job for one.

> Cell plan. The G2 drives into the U. Cartons flow from the case erector to the palletiser.

*THE CELL*

#### A complete end of line, built from one generator

We built a U-shaped cell the robot drives into: the pick table on its left, the conveyor in front and the sort rack on its right. Downstream, the line has a case erector, a drop gap with a floor bin, a right-angle transfer, a case sealer and a cobot palletiser, so the robot works inside a real line and not a bare table.

One Python generator makes the scene and the list of colliders. The motion planner and the tests use the same list, so a moved fixture is a one-line change that every check sees.

*MOTION*

#### Every move is checked before it runs

The G2 turns its waist first, then moves the arm: +55° to the table, 0° to the carton, −95° to the rack. Each arm path is checked against the head camera and the fixtures over its full length, and the wheeled base holds its position on odometry while the arms move.

> The packing sequence from the G2's head camera. Drive in, table, carton, sort rack.

> What the robot sees, 640 × 400. The data recorder and the training use this view.

*DRIVE-IN*

**0.57 cm**

final position error after 2.0 m in 10.3 s, with 0.00° heading error.

*HEAD CLEARANCE*

**0.20 m**

minimum distance from every arm path to the head camera. Paths that come closer are rejected.

*BASE HOLD*

**0.43 cm**

base drift while the arms move. Without the hold, a reach can push the base by up to 23 cm.

*DATA AND TRAINING*

#### From teleoperation to a training run

Operators drive the arms from a keyboard over SSH or with a SpaceMouse. A scripted generator randomises bag positions, orientation and labels inside the reachable zone, then records each episode and scores where the bag ended up.

Our pilot dataset has 20 episodes, and all 20 ended with the bag in the carton. Physics held 99.7 Hz and the head camera 30 Hz during generation, and the recorder wrote about 1.1 MB/s against 78 MB/s for the raw streams.

A first ACT-style training run on this data took the validation loss from 0.45 to 0.075 in 300 steps on a CPU. That run proves the pipeline works end to end. It is not an evaluation of a policy, and full training runs on cloud GPUs.

> One pilot episode: start, grasp, lift, transfer, place and end.

> A teleoperation episode, redrawn from its HDF5 file. Commanded and measured joints agree within 0.0012 rad. Recorded in the first, simpler scene.

> Training loss on the pilot dataset. 16 training episodes, 4 held-out validation episodes, CPU, 300 steps.

> Mapping and navigation on the first cell layout, from the two chassis lidars.

*MOBILITY*

#### A robot that can leave the cell

With two chassis lidars, the G2 maps the room with slam_toolbox and navigates with AMCL and Nav2. Both Nav2 goals in the test succeeded, with final errors of 0.10 m and 0.084 m. That run used the first cell layout, so the map has to be made again for the U cell.

The cell also includes an interface layer with the AgiBot GDK names, so code written for the real G2 runs on the simulated cell without changes.

*STATUS*

Simulation stage. All results on this page come from simulation. No test on a real G2 is complete.

The bags are rigid placeholders, so the grasp uses an attach and release. Deformable bags and a real gripper grasp are the next steps, followed by full policy training on cloud GPUs.

Code: agibot-g2-humanoid-packoff-cell , Apache-2.0, for non-commercial use. The renders use the AgiBot G2 model and GenieSimAssets (CC BY-NC-SA 4.0), AgiBot Genie Sim (MPL 2.0) and NVIDIA Isaac Sim.

*NEXT CASE STUDY*

#### WardZero: the hospital where robots train before they meet patients

[Read case study]

#### Running a manual packing station?

We can model your line and show what a humanoid can and cannot do at it, before you buy one.

[Talk to us]

[How a programme starts]

---

## Page: Case study: WardZero (`work-wardzero.html`)

Browser title: WardZero: Kyne Robotics  
Meta description: Case study: WardZero, a simulated UK hospital with a surgical wing, a ward, an A&E, fire doors and bed lifts, where a Unitree G1 humanoid trains in Isaac Sim and MuJoCo.

*CASE STUDY: HEALTHCARE*

### WardZero, the hospital where robots train before they meet patients

A simulated hospital with a surgical wing, a ward and a small A&E, built to UK hospital guidance. The reference robot is a Unitree G1 humanoid with BrainCo hands.

Pause video

**Robot:**

Unitree G1, 29 DoF, two BrainCo Revo2 hands

**Setting:**

Hospital with a surgical wing, a six-bed ward and an A&E

**Simulators:**

NVIDIA Isaac Sim and MuJoCo, on one robot interface

**Stage:**

Simulation. Open source, Apache-2.0

*THE PROBLEM*

#### Hospitals are hard places for robots

Hospitals are full of things robots find difficult: self-closing fire doors, bed lifts, long reflective corridors, trolleys parked against the walls and people everywhere. You cannot test a robot on a live ward until it has proved itself somewhere else.

WardZero is that somewhere else. Feedback on the first version said lifts and fire doors mattered most, so version 2 adds them, with physics, in both simulators.

*BUILT TO GUIDANCE*

#### Closer to a real UK hospital

Version 2 follows NHS England and UK Government guidance for hospital buildings. Each door and lift runs the same control code in Isaac Sim and MuJoCo, and a fire-alarm signal closes every fire door in about 6 seconds while the lidar watches them move.

Area

Guidance

What WardZero has

Fire doors

HTM 05-02

Up to 22 fire doorsets with physics. The leaves close themselves, and magnets hold the corridor doors open until the fire alarm releases them.

Lifts

HTM 08-02

Two pairs of bed lifts, car 1800 × 2700 mm, with call buttons, door timing, light curtains and fire recall.

Ward

HBN 04-01

A six-bed ward with en-suite bedrooms, a nurse base and workstations with observation windows.

A&E

HBN 15-01

An ambulance entrance, resus with two bays, majors cubicles, triage, minors, X-ray and walk-in reception.

Circulation

HBN 00-04

A 4 m link corridor to the surgical wing, so two beds can pass.

Access

Approved Document M

Door opening forces under 30 N. Lift buttons between 0.9 m and 1.2 m above the floor.

> Ward bedroom with en-suite

> A&E resus, two bays

> Bed lifts, main building

> Stair fire door

> Ward corridor from the nurse base

> A&E ambulance entrance

> 4 m link corridor

> Ward entrance fire doors

WardZero follows the guidance for robot testing. It is not a certified building design, and no fire engineer has reviewed it. Known gaps, such as ward bedroom doors narrower than the guidance recommends for beds, are listed in the project repository.

> Isaac Sim backend. Third-person view, head camera, lidar from above and the 12 leg joints. The walking policy here is a placeholder.

*ONE INTERFACE, TWO SIMULATORS*

#### The same software in MuJoCo, Isaac Sim and on the robot

The controller sends motor targets at 500 Hz and reads joint states, exactly as on the real G1. MuJoCo gives fast physics for training. Isaac Sim gives realistic rendering, a lidar and a head camera for testing navigation and perception.

Everything above the controller is identical in both, and one layout file builds the hospital for each simulator in the same world frame.

> MuJoCo hospital world. The fast-physics version of the same building, made from the same layout file.

*ROBOT AGNOSTIC*

#### Bring a different robot

The hospital, the safety layer and the navigation stack contain no robot-specific code. A different robot brings its own model, simulator bindings and controller, and inherits everything else.

*CONTROLLER TRAINING*

#### 2,048 robots learning at once on one GPU

PPO trains the whole-body controller in MuJoCo MJX, with 2,048 robots in parallel on a single RTX 3070. The curriculum moves from standing, to walking with arm targets, to following full-body motions.

A teacher policy with privileged data trains a student that uses only the sensors of the real robot. Stage A1, standing, is complete: survival rose from 0.05 to 0.97 in 39 million steps, in about an hour.

> Stage A1, before and after. The trained policy stands for the full 11 s test, with a maximum tilt of 2.7°.

*CONTROL RATE*

**500 Hz**

motor targets on the robot's own low-level interface, in both simulators.

*STAGE A1 SURVIVAL*

**0.05 → 0.97**

in 39 million steps, about one hour on one RTX 3070.

*MAP COVERAGE*

**96.6 %**

of the floor the robot can reach, mapped during a 60-point route.

> Mode manager and keyboard teleoperation. In HOLD the robot ignores velocity keys until an explicit resume.

*SAFETY AND TELEOPERATION*

#### Every input goes through one safety layer

The mode manager has seven modes, from DAMP, with the motors off, to HOLD. A control lease sets which source has control, a watchdog sets HOLD if the signal stops, a hardware emergency stop overrides everything and speed zones on the map cap the speed.

Operators can teleoperate the arms and hands from a webcam. MediaPipe tracks the operator, so no VR headset is needed.

> Mapping while Nav2 drives. About 5.7 hours of simulated walking, shown in 27 seconds.

*AUTONOMY*

#### A map you can check against the building

slam_toolbox maps the hospital while Nav2 with the MPPI controller drives a 60-point route through the hospital and the surgical wing. Because the simulated building is exact, the map can be scored: 99.6% of wall cells sit within 0.10 m of the Isaac Sim ground truth.

*STATUS*

Simulation stage, in development. All tests used simulation only. No test of the transfer from simulation to a real robot is complete yet.

Standing (stage A1) is trained. Walking (stage B) and full-body motion tracking (stage C) are not trained yet, so the walking in these clips uses a placeholder policy.

Code: hospital-sim and its component repositories, Apache-2.0. The renders show third-party assets under their own licences: Lightwheel SimReady (CC BY-NC 4.0), NVIDIA Isaac for Healthcare (Apache 2.0) and the NVIDIA Isaac Sim hospital building (NVIDIA Limited Use Content).

*NEXT CASE STUDY*

#### AgiBot G2 pack-off cell: a humanoid at the end of a packing line

[Read case study]

#### Planning robots for a hospital or a care setting?

We can model your building, its doors and its lifts, and test a robot's routes before it sets foot on a ward.

[Talk to us]

[How a programme starts]

---

## Page: Company (`company.html`)

Browser title: Company: Kyne Robotics  
Meta description: Kyne Robotics builds software that automates localised humanoid deployment, with engineers who install and support it on site.

*COMPANY*

### We build localised deployment automation for humanoids

Kyne Robotics makes Unitree, AgiBot and other off-the-shelf humanoids do useful work. Our software adapts each robot to a specific site and trains it for the job, and our engineers integrate it on site.

*WHY KYNE EXISTS*

#### Robots you can order still need someone to make them useful

Humanoid hardware is now something you can buy. What arrives is a capable machine with a walking controller and an SDK.

Getting it to pack a carton at the end of a line, or to push through a fire door and wait for a lift, is a separate piece of work. It takes task software, trained policies, a safety layer and days on site with the people who run the process, and it is the piece most buyers underestimate.

Kyne does that piece, and automates as much of it as possible: the site model, the training data, the training and the tests. We work across manufacturers, so whichever robot fits your task, our software makes it work in your building.

*HOW WE WORK*

#### Five habits we bring to every site

*01*

##### Start in simulation

We test your task on a model of your site before a robot is bought or moved. A problem found there is far cheaper to fix than one found on the floor.

*02*

##### Use the real interface from day one

Code written against the manufacturer's SDK in simulation runs on the robot without a rewrite.

*03*

##### Say where every number came from

Each figure we publish comes with its method and the stage it was measured at.

*04*

##### Be clear about the limits

Simulation is weak on soft goods and on people. We say so, and we test those parts on hardware early.

*05*

##### Pick the robot for the task

We are not tied to a manufacturer, and sometimes the right answer is a conveyor.

*BASED IN LONDON*

##### On site when it matters

Simulation and training run on our workstations and on cloud GPUs. Integration happens at your site, in person.

*FOUNDER*

#### Rakshith Bangalore Kumaraswamy

Kyne is led by Rakshith Bangalore Kumaraswamy, a robotics engineer with a background in humanoid R&D. He has trained neural policies for legged control and worked on actuator identification and the sim-to-real gap on platforms such as the Unitree H1-2.

He built both projects on this site, the AgiBot G2 pack-off cell and WardZero, and hosts the Unfiltered Robotics podcast.

[GitHub]

[See the projects]

#### Who we want to hear from

Operations and engineering leads weighing up humanoids, teams with a robot that is not yet doing its job, and manufacturers looking for an application partner.

[Talk to us]

---

## Page: Contact (`contact.html`)

Browser title: Contact: Kyne Robotics  
Meta description: Tell Kyne Robotics about your site and the job you want a robot to do. We reply personally and usually suggest a simulation study first.

*CONTACT*

### Tell us about your site

Whether you are scoping a first humanoid programme or you already have a robot that needs to do a job, start here.

*ENQUIRY*

*NAME*

*WORK EMAIL*

*COMPANY*

*ROLE*

*WHAT ARE YOU LOOKING AT?*

Field: Do you have a robot yet?

*NOT YET*

*EVALUATING MODELS*

*ORDERED*

*ON SITE*

*SITE AND INDUSTRY*

*THE JOB YOU WANT A ROBOT TO DO*

We use your details only to reply to this enquiry.

[Send enquiry]

*WHAT HAPPENS NEXT*

- We read your note and reply personally.

- A call about the site, the task and the constraints.

- A proposal. Usually a simulation study first, or a scoped project if you already have hardware.

*DIRECT*

hello@kynerobotics.com

Based in London. We travel to client sites for integration work.

#### Not ready to talk yet?

Read how a humanoid programme starts, or look at the two projects in detail.

[Humanoid programmes]

[Our work]

---

## Page: Page not found (`404.html`)

Browser title: Page not found: Kyne Robotics  
Meta description: 

*404*

### This door does not lead anywhere

The page you asked for is not here. It may have moved.

[Go to the home page]

[Talk to us]

---

## Shared footer

Kyne

Software that automates localised humanoid deployment.

#### Services

- Application software

- Policy training

- On-site integration

#### Programmes

- Simulation study

- What you get

- Questions

#### Work

- AgiBot G2 pack-off cell

- WardZero

#### Company

- Technology

- About

- Contact

- GitHub

Copyright © 2026 Kyne Robotics. London, United Kingdom. Project media shows simulation renders. Third-party assets keep their own licences, listed on each case study.
