## Description of GUI for Industrial Robotics Exercises

As the new Industrial Robotic exercises are quite different than the rest of the exercises in our Robotics Academy (in part because we now build on top of MoveIt) we need to implement a new RQT-based GUI with the following functionalities:

#### 1. Robot arm state + teleoperator

- Show angle value of each joint (including end effector if its articulated). Include angle limits, read from yaml file.
- Show position and orientation of end effector.
- Operate arm by **Forward Kinematics**, via sliders or similar for each joint. Something similar to what is implemented in the *Joints* tab of the *MotionPlanning* panel in RViz
- Operate arm by **Inverse Kinematics**, being able to set the position (x,y,z) and orientation (r,p,y) of the end effector. Button to plan and execute trajectory.

- **Optional**: Name of available Planning Groups in the scene? Possibility to select any of them to plan and execute? To be tested. 

#### 2. Launch and manage student code  

- Button to launch student code (will be in solution.py) 
- Button to stop student code
- Message box (Code running, code stopped, etc)
- **Important**: code in these exercises will not need default cyclic execution as in others, so implementing hot-reloading for the student code would be nice :-)

#### 3. Camera viewer

- Similar to other existing exercises in the Robotics Academy. Just for exercises with depth camera. Two image streams: original and filtered images. 

#### 4. Scene Visualizer?

How could we visualize the robot and the rest of the scene?

- **Very easy option**: add just a button to launch RViz configured to launch the MoveIt *MotionPlanner* 
- **Not-so-easy option**: Check if embedding RViz visualization in RQT works. The [list of RQT available plugins](http://wiki.ros.org/rqt/Plugins) has a [rqt_rviz plugin] which, in theory, *provides a GUI plugin embedding RViz*



**Final note**: *An implementation approach for could be the use of different .perspective files for each GUI functionality. This is currently being done with the drone_teleop for the drone exercises. The different perspectives are included in the jderobot_assets package*