# List of Contents
- [List of Contents](#list-of-contents)
- [Introduction](#introduction)
- [Common Commands](#common-commands)
  - [Docker Commands Options](#docker-commands-options)
      - [`run`](#run)
      - [`create`](#create)
      - [`start`](#start)
      - [`stop`](#stop)
      - [`rm`](#rm)
      - [`exec`](#exec)
      - [`ls`](#ls)
      - [`inspect`](#inspect)
      - [`logs`](#logs)
      - [`top`](#top)
  - [Experiment: create/run/delete a container](#experiment-createrundelete-a-container)
  - [Docker Networks](#docker-networks)
    - [Commands](#commands)
  - [Working with images](#working-with-images)
    - [Notes](#notes)
  - [Docker Images](#docker-images)
    - [Docker File](#docker-file)

# Introduction

- **Containers** are a solution to the problem of how to get software to run reliably when moved from one computing environment to another. This could be from a developer's laptop to a test environment, from a staging environment into production, and perhaps from a physical machine in a data center to a virtual machine in a private or public cloud.
  - Containers aren't Mini-VM's. However, they are **processes**. In other words, they are packages of software.
  - Containers are limited to what resources they can access.
  - Each container has a **unique** name and ID.
- **Containerization** is the lightweight alternative to a full machine. It involves encapsulating an application in a container with its own operating environment.
- **Docker** is a platform for developers and sysadmins to develop, deploy, and run applications with containers.
  - **Docker Desktop** is an application for MacOS and Windows machines for the building and sharing of containerized applications and microservices.
- **Image** is a lightweight, stand-alone, executable package that includes everything needed to run a piece of software, including the code, a runtime, libraries, environment variables, and config files.
  - **Image** is the application we want to run. However, **Container** is an instance of that image running as a process. (many containers can run from the *same image*)
  - [**Docker Hub**](hub.docker.com) is a cloud-based registry service which allows you to link to code repositories, build your images, test them, and store manually pushed images.
  - **Dockerfile** is a text document that contains all the commands a user could call on the command line to **assemble an image**. Using `docker build` users can create an automated build that executes several command-line instructions in succession.
- **Docker Compose** is a tool for defining and running multi-container Docker applications. With Compose, you use a YAML file to configure your application's services. Then, with a single command, you create and start all the services from your configuration.
- **Docker Daemon** is a background service running on the host that manages building, running, and distributing Docker containers. The daemon is the process that runs in the operating system to which clients talk to.
- **Docker Engine** is a client-server application with these major components:
  - A **server** which is a type of long-running program called a daemon process (the `dockerd` command).
  - **Docker Client** is the way you interact with Docker. The most common way is through the `docker` command. The client can run on the same host as the daemon or connect to a remote daemon.

- **Docker Swarm** is a clustering and scheduling tool for Docker containers. With Swarm, IT administrators and developers can establish and manage a cluster of Docker nodes as a single virtual system.

# Common Commands

Docker command line structure: `docker <command> <sub-command> (options)`

- `docker version`: show the docker version information
- `docker info`: display system-wide information
- `docker build <path>`: build an image from a Dockerfile
- `docker run <image name>`: run a container from an image
- `docker start <container name>`: start a stopped container
- `docker exec -it <container name> <command>`: execute a command in a running container
- `docker ps`: list running containers
  - `docker ps -a`: list all containers
- `docker images`: list all images
- `docker search <image name>`: search for an image in Docker Hub
- `docker pull <image name>`: pull an image from a registry
- `docker push <image name>`: push an image to a registry
  - `docker login`: log in to a registry
  - `docker logout`: log out from a registry

## Docker Commands Options
#### `run` 

- **Running** a container from an image. Technically, the client sends a request through the REST API to the Docker daemon, which carries out the instruction.
  - Each container has a unique ID and name. If you do not specify a name, Docker will generate a random one.
  
      ```bash
    docker container run <options> <image name>
    ```

      ```bash
      docker run <options> <image name>
      ```

  Some `<options>` are listed below; but more can be found `docker container run --help`:
  - `run -d`: Run a container in the **background**(detached mode)
  - `run -it`: Run a container **interactively**
  - `run -p <host port>:<container port>`: Map (expose) a container's port to a host port
  - `run --name <container name>`: Assign a **name** to the container
  - `run --rm`: Automatically **remove** the container when it exits
  - `run --env <key=value>`: Set an **environment variable**
  - `run --network <network name>`: Connect the container to a **network**
  - `run --volume <host path>:<container path>`: Mount a **volume** from the host to the container
  
#### `create`

- **Creating** a container from an image

    ```bash
    docker container create <options> <image name>
    ```

    Some `<options>` are listed below; but more can be found `docker container create --help`
    All previous options (in `run`) are applicable here.
  - `create --name <container name>`: Assign a **name** to the container
  - `create -interactive/-i`: Keep **STDIN** open even if not attached. Useful for interactive shells.
  - `create -tty/-t`: Allocate a **pseudo-TTY** Often used with -i for interactive shells.
  - `create --cpus <value>`: Limit the **CPU** usage of the container
  
#### `start` 

- **Starting** a container
  `start`

    ```bash
    docker container start <container name>
    ```

    Some `<options>` are listed below; but more can be found `docker container start --help`
  - `start -a`: Attach **STDOUT/STDERR** and forward signals
  - `start -i`: Attach **STDIN** to the container
  - `start -ai`: Attach **STDIN/STDOUT/STDERR** and forward signals (interactive mode)
  
#### `stop`

- **Stopping** a container
  `stop`

    ```bash
    docker container stop <container name>
    ```

    Some `<options>` are listed below; but more can be found `docker container stop --help`
  - `stop -t <seconds>`: Number of seconds to wait before stopping the container
  
#### `rm`

- **Removing** a container
  `rm`

    ```bash
    docker container rm <container name>
    ```

    Some `<options>` are listed below; but more can be found `docker container rm --help`
  - `rm -f`: Force the removal of a running container (uses SIGKILL)
    - It is the equivalent of `docker kill <container name>` and then `docker rm <container name>`
  - `rm -v`: Remove the volumes associated with the container
  
#### `exec`

- **Running** a command in a running container
  `exec`
  difference between `exec` and `run` is that `exec` is used to run a command in an existing container, while `run` is used to create a new container and run a command in it.

    ```bash
    docker container exec <options> <container name> <command>
    ```

    Some `<options>` are listed below; but more can be found `docker container exec --help`
  - `exec -d`: Detached mode: run command in the background
  - `exec -i`: Keep **STDIN** open even if not attached
  - `exec -t`: Allocate a **pseudo-TTY**
  - `exec -it`: interactive mode
  
#### `ls`

- **Listing** containers
  `ls`

    ```bash
    docker container ls
    ```

    Some `<options>` are listed below; but more can be found `docker container ls --help`
  - `ls -a`: List all containers (default shows just running)
  - `ls -q`: Only display numeric IDs
  - `ls -s`: Display total file sizes

#### `inspect`

- **Inspecting** a container
  `inspect`

    ```bash
    docker container inspect <container name>
    ```

    Some `<options>` are listed below; but more can be found `docker container inspect --help`
  - `inspect -f`: Format the output using the given Go template

#### `logs`

- **Displaying** logs of a container
  `logs`

    ```bash
    docker container logs <container name>
    ```

    Some `<options>` are listed below; but more can be found `docker container logs --help`
  - `logs -f`: Follow log output
  - `logs -t`: Show timestamps

#### `top`

- **Displaying** the running processes of a container
  `top`

    ```bash
    docker container top <container name>
    ```

    Some `<options>` are listed below; but more can be found `docker container top --help`
  - `top -o`: Sort by field
  - `top -H`: Display threads
  - `top -n`: Limit the number of processes displayed
  - `top -l`: Limit the number of lines displayed
  - `top -pid`: Display the processes with the given PID
  - `top -user`: Display the processes with the given username
  - `top -stats`: Display the processes with the given stats
  - `top -pid`: Display the processes with the given PID
- Display live performance data of a container
  `stats`

    ```bash
    docker container stats <container name>
    ```

    Some `<options>` are listed below; but more can be found `docker container stats --help`
  - `stats -a`: Display all containers (default shows just running)
  - `stats -no-stream`: Disable streaming stats and only pull the first result
  - `stats -format`: Format the output using the given Go template

## Experiment: create/run/delete a container

- **creating** and starting a new container from nginx image (locally in image cache or downloading from Docker Hub) on port 80
  `run --publish/-p`

    ```bash
    docker container run --publish 8080:80 nginx
    ```

  - changing the version of nginx image 
  `<image name>:<version>`

    ```bash
    docker container run --publish 8080:80 nginx:1.11 
    ```

  - running the container in the **background** (it will generate a container ID/name to access it) 
  `-detach/-d`

    ```bash
    docker container run --publish 8080:80 -detach nginx
    ```

  - creating the container using a **specified name **
  `--name <specified name>`

      ```bash
    docker container run --publish 8080:80 --name webhost nginx
    ```

  - **deleting** the container after exiting 
  `--rm`

    ```bash
    docker container run -p 80:80 --rm nginx
    ```

  - starting a shell in a container (**start** a new container **interactively**)
  `-it`

    ```bash
    # in here <command> is bash
    docker container run -it --name proxy nginx <command>

    # creating a ubuntu as a container
    docker container run -it --name ubuntu ubuntu
    ```

  - running additional command in **existing container**
  `exec -it`

    ```bash
    docker container exec -it --name db mysql bash 
    ```

- **Starting** a pre-created container [`start`]

    ```bash
    docker cotainer start <container name/id>
    ```

  - starting a shell in a pre-created container 
  `-ai`

        ```bash
        docker container start -ai <container name/id>
        ```

- **Checking**
  - Listing all running containers [`ls/ps`]

      ```bash
      docker container ls 
      docker ps
      ```

    - listing all created containers [including stopped ones](`ls -a`)

      ```bash
       docker container ls -a
       ```

  - Displaying logs of a container [`logs`]

      ```bash
      docker container logs <container name/id>
      ```

  - Displaying the running process of a container
  `top`

      ```bash
      docker container top <container name/id>
      ```

  - Displaying metadata about the container [startup, config, volumes, networking, etc] in JSON format
  `inspect`

      ```bash
      docker container inspect <container name/id>
      ```

  - Displaying live performance of containers
  `stats`

      ```bash
      docker container stat
      ```

- **Stopping** a container using its ID [the four first letters of a container ID would be sufficient]
  `stop`

    ```bash
    docker container stop <container ID> 
    ```

- **Removing** container(s) 
  `rm`

    ```bash
    docker container rm <container(s) id>
    ```

## Docker Networks

Dockers default network is `bridge`. You can create your own virtual networks.

- Each container connected to a private virtual network `bridge`.
- Each virtual network routes through NAT firewall on host IP.
- All containers on a virtual network can talk to each other without `-p`.
- Docker daemon has a built-in DN server that containers use by default.
- Docker defaults the hostname to the container's name, but you can also set aliases.

### Commands

- Displaying all container networks

    ```bash
    docker network ls
    ```

- Creating a virtual network to attach it to container[s](`create`)

    ```bash
    docker network create <network name>
    ```

- Connecting container(s) to a virtual network[`--network/connect`]
  - Creating a container and connecting it to a virtual network

    ```
    docker container run -d --name new_nginx --network <network name> nginx
    ```

  - Connecting an existing container to a virtual network

    ```
    docker network connect <network name/ID> <container name/ID>
    ```

  - Disconnecting an existing container from a virtual network

    ```
    docker network disconnect <network name/ID> <container name/ID>
    ```

- Finding an IP address of a created container using `inspect --format`

    ```
    docker container inspect --format '{{.NetworkSettings.IPAddress}}' <container name/id>
    ```

## Working with images

### Notes

- **Images** are application binaries and dependencies and metadata about the image data and how to run the image. Not a complete OS. No kernel, kernel modules(e.g. drivers)
- Images can have different version, which specifies with tags.
- Each image layer is uniquely identified and only stored once on a host.
- A container is just a single read/write layer on top of image.
-

## Docker Images

- Listing all available images:

  ```bash
  docker image ls
  ```

- Grabbing a specific image:

  ```bash
  docker pull <image name(repistory):tag(version)>
  # if you do not specify the version, it will pull the latest version.
  ```

- Displaying metadata of an image:

  ```bash
  docker image inspect <image name>
  ```

- Searching for an image in Docker Hub:

  ```bash
  docker search <image name>
  ```

- Displaying the history of an image:

  ```bash
  docker image history <image name>
  ```

- Changing a tag of an image:

  ```bash
  docker image tag <old> <new>
  ```

- Pushing a created image to docker hub:

  ```bash
  #first you should log in using: 
  docker login
  # push the image 
  docker image push <image name>
  #logout
  docker logout
  ```

- committing changes to an image:

  ```bash
  docker container commit <container name> <new image name>
  ```

### Docker File

Dockerfile is a text document that contains all the commands a user could call on the command line to assemble an image. Using `docker build` users can create an automated build that executes several command-line instructions in succession.

```bash
# syntax=docker/dockerfile:1
#start from a base image (usually a minimal Linux distribution)
FROM <image>:<tag>

#set environment variables (optional)
ENV <key>=<value>

#Specify the working directory. The CMD command will be executed in this directory
WORKDIR <path>

#copy files from the host to the container. If we use <.> as destination, it will copy to the working directory
COPY <source> <destination>

# Run a command in the container
RUN <install some dependencies>

#CMD is the command that is executed when the container is launched
CMD <command that is executed on `docker container run`>
```

  The docker file consists of different layers as below, which are executed by order.

  1) `From`: usually from a minimal Linux distribution like debain or (even better) alpine. For starting from empty container use `From scratch`
  2) `ENV`: very important of setting keys and values in containers.
  3) `WORKDIR`: setting the working directory in the container.
  4) `COPY`: copying the source codes from local to container images.
  5) `ADD`: copying the source codes from local to container images. The difference between `COPY` and `ADD` is that `ADD` can also extract tar files.
  6) `RUN`: the commands that start when a container is built.
  7) `RUN`: one `RUN` command is used for forwarding request and error logs to docker log collector.
  8) `EXPOSE`: expose the specified ports on the docker virtual network. In order to open/forward these ports on host, we require using `-p`.
  9) `CMD`: Run this command when the container is launched. Only one CMD allowed, so the last on among multiple ones will win.
  10) `WORKDIR`: it is the best practice when we want to change a directory rather than using `RUN cd <path>`
  11) `ENTRYPOINT`: it is used to configure a container that will run as an executable. It is used to configure the container to run as an executable.
  12) `VOLUME`: it is used to create a mount point with the specified name and mark it as holding externally mounted volumes from native host or other containers.

If any changes happen in docker file, it will not rerun the building process at first. It is using hash and built cache to check what are the changes.

```bash
docker image build -t <tag name> <directory>
```
