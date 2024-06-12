# Temperature Data Logger API

## Purpose

This python code using Flask framework was developed to generate a simple API for the [Temperature Data Logger](https://github.com/GustavoSantiago113/Soil_Temperature_Datalogger). It is capable of doing POST and GET requests to a MongoDB database previously configured.

## Instructions

First of all, create a branch of this repository to your GitHub account. Then, in your branch, modify the lines 12 ,13 and 14, inserting the MongoDB connection String, the Database and the Collection names.

As a tip, you can include a token in the endpoints to increase security and avoid a data input or pulling by accident.

Lastly, after initialize the instance or the remote server, pulling the repository to your system through git and installing Docker in the system, it is necessary to run the application in a container. To do this, navigate to the the repository folder in the system and run:

This will create the image:

`docker build . -t soiltemp:1.0`

Run this to check if the image was successfully created:

`docker images`

Lastly, run the following to run the container:

`docker run -d -p 80:5000 soiltemp:1.0`

In the previous command, the 80:5000 are the ports. The 80 is the port that has to be forwarded from the host and 5000 is the port which the container is running in the server. Port 5000 is the standard port for Flask applications and 80 is the standard port for http.

