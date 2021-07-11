# First project

Create Docker and docker-compose files to run a Python application (simple hello world) inside a container on a dedicated AWS server.

Here is an example of the result.

![result](https://github.com/SergeiSd/data-engineering-course/blob/main/Project_1/images/result.png)


### Running a dedicated server on AWS EC2 platform based on Linux.


| Parameter                  |                         |
| ---------------------------|:-----------------------:|
| Amazon Machine Image       | Ubuntu Server 20.04 LTS |
| Instance Type              | t2.micro                | 
| Configure Instance Details | default                 |
| Add Storage                | default                 |
| Add Tags                   | default                 |
| Configure Security Group   | default                 |


### Transferring `Dockerfile`, `docker-compose.yml` and `app.py` files to a dedicated server.

    # your_pairkey.pem is a key pair for connecting to an EC2 instance
    # your_IPv4 is public IPv4 DNS (Ex. ec1-2-34-56-789.eu-central-1.compute.amazonaws.com)
    # your_directory is created directory on a dedicated AWS EC2 server
    
    scp -r -i your_pairkey.pem Dockerfile docker-compose.yml app.py your_IPv4:your_directory


### Connect to instance EC2
        
        # your_pairkey.pem is a key pair for connecting to an EC2 instance
        # your_IPv4 is public IPv4 DNS (Ex. ec1-2-34-56-789.eu-central-1.compute.amazonaws.com)
        
        ssh -i "your_pairkey.pem"  your_IPv4
