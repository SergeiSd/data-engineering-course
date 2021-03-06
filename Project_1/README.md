# First project

Create Docker and docker-compose files to run a Python application (simple hello world) inside a container on a dedicated AWS server.

Here is an example of the result.

![result](https://github.com/SergeiSd/data-engineering-course/blob/main/Project_1/images/result.png)

---

### Prerequisites

![](https://img.shields.io/badge/Docker-19.03.8-inactivegreen) ![](https://img.shields.io/badge/docker--compose-1.25.0-inactivegreen)

---

### Running a dedicated server on AWS EC2 platform based on Linux.

Parameters for launch instance.

| Parameter                  |                         |
| ---------------------------|:-----------------------:|
| Amazon Machine Image       | Ubuntu Server 20.04 LTS |
| Instance Type              | t2.micro                | 
| Configure Instance Details | default                 |
| Add Storage                | default                 |
| Add Tags                   | default                 |
| Configure Security Group   | default                 |

---

### Transferring `Dockerfile`, `docker-compose.yml` and `app.py` files to a dedicated server.

    # your_pairkey.pem is a key pair for connecting to an EC2 instance
    # your_IPv4 is public IPv4 DNS (Ex. ec1-2-34-56-789.eu-central-1.compute.amazonaws.com)
    # your_directory is created directory on a dedicated AWS EC2 server
    
    scp -r -i your_pairkey.pem Dockerfile docker-compose.yml app.py your_IPv4:your_directory

---

### Connect to instance EC2
        
    # your_pairkey.pem is a key pair for connecting to an EC2 instance
    # your_IPv4 is public IPv4 DNS (Ex. ec1-2-34-56-789.eu-central-1.compute.amazonaws.com)
        
    ssh -i "your_pairkey.pem"  your_IPv4

---    
    
### Build and run with Compose

Run Python application inside container on dedicated server.

    # From your project directory
    sudo docker-compose up

---

### Installing

Just git clone this repo and you are good to go.
    
    # sudo apt-get install subversion
    svn export https://github.com/SergeiSd/data-engineering-course/trunk/Project_1
