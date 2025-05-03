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

