# AI Ganpati 

## Contents

- [Introduction](#introduction)
- [Repository contents](#repository-contents)
- [Flow Diagram](#block-diagram)
- [What goes in?](#input)
- [What comes out?](#output)
- [Dependencies](#dependencies)
- [For Embedded Linux platforms](#for-embedded-linux-platforms)
- [Docker Image](#docker-image)
***

### Introduction

- This repository contains a fun application made on python3 intended to dispense sweets to individuals based on their choice.

- Before running the codes, we need to install all the prerequisites. 

- Have made a requirements.txt for the same. 

- Use ``` pip3 install -r requirements.txt ``` to install prerequisites.

- Can be executed on x86 and ARM architecture systems.

- Have also created a Dockerfile and docker image for the application. 
***


## Repository contents

1. requirements.txt - contains all the prerequisites required for the functioning of the application.

2. models - conatins trained models required for face inference.
	>  **Note: The voice model has been pre-trained using several voice samples.**

3. utils - contains the all dependencies that the main codes require.

4. words - contains the voice input given by user which will be used to get the label.

5. scripts - contains script files to perform various actions using Arduino GPIO pins. 

6. arduino-codes - codes for some action to be performed. 

7. Dockerfile - dockerfile for the application 
***

### Block Diagram

![Block Diagram](https://github.com/darpan-jain/ai-gan-master/blob/master/overview.png)
***

### Input

 - Run `python3 input.py` for face input and then voice input for choice of sweet (laddu/modak/pedha).

 - LEDs can be used to display the status to a user. (see ./Scripts)

 - The code uses the MTCNN model for Face detection.

 - Face alignment is done using dlib.

 - FaceNet is used for converting the various features of a person's face into 128D embeddings.
 
 ***

### Output

 - Run `python3 recognition.py `

 - When a face is detected, the system verifies if the person exists in the database.

 - On recognition, the corresponding label is displayed.

 - The robotic arm dispenses the sweet as per the registered person's choice.
 
- Both the codes (input.py and recognition.py) can be executed simultaneously. 
***

### Dependencies

All the required dependencies can be install by running the command `pip install -r requirements.txt`
***

### For Embedded Linux Platforms

- Connect 2 USB/CSI cameras (as per availability) and a mic for voice input
- Install drivers if required using ```insmod [driver location]```
- Check the device IDs for the connected peripherals in ```/proc/asound/```
- Make changes in .asoundrc accordingly.
***

### Docker Image

- Install docker using ```sudo apt-get install docker.io``` and assign sudo permission to it.

- You can find the readymade image that I've already built using ``` docker pull darpanjain/ai-input ```

- Visit [My DockerHub Profile](https://hub.docker.com/u/darpanjain/ "DockerHub Profile darpan-jain")

- Run the image using ``` docker run -it --rm ai-input ```

- You can use the provided Dockerfile to build your own image.

> 1. Clone the repo to your system
> 2. Build your image using ``` sudo  docker build -t application:v1 . ```
***

**_Any contributions to the project are welcome :)_**
