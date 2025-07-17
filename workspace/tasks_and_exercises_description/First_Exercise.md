## Description of the first exercise (simple pick and place)

This first exercise will be the entry point for the new **Industrial Robotics exercises** of our JdeRobot Robotics Academy. It will be based in simple *pick and place* operations with a single robotic manipulator and a mechanical gripper. 

The **exercise goal** will be to perform a complete pick and place of several objects, to complete a sorting task (sort objects by color, by shape, in different trays or boxes)

The **main objective** will be to familiarize the student with the underlying infrastructure (ROS + MoveIt + our own industrial robotics API) and with the key elements needed for more complex exercises (how launch the exercise, how code the solution, differences between Gazebo and MoveIt scene, handle obstacles, etc). 

#### Gazebo world for the exercise

- **Arm + gripper**: ABB IRB120 with Robotiq 85 2-finger parallel gripper
- **Scene objects:**
  -  Static conveyor belt (or table) with objects of different shapes (cube, cylinder, sphere), sizes and colours. Try to spawn around 6-8 objects. 
  - Three-four trays or boxes easily identifiable (using numbers or different colours). Locate them within the arm manipulator workspace, maybe at the sides of the robot (suggestion: two new tables, one in each robot side with two trays or boxes each)
  - Factory-like ground plane and sorroundings?
  - JdeRobot logo (somewhere on the ground, for example).It is available at our [jderobot _assets package](https://github.com/JdeRobot/assets), also available as ROS package.

**Important:** any new object used in Gazebo must be uploaded to our [jderobot_assets package](https://github.com/JdeRobot/assets), which contains static resources (concretely to the melodic-devel branch, in our case) 

#### Documentation and exercise theory

- Prepare documentation and exercise theory following the same format as the actual exercises (see for example the [drone gymkhana exercise](http://jderobot.github.io/RoboticsAcademy/exercises/Drones/drone_gymkhana)). Use [Jekyll](https://jekyllrb.com/) & [Minimal Mistakes](https://mademistakes.com/work/minimal-mistakes-jekyll-theme/).
- Include a detailed description of the new Industrial Robotics GUI 
- Develop a complete solution for the exercise (which will be kept in a separate repo). Add a demonstrative video with part of the exercise solution
- Take special care when describing the API section
- We will open an issue to add  the new Industrial exercises in our [JdeRobot Robotics Academy repo](https://github.com/JdeRobot/RoboticsAcademy), working in a separate branch to upload the GSoC-2020 developments during the summer.