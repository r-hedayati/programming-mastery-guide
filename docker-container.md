## Notes
- **Containers** aren't Mini-VM's. However, they are **processes**.
- **Containers** are limited to what resources they can access.
- **Container** is an instance of that image running as a process. **Image** is the application we want to run
- Multiple **containers** can be run based on a single image.  
- Each **container** has a unique name and ID. 
## Basic commands
docker command line structure: `docker <command> <sub-command> (options)` 
  - `docker version`: verified CLI can talk to engine
 -  ` docker info`: most config values of engine


## Creating/Checking/Deleting a container
- **Creating** and starting a new container from nginx image (locally in image cache or downloading from Docker Hub) on port 80 [`run --publish/-p`]
    ```
    docker container run --publish 8080:80 nginx
    ```
  - changing the version of nginx image [`<image name>:<version>`]
    ```
    docker container run --publish 8080:80 nginx:1.11 
    ```
  - running the container in the background (it will generate a container ID/name to access it) [`-detach/-d`]
    ```
    docker container run --publish 8080:80 -detach nginx
    ```
  - creating the container using a specified name [`--name <specified name>`]
      ```
    docker container run --publish 8080:80 --name webhost nginx
    ```
  - Deleting the container after exiting [`--rm`]
    ```
    docker container run -p 80:80 --rm nginx
    ```
  - starting a shell in a container (start a new container interactivelly) [`it`]
    ```
    # in here command is bash
    docker container run -it --name proxy nginx <command>

    # creating a ubuntu as a container
    docker container run -it --name ubuntu ubuntu
    ```
  - running additional command in existing container[`exec -it`]
    ```
    docker container exec -it --name db mysql bash 
    ```
- **Starting** a pre-created container [`start`]
    ```
    docker cotainer start <container name/id>
    ```
    - starting a shell in a pre-created container [`ai`]
        ```
        docker container start -ai <container name/id>
        ```
- **Checking**
  - Listing all running containers [`ls/ps`]
      ```
      docker container ls 
      docker ps
      ```
      - listing all created containers (including stopped ones)[`ls -a`]
      ```
       docker container ls -a
       ```
  - Displaying logs of a container [`logs`]
      ```
      docker container logs <container name/id>
      ```
  - Displaying the running process of a container [`top`]
      ```
      docker container top <container name/id>
      ```
  - Displaying metadata about the container (startup, config, volumes, networking, etc)[`inspect`]
      ```
      docker container inspect <container name/id>
      ```
  - Displaying live performance of containers [`stat`]
      ```
      docker container stat
      ```
- **Stopping** a container using its ID (the four first letters of a container ID would be sufficient)[`stop`]
    ```
    docker container stop <container ID> 
    ```
- **Removing** container(s) [`rm`]
    ```
    docker container rm <container(s) id>
    ```
## Docker Networks
### Notes
- Each container connected to a private virtual network "bridge".
- Each virtual network routes through NAT firewall on host IP. 
- All containers on a virtual network can talk to each other without `-p`.
- Docker daemon has a built-in DN server that containers use by default.
- Docker defaults the hostname to the container's name, but you can also set aliases.

### Commands
- Displaying all container networks
    ```
    docker network ls
    ```
- Creating a virtual network to attach it to container(s)[`create`]
    ```
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

## Commands
- Listing all available images:
  ```
  docker image ls
  ```
- Grabbing a specific image:
  ```
  docker pull <image name(repistory):tag(version)>
  # if you do not specify the version, it will pull the latest version.
  ```
- Displaying metadata of an image:
  ```
  docker image inspect <image name>
  ```
- Displaying the history of an image: 
  ```
  docker image history <image name>
  ```
- Changing a tag of an image:
  ```
  docker image tag <old> <new>
  ```
- Pushing a created image to docker hub:
  ```
  #first you should log in using: 
  docker login
  # push the image 
  docker image push <image name>
  #logout
  docker logout
  ```
  ## Docker File
  The docker file consists of different layers as below, which are executed by order.
  1) `From`: usually from a minimal Linux distribution like debain or (even better) alpine. For starting from empty container use `From scratch`
  2) `ENV`: very important of setting keys and values in containers. 
  3) `RUN`: the commands that start when a container is built. 
  4) `RUN`: one `RUN` command is used for forwarding request and error logs to docker log collector.
  5) `EXPOSE`: expose the specified ports on the docker virtual network. In order to open/forward these ports on host, we require using `-p`.
  6) `CMD`: Run this command when the container is launched. Only one CMD allowed, so the last on among multiple ones will win.
  7) `WORKDIR`: it is the best practice when we want to change a directory rather than using `RUN cd <path>`
  8) `COPY`: using for copying the source codes from local to container images.

If any changes happen in docker file, it will not rerun the building process at first. It is using hash and built cache to check what are the changes. 
```
docker image build -t <tag name> <directory>
```