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
- Run the following to install AWS SDK
  - git clone https://github.com/aws/aws-iot-device-sdk-python
  - cd aws-iot-device-sdk-python
  - sudo python setup.py install
- Follow the steps in the link: https://docs.aws.amazon.com/iot/latest/developerguide/iot-gs.html to set up AWS account and to create     resources required to send, receive, and process MQTT messages from devices using AWS IoT 
- Refer the link: https://docs.aws.amazon.com/iot/latest/developerguide/config-and-test-rules.html to create and configure a rule to       send the data received from a device to an Amazon SNS topic
- Refer the link: https://docs.aws.amazon.com/iot/latest/developerguide/iot-lambda-rule.html to create a Lambda function that publishes   a message to the Amazon SNS topic created and to create a Lambda rule that calls the Lambda function, passing in some data from the     MQTT message that triggered the rule.
- Follow the steps in the link: https://docs.aws.amazon.com/sdk-for-javascript/v2/developer-guide/getting-started-browser.html to gain     access to AWS services from a browser script using Amazon Cognito Identity.
- Refer the link: https://startupnextdoor.com/adding-to-sqs-queue-using-aws-lambda-and-a-serverless-api-endpoint/ for adding data to an   SQS queue using AWS lambda
- Clone the Repository to the Raspberry Pi (https://github.com/AmreetaSengupta/Embedded-Interface-Design.git)
- Go to the folder Project 3 and run the following:
  - python3 sensor_reading_gui.py
  - Run the client by clicking on test.html
 

## PROJECT WORK
- Amreeta Sengupta: Responsible for Cost estimation between google and AWS, setting up MQTT, SQS and creting lambda function for passing   data 
- Ridhi Shah: Responsible for setting up communication via SNS and integration of SQS with HTML client

## PROJECT ADDITIONS
- Following Error Conditions were taken care of :
  - An alert message is sent via E-mail when the DHT22 sensor is disconnected.
  - A button is added which on pressing displays the number of messages in the queue
 


## REFERNECES
- EID Lecture Files (Intro to NodeJS)
- https://html.com/tags/comment-tag/
- https://canvasjs.com/html5-javascript-line-chart/
- https://www.w3schools.com/
- https://stackoverflow.com/
- http://www.tornadoweb.org/en/stable/
- https://www.pubnub.com/blog/nodejs-websocket-programmingexamples/
- https://os.mbed.com/cookbook/Websockets-Server
- https://docs.aws.amazon.com/code-samples/latest/catalog/javascript-sqs-sqs_receivemessage.js.html
- https://techblog.calvinboey.com/raspberrypi-aws-iot-python/
