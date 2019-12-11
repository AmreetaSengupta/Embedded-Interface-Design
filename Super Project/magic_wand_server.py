#*****************************************************************
# File Name: magic_wand_server.py
# Description: This code is used to load the GUI.
# Date: 11/18/2019
# Author: Amreeta Sengupta and Ridhi Shah
#*****************************************************************

from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QLabel, QApplication, QMainWindow
from PyQt5.QtGui import QPixmap
from PyQt5 import Qt
import sys
import boto3
import os
import sys
import subprocess
import wave
from contextlib import closing
from tempfile import gettempdir
from botocore.exceptions import BotoCoreError, ClientError
import mysql.connector

s3 = boto3.resource('s3')
s3client = boto3.client('s3')
sqs_client = boto3.client('sqs')
host_name = "localhost"
user_name = "eid19"
passwd_name = "eid19"
database_name = "EID"
table_name = "MagicWand_eid"
table_name_label = "MagicWand_Label"

mydb = mysql.connector.connect(
  host=host_name,
  user=user_name,
  passwd=passwd_name
)

#CREATING A DATABASE
mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE IF NOT EXISTS {}".format(database_name))
for(dbname,) in mycursor:
        print(dbname)


#TO ESTABLISH A CONNECTION TO THE MYSQL SERVER
mydb = mysql.connector.connect(
  host=host_name,
  user=user_name,
  passwd=passwd_name,
  database=database_name
)

#CREATING A TABLE IN THE DATABASE
mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE IF NOT EXISTS {} (id INT AUTO_INCREMENT PRIMARY KEY, Command VARCHAR(150))".format(table_name))

#CREATING A TABLE IN THE DATABASE
mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE IF NOT EXISTS {} (id INT AUTO_INCREMENT PRIMARY KEY, Label VARCHAR(150))".format(table_name_label))

#DELETING ALL ROWS OF THE TABLE
mycursor = mydb.cursor()
mycursor.execute("DELETE FROM {} ".format(table_name))

#DELETING ALL ROWS OF THE TABLE
mycursor = mydb.cursor()
mycursor.execute("DELETE FROM {} ".format(table_name_label))

########### COMMAND ##############
response = sqs_client.get_queue_attributes(
    QueueUrl='https://sqs.us-east-1.amazonaws.com/229856064192/SuperProject_Cmd',
    AttributeNames=[
        'ApproximateNumberOfMessages',
    ]
)
num_msg=(response['Attributes']['ApproximateNumberOfMessages'])
total_num_msg=int(num_msg)
print("Total number of commands = {}".format(total_num_msg))

for i in range(total_num_msg):
        q_msg = sqs_client.receive_message(
            QueueUrl='https://sqs.us-east-1.amazonaws.com/229856064192/SuperProject_Cmd',
            MaxNumberOfMessages = 1
        )
        db_msg=q_msg['Messages'][0]['Body']
        mycursor.execute("INSERT INTO {} (Command) VALUES ('{}')".format(table_name, db_msg))
        mydb.commit()
        rec_handle = q_msg['Messages'][0]['ReceiptHandle']     
        del_msg = sqs_client.delete_message(
                        QueueUrl='https://sqs.us-east-1.amazonaws.com/229856064192/SuperProject_Cmd',
                        ReceiptHandle=rec_handle
                        )
         
  

#TO VIEW THE CONTENTS OF THE TABLE
mycursor.execute("SELECT * FROM {}".format(table_name))
for i in mycursor:
  print(i)
  
mycursor = mydb.cursor()
mycursor.execute("SELECT Command FROM MagicWand_eid")
myresult = mycursor.fetchall()

Img_corr_cnt = 0
total_cnt = 0
img_wrong = 0
incorrect = 0
correct = 0
correct_try = 0
per = 0

print(myresult);

for x in myresult:
  if(x[0]=="Image correct"):
    Img_corr_cnt = Img_corr_cnt + 1

print("Number of Correct Images are {}".format(Img_corr_cnt))

for y in myresult:
  if(y[0]=="Image Identified"):
    total_cnt = total_cnt + 1
 
print("Total Images are {}".format(total_cnt))

for c in myresult:
  if(c[0]=="wrongo"):
    img_wrong = img_wrong + 1

print("Number of Incorrect Images are {}" .format(img_wrong))

if(total_cnt != 0):
  percent_corr = (Img_corr_cnt/total_cnt)*100
  correct=str(percent_corr)
  print('Percentage of Correct Images is ' + correct + '%') 
