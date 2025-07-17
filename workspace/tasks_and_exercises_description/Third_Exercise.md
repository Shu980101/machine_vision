## Description of the third (and last) exercise (mobile manipulators)

The third **exercise goal** will be to use mobile AGVs (including a robotic arm) to perform pick and place operations in a realistic industrial warehouse. The student will use a combination of the **ROS Navigation** stack (including making an occupancy map and self-localization) + **MoveIt** (our API using pick() and place() methods)

#### Gazebo world for the exercise (first draft)

- **AGV + Arm + gripper**: Neobotix AGV (check both MMO-500 and MMO-700) with UR10 arm, from the [Neobotix repo](https://github.com/neobotix/neo_simulation). If Neobotix gives permission, modify it to include a small tray to carry objects

- <img src="https://www.neobotix-roboter.de/fileadmin/_processed_/0/d/csm_MMO-500-UR10-Main_%C3%BCbersicht_2ed8566837.jpg" alt="Neobotix MM=-500" style="zoom:50%;" />

  

- **Scene objects :**

  - A "realistic" industrial warehouse, squared (or rectangular) in shape. 

  - Pick objects (different shapes and colors) will be placed in a source table. 

  - Three conveyor belts (or similar) will be used as targets (by color, or shape). Adjust position and heights to allow 2D detection by onboard AGV Lidars. 

    

- **Test:**
  - **Test 1:** pick and place of three objects in different targets, one at a time.. 
  - **Test 2:** pick and place of three objects using the onboard tray.. 