
#!/bin/bash
echo -e "Building image old_machine_vision:latest"

DOCKER_BUILDKIT=1 \
docker build --pull --rm -f .docker/Dockerfile \
--build-arg BUILDKIT_INLINE_CACHE=1 \
--tag old_machine_vision:latest .

