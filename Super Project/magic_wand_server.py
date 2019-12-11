#****************************************************************************************************************
# File Name: magic_wand_server.py
# Description: This code is used receive data from AWS SQS and store it in SQL database and load the GUI.
# Date: 12/11/2019
# References: https://www.w3schools.com/python/python_mysql_getstarted.asp
#             https://docs.aws.amazon.com/code-samples/latest/catalog/code-catalog-python-example_code-sqs.html
#****************************************************************************************************************

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

__author__ = "Amreeta Sengupta, Ridhi Shah"
__copyright__ = "Copyright (C) 2019 by Amreeta Sengupta and Ridhi Shah"

s3 = boto3.resource('s3')
s3client = boto3.client('s3')
sqs_client = boto3.client('sqs')
host_name = "localhost"
user_name = "eid19"
passwd_name = "eid19"
database_name = "EID"
table_name = "MagicWand_eid"
table_name_label = "MagicWand_Label"


Img_corr_cnt = 0
total_cnt = 0
img_wrong = 0
incorrect = 0
correct = 0
correct_try = 0
per = 0
last_label = " "
b = 0
total_num_msg = 0
a = 0

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

'''
#DELETING ALL ROWS OF THE TABLE
mycursor = mydb.cursor()
mycursor.execute("DELETE FROM {} ".format(table_name))

#DELETING ALL ROWS OF THE TABLE
mycursor = mydb.cursor()
mycursor.execute("DELETE FROM {} ".format(table_name_label))
'''

# Form implementation generated from reading ui file 'sensor_reading_gui.ui'
# Created by: PyQt5 UI code generator 5.11.3
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
        global Img_corr_cnt, img_wrong, total_cnt, correct_try, incorrect, total_num_msg, correct, per, last_label,b,a
        
        ########################################### COMMAND ##################################################### 
        mycursor = mydb.cursor()
        response = sqs_client.get_queue_attributes(
            QueueUrl='https://sqs.us-east-1.amazonaws.com/229856064192/SuperProject_Cmd',
            AttributeNames=[
                'ApproximateNumberOfMessages',
            ]
        )
        num_msg=(response['Attributes']['ApproximateNumberOfMessages'])
      
        #READING DATA FROM QUEUE AND STORING IT IN SQL TABLE AND DELETING IT FROM THE QUEUE
        for i in range(int(num_msg)):
                q_msg = sqs_client.receive_message(
                    QueueUrl='https://sqs.us-east-1.amazonaws.com/229856064192/SuperProject_Cmd',
                    #MaxNumberOfMessages = 1
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
        mycursor.execute("SELECT * FROM MagicWand_eid where id > %s",(str(a),))
        myresult = mycursor.fetchall()

        print(myresult);
        
        #MANIPULATING THE VALUES OF THE IMAGES AND VOICE COMMANDS
        for z in range(len(myresult)):
          if(myresult[z][1]=='Sorry, can you please repeat that?' or myresult[z][1]=='Sorry, I could not understand. Goodbye.'):
            incorrect = incorrect + 1
          elif(myresult[z][1]=="Image correct"):
            Img_corr_cnt = Img_corr_cnt + 1
            total_cnt = total_cnt + 1
          elif(myresult[z][1]=="wrongo"):
            total_cnt = total_cnt + 1
  
          total_num_msg = total_num_msg + 1
          a = myresult[z][0]
        
        correct_try = total_num_msg - incorrect

        if(total_num_msg != 0):
          per = (correct_try/total_num_msg)*100

        img_wrong = total_cnt - Img_corr_cnt

        if(total_cnt != 0):
          percent_corr = (Img_corr_cnt/total_cnt)*100
          correct=str(percent_corr)
     
        ########################################### LABELS ##################################################### 
        response_label = sqs_client.get_queue_attributes(
            QueueUrl='https://sqs.us-east-1.amazonaws.com/229856064192/Superproject_Queue',
            AttributeNames=[
                'ApproximateNumberOfMessages',
            ]
        )
        num_msg_label=(response_label['Attributes']['ApproximateNumberOfMessages'])
        b=int(num_msg_label)

        
        #READING DATA FROM QUEUE AND STORING IT IN SQL TABLE AND DELETING IT FROM THE QUEUE
        for i in range(b):
                q_msg_label = sqs_client.receive_message(
                    QueueUrl='https://sqs.us-east-1.amazonaws.com/229856064192/Superproject_Queue',
                    #MaxNumberOfMessages = 1
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
          myresult = mycursor.fetchall()
        
          last_label = myresult[0][0]
        
        #SETTING THE VALUES IN THE GUI
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
   


