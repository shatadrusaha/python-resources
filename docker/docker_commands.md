## Docker Commands


### Download a docker image.
- using _'image name'_.
    ```bash
    # downloads image with 'latest' tag.
    docker pull <image_name>
    ```

- using _'image name'_ and _'tag'_.
    ```bash
    docker pull <image_name>:<tag>
    ```


### Run a docker image.
_N.B. : If the image is NOT available 'locally', docker will first 'download' the image from 'docker hub' and then 'run' it._
- using _'image name'_.
    ```bash
    # runs image with 'latest' tag.
    docker run <image_name>

    # run in 'detached' mode (background).
    docker run -d <image_name>
    ```

- using _'image name'_ and _'tag'_.
    ```bash
    docker run <image_name>:<tag>
    ```


### List docker containers.
- running docker containers.
    ```bash
    docker ps
    ```

- all docker containers, _running and exited_.
    ```bas
    docker ps -a
    ```


### Stop docker container.
- using _'container ID'_.
    ```bash
    docker stop <container_id>
    ```

- using _'container name'_.
    ```bash
    docker stop <container_name>
    ```


### Remove docker container(s).
- using _'container ID'_.
    ```bash
    # single container
    docker rm <container_id>

    # multiple containers
    docker rm <container_id_01> <container_id_02> <container_id_03> <container_id_04>
    ```
    _N.B. : You don't have to provide the complete container_id. First few letters of container_id will also work._ 

- using _'container name'_.
    ```bash
    # single container
    docker rm <container_name>

    # multiple containers
    docker rm <container_name_01> <container_name_02> <container_name_03> <container_name_04>
    ```


### List docker images.
```bash
docker images
```


### Remove docker image(s).
_N.B. : Before removing an image, make sure there is no active container(s) running or any exited container using that image. STOP and/or REMOVE the container(s) first and then remove the image._

- Image(s) that has(have) _'latest'_ tag(s).
    ```bash
    # single image
    docker rmi <image_name>

    # multiple images
    docker rmi <image_name_01> <image_name_02> <image_name_03> <image_name_04>
    ```

- Image(s) with _'specific'_ tag(s), other than _'latest_.
    ```bash
    # single image
    docker rmi <image_name>:<tag>

    # multiple images
    docker rmi <image_name_01>:<tag>  <image_name_02>:<tag>
    ```


### Attach and detach from a container.
[link](https://www.howtogeek.com/devops/how-to-detach-from-a-docker-container-without-stopping-it/)
```bash
# run and attach to a container.
docker run <image_name>
docker attach <container_name or container_id>

# run a container in detached mode.
docker run -d <image_name>

# exit a running container.
CTRL + C
# for some reason you have to do it 3 times, to exit.

# detach from a running container, NOT EXIT.
CTRL + P CTRL + C
# for some reason you have to do it 3 times, to detach.
```


### Advanced _'run'_ commands.

- #### Append a command.
    ```bash
    # runs a docker container from the docker image 'ubuntu', 'sleeps' for 1000 seconds and then 'exits'.
    # docker run ubuntu <command>
    docker run ubuntu sleep 1000

    # detached mode
    docker run -d ubuntu sleep 1000

    # interactive mode ONLY.
    docker run -i ubuntu
    ls # will list the files and/or folders in the container.

    # interactive terminal mode.
    docker run -it ubuntu bash
    ```

- #### Port mapping.
    ```bash
    # docker run -p <port_host>:<port_container> <image_name>
    docker run -p 80:5000 kodekloud/simple-webapp

    # multiple image containers and/or multiple container instances of same image.
    docker run -p 8000:5000 kodekloud/simple-webapp
    docker run -p 8080:5000 kodekloud/simple-webapp
    docker run -p 9000:5000 kodekloud/simple-webapp

    docker run -p 3306:3306 mysql
    docker run -p 8306:3306 mysql
    ```

- #### Volume mapping.
    ```bash
    # docker run -v <path_docker_host>:<path_container> <image_name>
    docker run -v /opt/datadir:/var/lib/mysql mysql

    # saves the jenkins data and can be reused, when spinning a new container.
    # https://github.com/jenkinsci/docker/blob/master/README.md
    docker run -p 8080:8080 -v /root/my-jenkins-data:/var/jenkins_home -u root jenkins/jenkins
    ```


### Advanced 'container' commands.

- #### Execute a command, on a running docker container.
    ```bash
    # see contents of a file.
    docker exec <container_name or container_id> cat /etc/hosts
    docker exec <container_name or container_id> cat /etc/*release*

    # run the bash/shell.
    docker exec -it <container_name or container_id> bash
    # type 'exit' to exit from the container terminal.
    ```

- #### Inspect.
    ```bash
    docker inspect <containe_name or container_id> # json output

    ```

- #### Logs.
    ```bash
    docker logs <containe_name or container_id>
    ```




