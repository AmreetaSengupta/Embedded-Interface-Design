# EMBEDDED INTERFACE DESIGN PROJECT 2 : SERVER CLIENT WEBSOCKET COMMUNICATION
                                                
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
- Run the following commands to install nvm, node and npm:
  - curl -o- https://raw.githubusercontent.com/creationix/nvm/v0.34.0/install.sh | bash
  - Restart the terminal
  - nvm –version (Returns the version number)
  - nvm install node (Installs the latest node)
  - nvm install 10.16.3 (Installs the stable LTS 10.16.3 node)
  - node -v (Returns the version number)
  - npm –v (Returns the version of npm installed with node.js)
- Run the following command to install Tornado module:
  - pip3 install tornado
- Clone the Repository to the Raspberry Pi (https://github.com/AmreetaSengupta/Embedded-Interface-Design.git)
- Go to the folder Project 2 and run the script  by typing the following:
  - ./eid_script.sh

## PROJECT WORK
- Amreeta Sengupta: Responsible for Establishing the connection between Node.js server and the HTML Client and intergration of both.
- Ridhi Shah: Responsible for Establishing the connection between Tornado server and the HTML Client and intergration of both.

## PROJECT ADDITIONS
- A Graph for last 10 values of temperature and Humidity is displayed on Button press fro both
- Following Error Conditions were taken care of :
  - Error message is displayed when the DHT22 sensor is disconnected.
  - Error message is displayed on the HTML webpage when the Node.js server is disconnected.
  - Error message is disaplyed on the HTML webpage when the Tornado server is disconnected.


## REFERNECES
- EID Lecture Files (Intro to NodeJS)
- https://html.com/tags/comment-tag/
- https://canvasjs.com/html5-javascript-line-chart/
- https://www.w3schools.com/
- https://stackoverflow.com/
- http://www.tornadoweb.org/en/stable/
- https://www.pubnub.com/blog/nodejs-websocket-programmingexamples/
- https://os.mbed.com/cookbook/Websockets-Server