else:
  print('No Images!');

print("Total Images are {}".format(total_cnt))    

for z in myresult:
  if(z[0]=="Sorry, can you please repeat that?" or z[0]=="Sorry, I could not understand. Goodbye."):
    incorrect = incorrect + 1
    
print("Number of Incorrect Voice Commands are {}".format(incorrect))  

correct_try = total_num_msg - incorrect

print("Number of Correct Voice Commands are {}".format(correct_try))  

if(total_num_msg != 0):
  per = (correct_try/total_num_msg)*100
  print("Percentage of Correct Voice Commands are {}".format(per))  
else:
  print('No Commands!');    
  
#######LABEL###############
response_label = sqs_client.get_queue_attributes(
    QueueUrl='https://sqs.us-east-1.amazonaws.com/229856064192/Superproject_Queue',
    AttributeNames=[
        'ApproximateNumberOfMessages',
    ]
)
num_msg_label=(response_label['Attributes']['ApproximateNumberOfMessages'])
b=int(num_msg_label)
print("Total number of messages in Label Queue are {}".format(b))

for i in range(b):
        q_msg_label = sqs_client.receive_message(
            QueueUrl='https://sqs.us-east-1.amazonaws.com/229856064192/Superproject_Queue',
            MaxNumberOfMessages = 1
        )
        db_msg_label=q_msg_label['Messages'][0]['Body']
        mycursor.execute("INSERT INTO {} (Label) VALUES ('{}')".format(table_name_label, db_msg_label))
        mydb.commit()
        rec_handle_label = q_msg_label['Messages'][0]['ReceiptHandle']     
        del_msg_label = sqs_client.delete_message(
                        QueueUrl='https://sqs.us-east-1.amazonaws.com/229856064192/Superproject_Queue',
                        ReceiptHandle=rec_handle_label
                        )
  
#TO VIEW THE CONTENTS OF THE TABLE
mycursor.execute("SELECT * FROM {}".format(table_name_label))
for k in mycursor:
  print(k)

#TO GET THE IMAGE LABEL 
if(b != 0):
  s3client.download_file('magic-wand','img1.jpg','./img1.jpg')
  mycursor.execute("SELECT Label FROM {} ORDER BY ID DESC LIMIT 1".format(table_name_label))
  for l in mycursor:
    print(l)
    last_label = l[0]
  print(last_label)
else:
  os.system('rm img1.jpg');
  last_label = "Image Label Not Found"
  
class MainWindow(QtWidgets.QMainWindow):
    
    def __init__(self):
        super(MainWindow, self).__init__() 
        uic.loadUi('magic_wand.ui', self) #ui file loaded
        self.refresh_button = self.findChild(QtWidgets.QPushButton, 'refresh_button') 
        self.refresh_button.clicked.connect(self.refresh)
        self.image_label = self.findChild(QtWidgets.QLabel, 'image_label')
        self.correct_image = self.findChild(QtWidgets.QLabel, 'correct_image')
        self.incorrect_image = self.findChild(QtWidgets.QLabel, 'incorrect_image')
        self.total_image = self.findChild(QtWidgets.QLabel, 'total_image')
        self.correct_cmd = self.findChild(QtWidgets.QLabel, 'correct_cmd')
        self.incorrect_cmd = self.findChild(QtWidgets.QLabel, 'incorrect_cmd')
        self.total_cmd = self.findChild(QtWidgets.QLabel, 'total_cmd')
        self.per_image = self.findChild(QtWidgets.QLabel, 'per_image')
        self.per_cmd = self.findChild(QtWidgets.QLabel, 'per_cmd')
        self.image = self.findChild(QtWidgets.QLabel, 'Image')
        self.show()
    
    def refresh(self):
        self.image_label.setText("{}".format(last_label))
        self.correct_image.setText("{}".format(Img_corr_cnt))
        self.incorrect_image.setText("{}".format(img_wrong))
        self.total_image.setText("{}".format(total_cnt))
        self.correct_cmd.setText("{}".format(correct_try))
        self.incorrect_cmd.setText("{}".format(incorrect))
        self.total_cmd.setText("{}".format(total_num_msg))
        self.per_image.setText("{}".format(correct))
        self.per_cmd.setText("{}".format(per))
        self.image.setPixmap(QPixmap('img1.jpg'))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = MainWindow();
    sys.exit(app.exec_())
