# Introduction

net-api is a documented REST API which returns structured data from network devices. This application is a mix of technologies and techniques and has been developed to
highlight what is possible with multiple open source projects.

## net-api Overview

The overview of net-api is shown in the diagram below:

![Overview](diagrams/net-api-overview.jpg)

As shown in the diagram, net-api handles device authentication, data transformation and transport from network devices and presents the consumer of the application with a fully documented API. This approach has multiple benefits to name a few:

- Provide non-network operators access to **configuration and state about the network, without the ability to make direct changes to devices**.
- Provide a reliable, structured API to query, which can be leveraged from third-party systems or custom applications.
- Provide a framework which is extensible and portable to deploy in most environments. Additional operations or API calls can be developed with minimal effort.


## Supported Environments

This application is only supported on:
 - Python 3.6 or greater
 - Linux/unix machines only

## Installation/Operating Instructions

There are two methods for installing or operating net-api; using a Python virtual environment or a Docker container. The instructions
for each method are described below.

### Python 3.X Installation and Operation

The most popular way of running this application is using it in a standard Python environment. To do so, please follow the options below:

1) Clone the repository to the machine on which you will run the application from:

```git
git clone https://github.com/writememe/net-api.git
cd net-api
```

2) Populate your Nornir inventory files:

    - [defaults.yaml](app/inventory/defaults.yaml)
    - [groups.yaml](app/inventory/groups.yaml)
    - [hosts.yaml](app/inventory/hosts.yaml)

Refer to the [Nornir Inventory Documentation](https://nornir.readthedocs.io/en/latest/tutorials/intro/inventory.html) if you have not used Nornir before
or follow the examples provided in this repository.

3) Create the virtual environment to run the application in and install the requirements. For your convenience, this can be completed by performing the following:

```console
make venv
```

4) Set two environmental variables, which are used by the application as the default credentials to login to devices:

```bash
export NORNIR_DEFAULT_USERNAME=<someusername>
export NORNIR_DEFAULT_PASSWORD=<somepassword>
```
5) Validate these environmental variables by entering the following command:

```
env | grep NORNIR
```
You should see the two environment variables set.

6) Setup an environmental variable to point to the NTC templates directory for TextFSM functionality.

In the example below, the virtual environment is using `python3.6`. You will need to adjust this if using anything else:

```bash
export NET_TEXTFSM=$VIRTUAL_ENV/lib/python3.6/site-packages/ntc_templates/templates
```

7) Validate these environmental variables by entering the following command:

```
env | grep NET_TEXTFSM
```
You should see th environment variable set.

8) Change to the `app/` directory, then start the flask application:

```python3
cd app
python webapp.py
```

9) The application will now be running on TCP/5000. For example, if the client IP is 10.0.0.1, the application will be available on http://10.0.0.1:5000

### Docker Installation and Operation

There is an option to build this application in a Docker image and run it as a container. To do so, please follow the options below:

1) Clone the repository to the machine on which you will run the Docker container from:

```git
git clone https://github.com/writememe/net-api.git
cd net-api
```

2) Populate your Nornir inventory files:

- [defaults.yaml](app/inventory/defaults.yaml)
- [groups.yaml](app/inventory/groups.yaml)
- [hosts.yaml](app/inventory/hosts.yaml)

Refer to the [Nornir Inventory Documentation](https://nornir.readthedocs.io/en/latest/tutorials/intro/inventory.html) if you have not used Nornir before
or follow the examples provided in this repository.

    
2) Build the Docker image, whereby `net-api` is the name of the image and `latest` is an arbitary docker tag:

```dockerfile
docker build -t net-api:latest .
```

3) Create a file of environmental variables, to be passed into the Docker image as it's starting up.  
   In the below example, the file `.env-vars` contains three environmental variables:
    - `NORNIR_DEFAULT_USERNAME` - Used by the application as the default username to login to devices in the Nornir inventory.
    - `NORNIR_DEFAULT_PASSWORD` - Used by the application as the default username to login to devices in the Nornir inventory.
    - `NET_TEXTFSM`- Used to point to the NTC templates directory for TextFSM functionality
   
```bash
.env-vars	
NORNIR_DEFAULT_USERNAME=<someadmin>
NORNIR_DEFAULT_PASSWORD=<somepassword>
# Change the `python3.6` to the version you are using in your environment.
NET_TEXTFSM=$VIRTUAL_ENV/lib/python3.6/dist-packages/ntc_templates/templates
```

4) Run the docker build, passing in the environment variables in Step 3. This will expose the build on port 5000:

```dockerfile
docker run -d --env-file=.env-vars -p 5000:5000 net-api:latest
```

5) Verify that the container is up and operational, by running `docker ps`:

```dockerfile
$ docker ps
CONTAINER ID        IMAGE               COMMAND               CREATED             STATUS              PORTS                    NAMES
fe8c0b858f18        net-api:latest      "python3 webapp.py"   21 minutes ago      Up 21 minutes       0.0.0.0:5000->5000/tcp   quizzical_rosalind
$
```

6) The application will now be running on TCP/5000. For example, if the client IP is 10.0.0.1, the application will be available on http://10.0.0.1:5000