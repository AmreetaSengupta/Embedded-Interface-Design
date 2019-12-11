## EMBEDDED INTERFACE DESIGN SUPER PROJECT : MAGIC WAND
                                           Authors   : Amreeta Sengupta and Ridhi Shah
                                           Professor : Bruce Montgomery 

### INSTALLATION INSTRUCTIONS
- Run the following commands in both the Raspberry Pis:
  - sudo apt-get update
  - sudo apt-get upgrade
  - sudo apt-get install python3-dev python3-pip
  
- To install boto3 package (which is the Amazon Web Services (AWS) Software Development Kit (SDK) for Python), use the following command:
  - pip3 install boto3
  
- QT which is a software library is also needed for GUI development and PyQT is needed, for developing QT software in linux using Python.
  Install these libraries using the following commands:
  - sudo apt-get install qt5-default pyqt5-dev pyqt5-dev-tools
  - sudo apt-get install qttools5-dev-tools
  
- For using the AWS Services (Lex, Polly, Rekognition, SQS) using boto3, use the following documentation:
  - https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html
  
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
  - The user needs to update the Login Details (i.e. username and password) in the code before running it

### PROJECT WORK
- Amreeta Sengupta : Responsible for Camera interface and Amazon Lex and SQS services.
- Ridhi Shah : Responsible for Microphone and speaker interface and Amazon Polly and Rekognition services.
