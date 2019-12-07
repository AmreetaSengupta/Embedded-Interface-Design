#*****************************************************************************************************************
# File Name: magic_wand_server.py
# Description: This code is used to load the GUI.
# Date: 11/18/2019
#******************************************************************************************************************

from PyQt5 import QtWidgets, uic
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
table_name = "MagicWand_EID"
table_name_label = "MagicWand_Label"

s3client.download_file('magic-wand','img1.jpg','./img1.jpg')

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
mycursor.execute("CREATE TABLE IF NOT EXISTS {} (id INT AUTO_INCREMENT PRIMARY KEY, Command VARCHAR(30))".format(table_name))

#CREATING A TABLE IN THE DATABASE
mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE IF NOT EXISTS {} (id INT AUTO_INCREMENT PRIMARY KEY, Label VARCHAR(30))".format(table_name_label))

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
a=int(num_msg)
print(a)

for i in range(a):
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
mycursor.execute("SELECT Command FROM MagicWand_EID")
myresult = mycursor.fetchall()

Img_corr_cnt = 0
total = 0

for x in myresult:
  print(x)
  if(x[0]=="Image correct"):
    Img_corr_cnt = Img_corr_cnt + 1
  #total = total+1

print(Img_corr_cnt)
print(a)

if(Img_corr_cnt != 0):
  percent_corr = (Img_corr_cnt/a)*100
  correct=str(percent_corr)
  print('Percentage of Correct Images is' + correct + '%') 

#######LABEL###############

response_label = sqs_client.get_queue_attributes(
    QueueUrl='https://sqs.us-east-1.amazonaws.com/229856064192/Superproject_Queue',
    AttributeNames=[
        'ApproximateNumberOfMessages',
    ]
)
num_msg_label=(response_label['Attributes']['ApproximateNumberOfMessages'])
b=int(num_msg_label)
print(b)

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
  
mycursor.execute("SELECT Label FROM {} ORDER BY ID DESC LIMIT 1".format(table_name_label))
for l in mycursor:
  print(l)
  last_label = l[0]

print(last_label)

#mycursor = mydb.cursor()
#mycursor.execute("SELECT Label FROM MagicWand_label")
#myresult_label = mycursor.fetchall()

#for y in myresult_label:
  #print(y)

#mycursor = mydb.cursor()
#res=mycursor.execute("SELECT Label FROM MagicWand_EID ORDER BY ID DESC LIMIT 1")
#print(res)


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
        self.show()
    
    def refresh(self):
        self.image_label.setText("{}".format("IMAGE LABEL NOT FOUND"))
        self.correct_image.setText("{}".format("0"))
        self.incorrect_image.setText("{}".format("0"))
        self.total_image.setText("{}".format("0"))
        self.correct_cmd.setText("{}".format("0"))
        self.incorrect_cmd.setText("{}".format("0"))
        self.total_cmd.setText("{}".format("0"))
        self.per_image.setText("{}".format("0"))
        self.per_cmd.setText("{}".format("0"))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = MainWindow();
    sys.exit(app.exec_())
