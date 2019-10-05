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
  - Use the following command to Log into MariaDB 
    - sudo mysql -u root -p
  - Create the database that the project will use using the following command: 
    - CREATE DATABASE DB_NAME;
  - Then create a username and password which the program will use with the help of the following command:
    - CREATE USER 'USERNAME'@'localhost' IDENTIFIED BY 'PASSWORD';
  - Grant all the privileges that the user will need with this command: 
    - GRANT ALL PRIVILEGES ON DB_NAME.* TO 'USERNAME'@'localhost';
  - Flush the privileges table, allowing the changes made in the previous step to take effect suing the following command: 
     - FLUSH PRIVILEGES;
  - Use Ctrl+C to exit MariaDB
  - Run "python3 -m pip install mysql-connector" to install MySQL Connector
  - The user needs to update the Login Details (i.e. username and password) in the code before running it.
- QT which is a software library is also needed for GUI development and PyQT is needed, for developing QT software in linux using Python.
  Install these libraries using the following commands:
  - sudo apt-get install qt5-default pyqt5-dev pyqt5-dev-tools
  - sudo apt-get install qttools5-dev-tools
  
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


