# Docker for ML
Docker for Machine Learning &amp; Data Science

# What is Docker?
- Tool that can package an application along with its dependencies in a container. This container can run on a Linux Server.
- Makes it easy to replicate the project. Enables to deploy the container to the cloud or share it with the team.
- Docker container are very lightweight.

# What is a Container?
- A container is a runnable instance of an Image.
- An abstraction at applayer that packages code and dependencies together.
- Multiple containers can run on the same machine and can share the OS-Kernel with other containers.
- Each container running in isolated processes.
- Containers take up less space than virtual machines and they can handle more applications.

# Container vs. VM
- VMs are demanding, they can take up multiple GBs of space.
- VMs can be slow, because they have to boot up an entire OS.
- VMs are abstractions of physical hardware, turning one server into many servers.

# Getting started
- Dockerfile: Contains instructions to build a container
- Build image: ``docker build -t testimage .``
- Show images: ``docker images --all``
- Build container: ``docker run --name testcontainer -p 5000:5000 testimage``
- Common commands:
- - Container status: ``docker ps``
- - Show images: ``docker images ls``
- - Changes in a running container: Open CLI of a running container in Docker dashboard
- - Logs: ``docker logs``
- - Remove container: ``docker rm``
- - Remove image: ``docker rmi``
- - Dockerhub login: ``docker login``
- - Tag an image: ``docker tag testimage dstoecklein/testimagerepo:hubtest`` <image username/reponame:tag>
- - Push to Dockerhub: ``docker push dstoecklein/testimagerepo:hubtest``
- - Pulling from Dockerhub: ``docker pull imagename``
- - Updating an Image: Recommended is to build a new image (consider containers as immutable)

# Volumes
- Share data between containers
- Commands:
- - Create Volume: ``docker volume create testvolume``
- - List Volumes: ``docker volume list``
- - Inspect Volume: ``docker volume inspect testvolume``
- - Create container1: ``docker run -it --name=testvolume1 --mount source=testvolume,destination=/testvolume alpine`` -> ``cd testvolume`` -> ``touch examplevolumetest.txt``
- - Create container2: ``docker run -it --name=newtestvolume --mount source=testvolume,destination=/testvolume alpine `` -> ``cd testvolume`` -> ``ls`` -> shows the ``examplevolumetest.txt`` file
- - Exit: ``exit``

# Compose
- Running and defining multiple container applications.
- Defined in a ``docker-compose.yml`` file.

# Kubernetes
- Tool for container orchestration