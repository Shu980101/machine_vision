#!/usr/bin/env bash

# Set the user variables
USER_NAME="${USER:-shu}"  # Default to "shu" if $USER is not set

echo -e "Starting up old_machine_vision container"
echo -e " >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"

# Allow GUI access
xhost +local:

# Check if NVIDIA GPU is available
if command -v nvidia-smi &> /dev/null && nvidia-smi &> /dev/null; then
    echo "NVIDIA GPU detected, using GPU acceleration"
    GPU_FLAGS="--gpus all"
    RUNTIME_FLAG="--runtime=nvidia"
else
    echo "No NVIDIA GPU detected, using software rendering"
    GPU_FLAGS=""
    RUNTIME_FLAG=""
fi

# Running the container with the user and GUI access
docker run -it --rm --privileged \
    $RUNTIME_FLAG \
    $GPU_FLAGS \
    --user "$(id -u $USER_NAME):$(id -g $USER_NAME)" \
    --group-add sudo \
    --env="DISPLAY=$DISPLAY" \
    --env="USER=$USER_NAME" \
    --env="HOME=/home/$USER_NAME" \
    --env=QT_X11_NO_MITSHM=1 \
    --env=LIBGL_ALWAYS_INDIRECT=0 \
    --env=LIBGL_ALWAYS_SOFTWARE=0 \
    --env=MESA_GL_VERSION_OVERRIDE=3.3 \
    --env=MESA_GLSL_VERSION_OVERRIDE=330 \
    --env=XAUTHORITY=/home/$USER_NAME/.Xauthority \
    --env=NVIDIA_VISIBLE_DEVICES=all \
    --env=NVIDIA_DRIVER_CAPABILITIES=all \
    --workdir="/catkin_ws" \
    --volume="/home/$USER_NAME:/home/$USER_NAME" \
    --volume="/etc/group:/etc/group:ro" \
    --volume="/etc/passwd:/etc/passwd:ro" \
    --volume="/tmp/.X11-unix:/tmp/.X11-unix:rw" \
    --volume="/run/user/$(id -u $USER_NAME):/run/user/$(id -u $USER_NAME)" \
    --volume="/dev/dri:/dev/dri" \
    --volume="/dev:/dev" \
    --volume="$(pwd)/workspace:/catkin_ws/src/workspace" \
    --net=host \
    --ipc=host \
    --pid=host \
    old_machine_vision:latest \
    /bin/bash
