## Description of the second exercise (add vision, collisions)

The second **exercise goal** will be to include vision (via RGBG cameras) to detect the position and orientation of the scene objects based on OpenCV techniques, using both object color and geometry. After the vision-based detection the manipulator must complete again a sorting task.

In addition, we will use vision for **automatic detection of collisions** in the scene, creating an Occupancy Map (octomap) using the MoveIt available tools (which work with 3D perception via point clouds or depth images)  

#### Gazebo world for the exercise

- **Arm + gripper**: Universal Robots UR5 + vacuum gripper
- **Scene objects:**
  -  Two depth cameras (one fixed, one attached to the manipulator end effector). 
  -  Spawn around 6-8 objects of different colors, geometries and sizes
  -  Use static objects to simulate collisions
  -  Use a different target, like custom-made organizing trays to place the objects. Something similar to this:

<img src="https://dhb3yazwboecu.cloudfront.net/990/bandeja-organizadora-de-vasos-para-lavavajillas-industriales-_l.jpg" alt="Organizing tray" style="zoom:50%;" />

