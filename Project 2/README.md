# EMBEDDED INTERFACE DESIGN PROJECT 2 : TEMPERATURE AND HUMIDITY CONTROLLER
                                                
                                           Authors   : Amreeta Sengupta and Ridhi Shah
                                           Professor : Bruce Montgomery 

## INSTALLATION INSTRUCTIONS
- Run the following commands in the Raspberry Pi:
  - sudo apt-get update
  - sudo apt-get upgrade
- Run the following commands to install nvm, node and npm:
  - curl -o- https://raw.githubusercontent.com/creationix/nvm/v0.34.0/install.sh | bash
  - Restart the terminal
  - nvm –version (Returns the version number)
  - nvm install node (Installs the latest node)
  - nvm install 10.16.3 (Installs the stable LTS 10.16.3 node)
  - node -v (Returns the version number)
  - npm –v (Returns the version of npm installed with node.js)
- Run the following command to setup MYSQL for node.js:
  -
- Run the following command to install DHT22 module in node.js:
  - npm install node-dht-sensor
- Clone the Repository to the Raspberry Pi (https://github.com/AmreetaSengupta/Embedded-Interface-Design.git)
- Go to the folder Project 2 and run the script by typing the following:

## PROJECT WORK
- Amreeta Sengupta: Responsible for sensor interfacing and storing the values in the database.
- Ridhi Shah: Responsible for design of GUI and linking it with the database.

## PROJECT ADDITIONS
- A button press changes the entire application from displaying any temperature data (in graphs or on the GUI) in degrees C to degrees F and back again. (Extra Credit)

## REFERNECES
- EID Lecture Files (Intro to NodeJS)
