---
layout: post
title: Community Bonding week3
---

## Test available arm manipulator, gripper, AGV and world for ROS and Gazebo9

In our [industrial robot repo](https://github.com/sixer51/IndustrialRobotics), we provided model, related configuration files and example usage of manipulator abb irb 120 and gripper robotiq 85 in Gazebo and Rviz. Users can already use it to do some manipulation simulations. However, for the need of developing more exercises, I should also test some other available arm manipulator, gripper, AGV and world packages, including model, related configuration files, and make sure they can run in Gazebo9 and Rviz.

### Arm Manipulator and Gripper
UR5 robot is the first manipulator I tested. It has been used by many people and can work properly. The model can be shown in Gazebo and Rviz. Planning and execution with MoveIt also work without any problems. I only saved required files for UR5 and deleted unnessary files for some other universal robot in [my repo](https://github.com/sixer51/universal_robot/tree/melodic-devel) to minimize the size of the package.  
Yuxiang Gao and Yeping Wang made a [package for UR5 arm and Robotiq 140 Gripper](https://github.com/intuitivecomputing/ur5_with_robotiq_gripper) in ROS kinetic. It requires some more work to migrate to ROS melodic, but it can be seen as a good example package of combination of UR5 and robotiq gripper.
![ur5_robotiq](https://raw.githubusercontent.com/intuitivecomputing/ur5_with_robotiq_gripper/master/img/simulation.png){: .mx-auto.d-block :}

Panda arm is the example manipulator in MoveIt simulator, so it is promised to work properly with MoveIt in Rviz. Erdal Pekel integrated it into Gazebo in [this repo](https://github.com/erdalpekel/panda_simulation). It requires an extra library which takes a few more time to install, but works well in my test in Gazebo and Rviz.
![panda](https://raw.githubusercontent.com/erdalpekel/panda_simulation/master/assets/panda-in-gazebo.png){: .mx-auto.d-block :}

### AGV with Arm Manipulator and Gripper

Neobotix mmo500 is an combination of mobile omnidirection robot, universal robot arm and a soft gripper. The company provides [simulation kit](https://docs.neobotix.de/display/ROSSim/ROS-Simulation) of all their robots including mmo500. When I tested its package, world and model can shown in Gazebo and Rviz, but there are still some spawning error need to be fixed. The gripper should also be changed with vacuum gripper 
![mmo500](https://docs.neobotix.de/download/attachments/328076/neo_website_img2.jpg?version=1&modificationDate=1566478792000&api=v2){: .mx-auto.d-block :}

### World of Warehouse Environment

[Agile Robotics for Industrial Automation Competition](https://www.nist.gov/el/intelligent-systems-division-73500/agile-robotics-industrial-automation-competition) (ARIAC) is held by National Institute of Standards and Technology(NIST), USA, since 2017. The competition is simulation-based and designed to promote robot agility by utilizing the latest advances in artificial intelligence and robot planning. Warehouse environment and objects in Gazebo, arm manipulator(UR10), vacuum gripper and some sensors are all integrated and provided. The kits of [2017](https://bitbucket.org/osrf/ariac/wiki/2017/Home.md) and [2018](https://bitbucket.org/osrf/ariac/wiki/2018/Home.md) are built in Ubuntu 16.04 and ROS kinetic which might need some mdification to work in UBuntu 18.04 and ROS melodic. I tested the kit of [2019](https://bitbucket.org/osrf/ariac/wiki/2019/Home) and it can show the environment in Gazebo properly. The [2020](https://github.com/usnistgov/ARIAC) kit should also work, but it is too complex for our current design of exercise, so I didn't test it.

ARIAC 2020, consisting of kit building in a simulated warehouse with robot arm, dual-arm gantry robot and dynamic obstacles
![ARIAC 2020, consisting of kit building in a simulated warehouse with robot arm, dual-arm gantry robot and dynamic obstacles](https://raw.githubusercontent.com/usnistgov/ARIAC/master/wiki/figures/ariac2020_3.jpg){: .mx-auto.d-block :}

ARIAC 2019, consisting of kit building in a simulated warehouse with two robot arms
![ARIAC 2019, consisting of kit building in a simulated warehouse with two robot arms](https://bitbucket.org/repo/pB4bBb/images/4199357480-ariac_2019_workcell.png){: .mx-auto.d-block :}

ARIAC 2018, consisting of order fulfillment in a simulated shipping container
![ARIAC 2018, consisting of order fulfillment in a simulated shipping container](https://bytebucket.org/osrf/ariac/wiki/2018/img/ariac_2018.jpg?rev=b866d999f664497bac55adbb51a13068c87a1b9d){: .mx-auto.d-block :}

ARIAC 2017, consisting of kit building in a simulated warehouse
![ARIAC 2017, consisting of kit building in a simulated2020-05-24-community_bonding_week3 warehouse](https://bitbucket.org/repo/pB4bBb/images/1577073220-ARIAC_full.png){: .mx-auto.d-block :}


## Test MoveIt Grasp package

With the [tutorial](https://ros-planning.github.io/moveit_tutorials/doc/moveit_grasps/moveit_grasps_tutorial.html) of MoveIt Grasp, I tested the example usage with panda arm manipulator, two finger gripper and vacuum gripper. As a new package, it is still unstable. It can show similar result as shown in the tutorial, but there is also some spawning errors and some undesired performances. To get it work, you should git clone the master branch, but not the melodic-devel branch of the [repo](https://github.com/ros-planning/moveit_grasps). More efforts are needed to get this package work properly, but if it can work, grasping tasks would become much easier. In the end of the tutorial, they mentions that this package has been tested with UR5, Jaco2, Baxter, REEM and Panda robot. Considering packages that I have tested, if we want to use this grasp package in our exercise, both UR5 and Panda arm mainpulator are good choice.