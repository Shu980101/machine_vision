---
layout: post
title: Community Bonding week4
---

## Pick and Place Demos in Gazebo

In the last week of Community Bonding period, two pick and place demos are implemented in Gazebo, which are the bases of our first exercise. The demonstration videos can be seen by clicking following pictures.

When preparing the project proposal, a [pick demo with irb120 manipulator and robotiq85 gripper was implemented in Rviz](https://www.youtube.com/watch?v=ztYnRgs7ipI), but we can only see the robot arm and gripper moving without seeing any objects in Gazebo because objects are generated in planning scene instead of Gazebo world. There were also some problems with planning and placing. In these two new demos, the robot is picking and placing objects in Gazebo world. I will discussed about the details of these two demos separatly.

### Pick and plaze with irb120 robot arm and robotiq85 gripper
To implement this demo, there are mainly two parts to be added based on the provided [industrial robot repo](https://github.com/JdeRobot/IndustrialRobotics/tree/melodic-devel). The first one is a world file with objects to be picked.  The second one is the [gazebo_grasp_fix plugin](https://github.com/jenniferBuehler/gazebo-pkgs/wiki/The-Gazebo-grasp-fix-plugin). The first part is easy, so I will only introduce the second part.

{: .box-note} 
**Note:** The melodic version of our official [industrial robot repo](https://github.com/JdeRobot/IndustrialRobotics/tree/melodic-devel) has been updated in the melodic-devel branch. Now users can follow the instrcution in that repo to start simulation with irb120 robot arm manipulator and robotiq85 gripper in Gazebo and Rviz. Example code of forward kinematic, inverse kinematic and Cartesian path planning are provided previously. A new example template of pick and place task will be updated later.

The reason for using gazebo_grasp_fix plugin is that it is very hard to simulate grasping object with robot hand in Gazebo. Without it, you would easily see the object slipping off the robot hand all the time. It may be possible to make it work, but will require much time in tuning URDF and object property. It is suggested to use this plugin if simulating a good grasping behavior is not of immediate priority to a project. I tried to change some parameters such as friction coeffition, object weight, but none of them help to solve sliping problem, so finally I choose to use this plugin.

The tutorial of using gazebo_grasp_fix plugin is [here](https://github.com/jenniferBuehler/gazebo-pkgs/wiki/The-Gazebo-grasp-fix-plugin). A challenge in using this plugin is to find what are the "palm_link" and "gripper_link" of your gripper. Palm_link is the link that finger joints are attached. Gripper_link are the links which are used to actively grasp objects. It seems to be clear, but actually not. You can't direcly use the links defined in URDF because multiple links will be combined in Gazebo, but valid links can be found in Gazebo GUI. There is only one "palm_link" which is the root link of all "gripper_links" even if there are some other links connecting gripper links and palm link. Then "gripper_links" are links that will directly contact with objects. It might be confused for some grippers with complex structure.

However, this plugin still doesn't work very well in my demo. It sometimes cannot detect the contact between gripper links and objects which make the object slip off. I am still trying to figure out the reason for this problem to make this pick and place function work stably.

[![irb20 and robotiq85](https://img.youtube.com/vi/55z6pJ_YAt4/0.jpg){: .mx-auto.d-block :}](https://youtu.be/55z6pJ_YAt4)

### Pick and place with UR5 robot arm and vaccum gripper
This demo is based on [ROS-I universal robotics official repo](https://github.com/ros-industrial/universal_robot) which I have tested last week. The main component of this demo is [gazebo_ros_vacuum_gripper plugin](https://github.com/start-jsk/jsk_apc/blob/76db5dd1aab662f55a71e7e3157789ca1c018e21/jsk_2015_05_baxter_apc/robots/baxter.gazebo#L39-L69). I also took [Lihuang's repo](https://github.com/lihuang3/ur5_ROS-Gazebo) which realizes pick and place with UR5 and vacuum gripper in ROS kinetic as reference. 

[![ur5 and vacuum gripper](https://img.youtube.com/vi/SD70gaJ5XG4/0.jpg){: .mx-auto.d-block :}](https://youtu.be/SD70gaJ5XG4)

With Lihuang's example package, it is easier to get the vacuum gripper work in Gazebo, but there are also some problems need to be solved. The first one is some spawning warnings saying the state of gripper links are unknown which doesn't influence the simulation, but makes the terminal unclear to visulize some other information. The second one is that if I delete the camera link in URDF file which actually has no relationship with gripper, the grippers can no longer be generated. The last one is the limited force of each vacuum gripper. Multiple vacuum grippers are needed to grasp a small object.