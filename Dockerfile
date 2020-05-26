# Use Ubuntu 18.04 release
FROM ubuntu:18.04

# Add labels about the Docker Build
LABEL maintainer="Daniel Teycheney danielfjteycheney@gmail.com"
LABEL version="1.0.0"
LABEL description="This image contains the net-api \
REST interface for various network devices."

# Install pip3 and and python3
RUN apt-get update -y && \
    apt-get install -y python3-pip python3-dev openssh-server

# Copy the requirements to the work directory
COPY ./requirements.txt /app/requirements.txt

# Configure the WORKDIR directory
WORKDIR /app

# Install the requirements
RUN pip3 install -r requirements.txt

# Copy the app configuration into the /app folders
COPY app/. /app

# Run the equivalent of `python3 webapp.py` inside the image
ENTRYPOINT [ "python3" ]

CMD [ "webapp.py" ]