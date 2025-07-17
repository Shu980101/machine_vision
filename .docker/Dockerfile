FROM ros:melodic-ros-base

# Set the user-related arguments
ARG USERNAME=shu
ARG USER_UID=1000
ARG USER_GID=1000

ENV DEBIAN_FRONTEND=noninteractive
ENV ROS_DISTRO=melodic
ENV LIBGL_ALWAYS_INDIRECT=0

# 1. Install general tools, Python tools, and editors
RUN apt-get update && apt-get install -y \
    curl wget git sudo gnupg2 lsb-release build-essential \
    python-pip python3-pip python3-setuptools \
    python-rosdep python-rosinstall python-vcstools \
    libpcl-dev \
    nano vim emacs \
    tree htop \
    && rm -rf /var/lib/apt/lists/*

# 2. Upgrade pip and install ROS-related Python packages via pip
RUN pip install --upgrade pip && \
    pip install rospkg catkin_pkg rosdep rosinstall rosinstall_generator wstool empy

# 3. Install catkin_tools via pip3
RUN pip3 install -U pip && pip3 install 'catkin_tools<0.9.0'

# 4. Block broken .deb Python modules to avoid dpkg conflict
RUN apt-mark hold python-catkin-pkg-modules python-rospkg-modules python-rosdistro-modules

# 5. Install required ROS packages and OpenGL/GPU support
RUN apt-get update && apt-get install -y \
    dbus-x11 \
    terminator \
    mesa-utils \
    libgl1-mesa-glx \
    libgl1-mesa-dri \
    libglu1-mesa \
    libegl1-mesa \
    libxrandr2 \
    libxss1 \
    libxcursor1 \
    libxcomposite1 \
    libasound2 \
    libxi6 \
    libxtst6 \
    ros-melodic-rqt \
    ros-melodic-rqt-common-plugins \
    ros-melodic-rviz \
    ros-melodic-perception-pcl \
    ros-melodic-moveit \
    ros-melodic-octomap-ros \
    ros-melodic-octomap-msgs \
    ros-melodic-octomap-rviz-plugins \
    ros-melodic-image-view \
    ros-melodic-tf \
    ros-melodic-tf2-ros \
    ros-melodic-robot-state-publisher \
    ros-melodic-nav-core \
    ros-melodic-gazebo-msgs \
    ros-melodic-gazebo-ros \
    ros-melodic-ros-controllers \
    ros-melodic-control-toolbox \
    ros-melodic-industrial-robot-simulator \
    ros-melodic-tf-conversions \
    ros-melodic-pcl-ros \
    ros-melodic-joint-state-publisher \
    ros-melodic-gazebo-ros-control \
    ros-melodic-gazebo-ros-pkgs \
    ros-melodic-base-local-planner \
    ros-melodic-pcl-ros \
    ros-melodic-abb-driver
    
# 6. Initialize rosdep
RUN rosdep update

# Create user and group with the specified UID and GID
RUN groupadd --gid ${USER_GID} ${USERNAME} && \
    useradd --uid ${USER_UID} --gid ${USER_GID} -m ${USERNAME} && \
    usermod -aG sudo ${USERNAME}
    
# Allow passwordless sudo for the user
RUN echo "${USERNAME} ALL=(ALL) NOPASSWD:ALL" > /etc/sudoers.d/${USERNAME} && \
    chmod 0440 /etc/sudoers.d/${USERNAME}

# 7. Set up catkin workspace and clone repositories as root first
RUN mkdir -p /catkin_ws/src
WORKDIR /catkin_ws/src

# Clone Machine Vision exercise repo
#RUN git clone https://github.com/TheRoboticsClub/colab-gsoc2020-Yijia_Wu.git

# Remove duplicate packages from src_exercise to avoid conflicts
#RUN rm -rf \
#    /catkin_ws/src/colab-gsoc2020-Yijia_Wu/src_exercise/IndustrialRobotics \
#    /catkin_ws/src/colab-gsoc2020-Yijia_Wu/src_exercise/universal_robot \
#    /catkin_ws/src/colab-gsoc2020-Yijia_Wu/src_exercise/ur5_gripper_demo \
#    /catkin_ws/src/colab-gsoc2020-Yijia_Wu/src_exercise/gazebo-pkgs \
#    /catkin_ws/src/colab-gsoc2020-Yijia_Wu/src_exercise/rqt_industrial_robot

# RUN rm -rf \
#     /catkin_ws/src/colab-gsoc2020-Yijia_Wu/src_exercise/IndustrialRobotics \





# 8. Resolve ROS dependencies in workspace
WORKDIR /catkin_ws
RUN /bin/bash -c "source /opt/ros/melodic/setup.bash && \
    rosdep install --from-paths src --ignore-src --rosdistro melodic -y --skip-keys=pcl"

# 9. Build workspace as root
RUN /bin/bash -c "source /opt/ros/melodic/setup.bash && catkin build"

# 10. Change ownership of the catkin workspace to the user
RUN chown -R ${USER_UID}:${USER_GID} /catkin_ws

# 11. Set up environment for both root and user
RUN echo "source /opt/ros/melodic/setup.bash" >> ~/.bashrc && \
    echo "source /catkin_ws/devel/setup.bash" >> ~/.bashrc && \
    echo "export GAZEBO_MODEL_PATH=\$GAZEBO_MODEL_PATH:/catkin_ws/src/IndustrialRobotics/assets/models" >> ~/.bashrc

# Set up environment for the user
RUN echo "source /opt/ros/melodic/setup.bash" >> /home/${USERNAME}/.bashrc && \
    echo "source /catkin_ws/devel/setup.bash" >> /home/${USERNAME}/.bashrc && \
    echo "export GAZEBO_MODEL_PATH=\$GAZEBO_MODEL_PATH:/catkin_ws/src/IndustrialRobotics/assets/models" >> /home/${USERNAME}/.bashrc && \
    chown ${USER_UID}:${USER_GID} /home/${USERNAME}/.bashrc

# 12. Create a startup script that ensures proper environment setup
RUN echo '#!/bin/bash' > /startup.sh && \
    echo 'source /opt/ros/melodic/setup.bash' >> /startup.sh && \
    echo 'source /catkin_ws/devel/setup.bash' >> /startup.sh && \
    echo 'export GAZEBO_MODEL_PATH=$GAZEBO_MODEL_PATH:/catkin_ws/src/IndustrialRobotics/assets/models' >> /startup.sh && \
    echo 'exec "$@"' >> /startup.sh && \
    chmod +x /startup.sh

# 13. Default command
ENTRYPOINT ["/startup.sh"]
CMD ["/bin/bash"]
