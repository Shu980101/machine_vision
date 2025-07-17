---
layout: post
title: Conclusion
---

## Project Introduction

The goal of this project is to develop a set of robot manipulation exercises with incremental complexity for JdeRobot Robotic Academy users. With these exercises, users can gain a better understanding of the processing of a manipulation task which mainly includes perception, planning and control. They can also become more familiar with some popular working frameworks in robotics: ROS, Gazebo, MoveIt, and some well-known open-source computer vision libraries: OpenCV and PCL.

## Initial Goal and Progress

The initial goal for this project is to release four exercises: classical pick and place tasks without and with vision assistance, picking from warehouse racks with an industrial mobile manipulator, cooperation between AGV and fixed manipulator to pick objects from a conveyor belt and delivery to the target position. 

However, considering the limitation and difficulties related to manipulation simulation we found in last three months, we finally decide to develop three industrial robotics exercise during GSoC period. The details of final results can be seen in following sections.

## Contributions

Three new industrial robotics exercises are released in JdeRobot Robotic Academy: Pick and Place, Machine Vision and Mobile Manipulation.  

[Documentation](https://jderobot.github.io/RoboticsAcademy/exercises/industrial_robots_section): User manual of three exercises, including introduction, installation guidance, API and GUI introduction, theory, hints and solution demonstration videos  

[Update in Industrial Robot Repo](https://github.com/JdeRobot/IndustrialRobotics):
- `assets`: worlds and Gazebo models
- `industrial_robots`: robot simulation packages, 
- `rqt_industrial_robots`: rqt-based GUI for three exercise

[Update in JdeRobot Robotics Academy Repo](https://github.com/JdeRobot/RoboticsAcademy): worlds, launch files, script files of three exercises

### Exercise one: Pick and Place
**Task:** Pick objects from a conveyor and place them to the box with the same color. Objects and Obstacles shape, color and pose are known.   
**Robot:** [IRB120](https://new.abb.com/products/robotics/industrial-robots/irb-120)  
**Gripper:** [robotiq85](https://robotiq.com/products/2f85-140-adaptive-robot-gripper)(two-finger mechanical gripper)  
**Sensor:** None  
[Tutorial](https://jderobot.github.io/RoboticsAcademy/exercises/IndustrialRobots/pick_place)  
**Domonstration Video:** 
[![solution](https://img.youtube.com/vi/kJMPz80w9BM/0.jpg){: .mx-auto.d-block :}](https://youtu.be/kJMPz80w9BM)

### Exercise two: Machine Vision
**Task:** Pick objects from a conveyor and place them to a box. Objects shape, color are known. The pose of objects should be detected using color and shape filter. The obstacles should be detected from point cloud.   
**Robot:** [UR5](https://www.universal-robots.com/products/ur5-robot/)  
**Gripper:** vacuum gripper(self-made)  
**Sensor:** kinect camera  
[Tutorial](https://jderobot.github.io/RoboticsAcademy/exercises/IndustrialRobots/machine_vision)    
**Domonstration Video:** 
[![solution](https://img.youtube.com/vi/LHq4ZA2lGxQ/0.jpg){: .mx-auto.d-block :}](https://youtu.be/LHq4ZA2lGxQ)

### Exercise three: Mobile Manipulator
**Task:** Pick objects on a conveyor and place them to trays on other conveyors. Objects and Obstacles shape, color and pose in world frame are known. 
**Robot:** [MMO-500](https://docs.neobotix.de/display/ROSSim/Robots)(mobile manipulator from Neobotix, combining AGV and UR5)  
**Gripper:** [Modular Grasper](https://www.shadowrobot.com/products/modular-grasper/)(three-finger mechanical gripper from Shadow Robot Company)   
**Sensor:** laser   
[Tutorial](https://jderobot.github.io/RoboticsAcademy/exercises/IndustrialRobots/mobile_manipulation)    
**Domonstration Video:** 
[![solution](https://img.youtube.com/vi/0oNY_UHu2cU/0.jpg){: .mx-auto.d-block :}](https://youtu.be/0oNY_UHu2cU)

## Future work

I still plan to keep working for JdeRobot Academy to improve the industrial robot exercises. Something that can be considered to do as next step for industrial robotics exercises are list as follows.
1. **Improve grasping stability:**  
Currently, I am using modified `gazebo_grasp_fix` plugin for mechanical gripper and `gazebo_ros_vacuum_gripper` for vacuum gripper. The modified version `gazebo_grasp_fix` plugin can slightly improve the possibility to grasp object, but we can still usually see the object oscillating while grasping. The `gazebo_ros_vacuum_gripper` plugin is still unstable to use in manipulation unless grasping small and light object as it only provides force but doesn't fix the object with the gripper as `gazebo_grasp_fix` plugin, so adding fixing object and gripper link functionality to this plugin might help a lot.

2. **More complex world and objects:**  
In these three exercises, objects are all single color, regular shape(box, sphere and cylinder). The setup of Gazebo world and obstacles are also simple. When the grasping, perception, planning functionalities are improved, more complex world and objects might be able to used in our future exercises which would be similar to real industrial application.

3. **Inculde more machine vision methods:**  
The method we use in machine vision exercise is color filter and shape filter in PCL which can only deals with single color and sphere or cylinder shape objects. There are actually more machine vision method can be used, such as pointcloud registration in PCL and some 2D detection method in OpenCV.

4. **Integration perception, navigation and manipulation:**  
Currently, mobile manipulation exercise only integrated navigation and manipulation because the implemented perception function is still limited. Once the perception side is ready to use, we can implment more realistic mobile manipulation tasks.

5. **Update to ROS2, Navigation2 and MoveIt2:**  
In ROS2, the navigation package Navigation2 and motion planning library MoveIt2 are both latest version. With the improved functionalities and features in these packages can probably improve the behavior of industrial robot exercises.