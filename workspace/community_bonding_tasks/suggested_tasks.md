## Community Bonding period (May 4 - May 31, 2020)

The idea is to use this period to improve our understanding about the infrastructure, prepare some stuff and do some testing, at an easy pace. So we'll be good to go when the Coding period starts in June!

This is the list of suggestions: 

#### 1. Install and play with JdeRobot Robotics Academy

- Install [Robotics Academy](https://github.com/JdeRobot/RoboticsAcademy). Check available exercises, which are described in the [Robotics Academy website](https://jderobot.github.io/RoboticsAcademy/exercises/)
- Become familiar with the way the student work (source code in a ROS template, launched from a GUI) and with the typical documentation available for him/her. We'll need to replicate it in our exercises. 
- Have a look at the [Academy forum](https://developers.unibotics.org/) and the developers slack channel from time to time.
- Try to solve a couple of exercises to understand the structure of a typical exercise in our Academy.... and have fun! :smile: 

------

#### 2. Migrate the Industrial Robotics repo to Ubuntu 18.04 + ROS Melodic. Fix the current errors

We need to be compatible with the other exercises in the Academy, so we should do our best to stick to Ubuntu 18.04+ ROS Melodic. The [present JdeRobot Industrial Robotics repo](https://github.com/JdeRobot/IndustrialRobotics/tree/master/irb120_robotiq85) is based the ABB IRB 120 6-axis manipulator from the [ABB Experimental metapackage](http://wiki.ros.org/abb_experimental) with a Robotiq 85 gripper from the [Stanley Innovations repo](https://github.com/StanleyInnovation/robotiq_85_gripper), **both for ROS Kinetic**. 

So, the suggestion is:

- Explore updating the actual repo to Ubuntu 18.04 + ROS Melodic

- Fix the spawning errors and warnings ([TEST 1 in the Industrial Robotics Challenge](https://wiki.jderobot.org/store/jmplaza/uploads/gsoc/gsoc2020-academy_test.pdf))

- Explore how make our repo self-contained? (copy URDF, xacro, config files needed) 

  

------

#### 3. Test some available robotic arms, grippers and Industrial AGVs for ROS/Gazebo 9 

We'll propose each new exercise in Industrial Robotics using a different robotic arm or AGV model in Gazebo. It could be a good idea to make a list of aomw available possibilities. The key point for us is if they have a working model for Gazebo 9, checking the [type of ros controller](http://wiki.ros.org/ros_control) implemented (joint_trajectory based on position, velocity, effort... )

The [ROS-Industrial repos](https://github.com/ros-industrial) are a very good source to start searching: 

- **Arm manipulators**:
  
  - ABB IRB120 and IRB1200: [ABB experimental metapackage](https://github.com/ros-industrial/abb_experimental) in ROS-Industrial
  - Universal Robot UR5. [UR metapackage](https://github.com/ros-industrial/universal_robot) in ROS-Industrial 
  - Franka Emika Panda. Gazebo simulation described [here](https://erdalpekel.de/?p=55). 
  
- **Grippers and other end effectors**:
  
- Robotiq 85. [Repo from Stanley Innovations](git clone https://github.com/StanleyInnovation/robotiq_85_gripper.git), for Gazebo 7. 
  
- **Industrial AGV with Robotic Arm**? (If not available we'll have to build one for us)

  

------

#### 4. What can MoveIt do? Explore Python API, the new GRASP package and make pick and place work in Gazebo

MoveIt is a complex package. And the [available tutorials](https://ros-planning.github.io/moveit_tutorials/) explore in detail the C++ ROS API, but lack the same precise information about the Python API, that will be our only choice:

So we should spend some time to:

- Read the [MoveIt documentation](https://moveit.ros.org/documentation/) and explore the [available tutorials](https://ros-planning.github.io/moveit_tutorials/) to understand what can (and cannot) be done with MoveIt
- Understand **moveit_commander** resources, the Python interface to the Move Group node. Explore the methods available in each class. Make simple tests with the resources we think we'll need for the Academy exercises (how use the [grasp type message](http://docs.ros.org/api/moveit_msgs/html/msg/Grasp.html) to use with pick(), place()...) 
  - [Move Group Commander](http://docs.ros.org/melodic/api/moveit_commander/html/classmoveit__commander_1_1move__group_1_1MoveGroupCommander.html)
  - [Planning Scene Interface](http://docs.ros.org/melodic/api/moveit_commander/html/classmoveit__commander_1_1planning__scene__interface_1_1PlanningSceneInterface.html)
  - [Robot Commander](http://docs.ros.org/melodic/api/moveit_commander/html/classmoveit__commander_1_1robot_1_1RobotCommander.html)
  - Perception pipeline 

In addition, in [November 2019](https://moveit.ros.org/moveit/ros/2019/11/18/moveit-grasps.html) the [package MoveIt Grasps](https://github.com/ros-planning/moveit_grasps) was introduced. It consist in a **grasps generator** which can replace the pick and place classic MoveIt pipeline, allowing to [define gripper properties, calculate an visualize grasp generation](https://ros-planning.github.io/moveit_tutorials/doc/moveit_grasps/moveit_grasps_tutorial.html), etc. 

- Have a look at the [MoveIt Grasp repo](https://github.com/ros-planning/moveit_grasps).	
- Is there Python interface in Grasp? Build a simple example



------

#### 5. Pick and place in Gazebo: the grasp fix plugin

MoveIt is generally used with real arm manipulators, not with Gazebo. So we need to explore how make pick and place work in Gazebo. It is generally based in the package **gazebo_grasp_plugin**, a model plugin for GAzebo available [here](https://github.com/JenniferBuehler/gazebo-pkgs/tree/master/gazebo_grasp_plugin).  

- Read the [documentation](https://github.com/JenniferBuehler/gazebo-pkgs/wiki/The-Gazebo-grasp-fix-plugin) of the plugin and the [tutorial of Grasping with Jaco](https://github.com/JenniferBuehler/grasp-execution-pkgs/wiki/Grasping-with-Jaco-in-Gazebo)
- Prepare a simple pick and place working example with our ABB IRB 120 + Robotiq 85 setup. 
- Record and publish a video in the JdeRobot YouTube channel. 



------

#### 6. Explore the integration of MoveIt and RViz with RQT

The Robotics Academy exercises typically use a GUI to teleoperate the robots and to launch the student solution. We'll be working with MoveIt, which has a[ nice plugin for Rviz](https://ros-planning.github.io/moveit_tutorials/doc/quickstart_in_rviz/quickstart_in_rviz_tutorial.html) visualizer. 

Interestingly, there is a metapackage available called [rqt_robot_plugins](http://wiki.ros.org/rqt/Plugins#Robot-interaction_tools_.28rqt_robot_plugins.29) that include some visualization tools we should explore. The idea is to know if we can build our own exercise GUI for Industrial Robotics Exercises , similar to the existing one for drone-exercises, for example. 

Plugins to explore:

- [rqt_moveit](http://wiki.ros.org/rqt_moveit?distro=melodic): An rqt-based tool that assists monitoring tasks for MoveIt!
- [rqt_rviz](http://wiki.ros.org/rqt_rviz): RViz embedding in rqt



And...that's it. We're ready to start!! :smiley: 