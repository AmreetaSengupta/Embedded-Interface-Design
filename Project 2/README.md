# EMBEDDED INTERFACE DESIGN PROJECT 1 : TEMPERATURE AND HUMIDITY CONTROLLER
                                                
                                           Authors   : Amreeta Sengupta and Ridhi Shah
                                           Professor : Bruce Montgomery 

## INSTALLATION INSTRUCTIONS
- Run the following commands in the Raspberry Pi:
  - sudo apt-get update
  - sudo apt-get upgrade
- Run the following commands to import Packages and Libraries of ADAFRUIT and Python in the Raspberry Pi from    https://pimylifeup.com/raspberry-pi-humidity-sensor-dht22/ which includes:
  - sudo apt-get install python3-dev python3-pip
  - sudo python3 -m pip install --upgrade pip setuptools wheel
  - sudo pip3 install Adafruit_DHT
- Use the following commands to set up MYSQL in Raspberry Pi from https://pimylifeup.com/raspberry-pi-mysql/ which includes:
  - sudo apt install mariadb-server
  - sudo mysql_secure_installation
  - Create a new a user and grant all privilidges to the database for that user using the instructions given in the link mentioned above.
  - Run "python3 -m pip install mysql-connector" to install MySQL Connector
  - The user needs to update the Login Details (i.e. username and password) in the code before running it.
 - Use the following command to install Matplotlib library for python to plot graphs:
   - python3 -m pip install -U pip
   - python3 -m pip install -U matplotlib
 - Use the following command to install multitimer module:
   - sudo pip3 install multitimer
- Clone the Repository to the Raspberry Pi (https://github.com/AmreetaSengupta/Embedded-Interface-Design.git)
- Go to the folder Project 1 and run the script by typing the following:
  - python3 sensor_reading_gui.py 
- A GUI will open which will allow the user to view and control the Temperature and Humidity Settings

## PROJECT WORK
- Amreeta Sengupta: Responsible for sensor interfacing and storing the values in the database.
- Ridhi Shah: Responsible for design of GUI and linking it with the database.

## PROJECT ADDITIONS
- A button press changes the entire application from displaying any temperature data (in graphs or on the GUI) in degrees C to degrees F and back again. (Extra Credit)


