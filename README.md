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
 - Use the following command to install Matplotlib to plot graphs:
   - python -m pip install -U pip
   - python -m pip install -U matplotlib
- Clone the Repository to the Raspberry Pi (https://github.com/AmreetaSengupta/Embedded-Interface-Design.git)
- Go to the folder Project 1 and run the script by typing the following:
  - python3 sensor_reading_gui.py 
- A GUI will open which will allow the user to view and control the Temperature and Humidity Settings

## PROJECT WORK
- Amreeta Sengupta: Responsible for sensor interfacing and storing the values in the database.
- Ridhi Shah: Responsible for design of GUI and linking it with the database.

## PROJECT ADDITIONS
- A button press changes the entire application from displaying any temperature data (in graphs or on the GUI) in degrees C to degrees F and back again. (extra credit)




