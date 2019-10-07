#*****************************************************************************************************************
# File Name: sensor_reading_gui.py
# Description: This code is used to store the sensor readings in a database and display these readings in a GUI 
#              and send data to the client through the Tornado Server.
# Date: 10/07/2019
# References: https://www.w3schools.com/python/python_mysql_drop_table.asp
#	      https://pimylifeup.com/raspberry-pi-humidity-sensor-dht22/ 
#	      https://pypi.org/project/multitimer/
#             https://matplotlib.org/
#             http://www.tornadoweb.org/en/stable/
#             https://www.pubnub.com/blog/nodejs-websocket-programmingexamples/
#             https://os.mbed.com/cookbook/Websockets-Server
#******************************************************************************************************************

import mysql.connector
import Adafruit_DHT
import datetime 
import threading
import multitimer
import tornado.httpserver
import tornado.websocket
import tornado.ioloop
import tornado.web
import socket
import asyncio
import json
from matplotlib import pyplot as plt
from PyQt5 import QtCore, QtGui, QtWidgets

__author__ = "Amreeta Sengupta, Ridhi Shah"
__copyright__ = "Copyright (C) 2019 by Amreeta Sengupta and Ridhi Shah"

#UPDATE THE USERNAME AND PASSWORD BEFORE RUNNING THE CODE
host_name = "localhost"
user_name = "ridhi_amreeta"
passwd_name = "eid19"
database_name = "sensor_readings"
table_name = "Sensor_Reading"
DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 4
conversion_type = 0
timer_count = 0

def timer_15():
        global timer_count
        timer_count = timer_count + 1
	#TO INSERT THE CONTENTS OF THE SENSOR INTO THE DATABASE TABLE
        humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
        if humidity is not None and temperature is not None:
                mycursor.execute("INSERT INTO {} (Humidity, Temperature, Timestamp) VALUES ({:0.2f},{:0.2f},'{}')".format(table_name, humidity, temperature, datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")))
                mydb.commit()
                ui.display_15_Fxn(humidity, temperature, datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S"))
                if timer_count == 30:
                        ui.exit_code_Fxn()
        else:
                ui.display_15_Fxn("None1", "None1", datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S"))

#TO ESTABLISH A CONNECTION TO THE MYSQL SERVER
mydb_tor = mysql.connector.connect(
  host=host_name,
  user=user_name,
  passwd=passwd_name
)

#CREATING A DATABASE
mycursor_tor = mydb_tor.cursor()

#TO ESTABLISH A CONNECTION TO THE MYSQL SERVER
mydb_tor = mysql.connector.connect(
  host=host_name,
  user=user_name,
  passwd=passwd_name,
  database=database_name
)
   
#CREATING A DATABASE
mycursor_tor = mydb_tor.cursor()

#TO ESTABLISH A CONNECTION TO THE MYSQL SERVER
mydb = mysql.connector.connect(
  host=host_name,
  user=user_name,
  passwd=passwd_name
)

#CREATING A DATABASE
mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE IF NOT EXISTS {}".format(database_name))

#TO ESTABLISH A CONNECTION TO THE MYSQL SERVER
mydb = mysql.connector.connect(
  host=host_name,
  user=user_name,
  passwd=passwd_name,
  database=database_name
)

"""
#TO DELETE A TABLE
mycursor = mydb.cursor()
mycursor.execute("DROP TABLE {}".format(table_name))

"""

#CREATING A TABLE IN THE DATABASE
mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE IF NOT EXISTS {} (id INT AUTO_INCREMENT PRIMARY KEY, Humidity FLOAT, Temperature FLOAT, Timestamp VARCHAR(30))".format(table_name))


"""
TO ALTER THE CONTENTS OF THE TABLE
mycursor.execute("ALTER TABLE {} MODIFY COLUMN Timestamp VARCHAR(30)".format(table_name))

#TO VIEW THE CONTENTS OF THE TABLE
mycursor.execute("SELECT * FROM {}".format(table_name))
for i in mycursor:
  print(i)
  
"""
#CONFIGURING THE TIMER 
timer = multitimer.MultiTimer(interval=15, function=timer_15, args=None, kwargs=None, count=30, runonstart=True)
timer.start()

# Form implementation generated from reading ui file 'sensor_reading_gui.ui'
# Created by: PyQt5 UI code generator 5.11.3

class Ui_gui(object):
        def setupUi(self, gui):
                gui.setObjectName("gui")
                gui.resize(811, 621)
                gui.setStyleSheet("background-color: rgb(255, 170, 127);\n"
                "background-color: rgb(170, 170, 255);")
                self.centralwidget = QtWidgets.QWidget(gui)
                self.centralwidget.setObjectName("centralwidget")
                self.pushButton_status = QtWidgets.QPushButton(self.centralwidget)
                self.pushButton_status.setGeometry(QtCore.QRect(270, 170, 99, 30))
                font = QtGui.QFont()
                font.setBold(True)
                font.setWeight(75)
                self.pushButton_status.setFont(font)
                self.pushButton_status.setStyleSheet("background-color: rgb(200, 199, 199);")
                self.pushButton_status.setObjectName("pushButton_status")
                self.temp_graph_pushButton = QtWidgets.QPushButton(self.centralwidget)
                self.temp_graph_pushButton.setGeometry(QtCore.QRect(20, 450, 191, 30))
                font = QtGui.QFont()
                font.setBold(True)
                font.setWeight(75)
                self.temp_graph_pushButton.setFont(font)
                self.temp_graph_pushButton.setStyleSheet("background-color: rgb(200, 199, 199);")
                self.temp_graph_pushButton.setObjectName("temp_graph_pushButton")
                self.humidity_graph_pushButton = QtWidgets.QPushButton(self.centralwidget)
                self.humidity_graph_pushButton.setGeometry(QtCore.QRect(600, 450, 191, 30))
                font = QtGui.QFont()
                font.setBold(True)
                font.setItalic(False)
                font.setWeight(75)
                self.humidity_graph_pushButton.setFont(font)
                self.humidity_graph_pushButton.setAutoFillBackground(False)
                self.humidity_graph_pushButton.setStyleSheet("background-color: rgb(200, 199, 199);")
                self.humidity_graph_pushButton.setObjectName("humidity_graph_pushButton")
                self.display_15 = QtWidgets.QLabel(self.centralwidget)
                self.display_15.setGeometry(QtCore.QRect(110, 240, 571, 22))
                font = QtGui.QFont()
                font.setBold(True)
                font.setWeight(75)
                self.display_15.setFont(font)
                self.display_15.setText("")
                self.display_15.setObjectName("display_15")
                self.temp_user = QtWidgets.QDoubleSpinBox(self.centralwidget)
                self.temp_user.setGeometry(QtCore.QRect(20, 370, 71, 32))
                self.temp_user.setStyleSheet("background-color: rgb(237, 237, 237);\n"
                "background-color: rgb(200, 199, 199);\n"
                "background-color: rgb(255, 255, 255);")
                self.temp_user.setObjectName("temp_user")
                self.humidity_user_2 = QtWidgets.QDoubleSpinBox(self.centralwidget)
                self.humidity_user_2.setGeometry(QtCore.QRect(700, 370, 71, 32))
                self.humidity_user_2.setStyleSheet("background-color: rgb(255, 255, 255);")
                self.humidity_user_2.setObjectName("humidity_user_2")
                self.celsius_faren = QtWidgets.QPushButton(self.centralwidget)
                self.celsius_faren.setGeometry(QtCore.QRect(410, 170, 101, 30))
                font = QtGui.QFont()
                font.setBold(True)
                font.setWeight(75)
                self.celsius_faren.setFont(font)
                self.celsius_faren.setStyleSheet("background-color: rgb(200, 199, 199);")
                self.celsius_faren.setObjectName("celsius_faren")
                self.threshold_label = QtWidgets.QLabel(self.centralwidget)
                self.threshold_label.setGeometry(QtCore.QRect(200, 510, 411, 71))
                font = QtGui.QFont()
                font.setBold(True)
                font.setWeight(75)
                self.threshold_label.setFont(font)
                self.threshold_label.setStyleSheet("background-color: rgb(170, 170, 255);")
                self.threshold_label.setText("")
                self.threshold_label.setObjectName("threshold_label")
                self.line = QtWidgets.QFrame(self.centralwidget)
                self.line.setGeometry(QtCore.QRect(0, 290, 801, 16))
                self.line.setFrameShape(QtWidgets.QFrame.HLine)
                self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
                self.line.setObjectName("line")
                self.line_2 = QtWidgets.QFrame(self.centralwidget)
                self.line_2.setGeometry(QtCore.QRect(380, 300, 20, 211))
                self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
                self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
                self.line_2.setObjectName("line_2")
                self.main_display = QtWidgets.QTextEdit(self.centralwidget)
                self.main_display.setGeometry(QtCore.QRect(110, 90, 581, 41))
                font = QtGui.QFont()
                font.setBold(True)
                font.setWeight(75)
                self.main_display.setFont(font)
                self.main_display.setAutoFillBackground(True)
                self.main_display.setStyleSheet("background-color: rgb(255, 255, 255);")
                self.main_display.setObjectName("main_display")
                self.line_3 = QtWidgets.QFrame(self.centralwidget)
                self.line_3.setGeometry(QtCore.QRect(0, 490, 811, 16))
                self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
                self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
                self.line_3.setObjectName("line_3")
                self.temperature_heading = QtWidgets.QLabel(self.centralwidget)
                self.temperature_heading.setGeometry(QtCore.QRect(130, 320, 151, 22))
                font = QtGui.QFont()
                font.setFamily("Noto Serif")
                font.setPointSize(13)
                font.setBold(True)
                font.setItalic(True)
                font.setWeight(75)
                self.temperature_heading.setFont(font)
                self.temperature_heading.setObjectName("temperature_heading")
                self.humidity_heading = QtWidgets.QLabel(self.centralwidget)
                self.humidity_heading.setGeometry(QtCore.QRect(550, 320, 131, 22))
                font = QtGui.QFont()
                font.setFamily("Noto Serif")
                font.setPointSize(13)
                font.setBold(True)
                font.setItalic(True)
                font.setWeight(75)
                self.humidity_heading.setFont(font)
                self.humidity_heading.setObjectName("humidity_heading")
                self.temperature_threshold_label = QtWidgets.QLabel(self.centralwidget)
                self.temperature_threshold_label.setGeometry(QtCore.QRect(130, 380, 221, 22))
                font = QtGui.QFont()
                font.setBold(True)
                font.setWeight(75)
                self.temperature_threshold_label.setFont(font)
                self.temperature_threshold_label.setObjectName("temperature_threshold_label")
                self.humidity_threshold_label = QtWidgets.QLabel(self.centralwidget)
                self.humidity_threshold_label.setGeometry(QtCore.QRect(480, 380, 211, 22))
                font = QtGui.QFont()
                font.setFamily("PibotoLt")
                font.setBold(True)
                font.setItalic(False)
                font.setWeight(75)
                self.humidity_threshold_label.setFont(font)
                self.humidity_threshold_label.setObjectName("humidity_threshold_label")
                self.main_heading = QtWidgets.QLabel(self.centralwidget)
                self.main_heading.setGeometry(QtCore.QRect(160, 20, 571, 22))
                font = QtGui.QFont()
                font.setFamily("Noto Serif")
                font.setPointSize(15)
                font.setBold(True)
                font.setItalic(True)
                font.setWeight(75)
                self.main_heading.setFont(font)
                self.main_heading.setObjectName("main_heading")
                gui.setCentralWidget(self.centralwidget)
                self.menubar = QtWidgets.QMenuBar(gui)
                self.menubar.setGeometry(QtCore.QRect(0, 0, 811, 28))
                self.menubar.setObjectName("menubar")
                gui.setMenuBar(self.menubar)
                self.statusbar = QtWidgets.QStatusBar(gui)
                self.statusbar.setObjectName("statusbar")
                gui.setStatusBar(self.statusbar)

                self.retranslateUi(gui)
                QtCore.QMetaObject.connectSlotsByName(gui)

        def retranslateUi(self, gui):
                _translate = QtCore.QCoreApplication.translate
                gui.setWindowTitle(_translate("gui", "Amreeta_Ridhi"))
                self.pushButton_status.setText(_translate("gui", "REFRESH"))
                self.temp_graph_pushButton.setText(_translate("gui", "TEMPERATURE PLOT"))
                self.humidity_graph_pushButton.setText(_translate("gui", "HUMIDITY PLOT"))
                self.celsius_faren.setText(_translate("gui", "C/F"))
                self.temperature_heading.setText(_translate("gui", "TEMPERATURE"))
                self.humidity_heading.setText(_translate("gui", "HUMIDITY"))
                self.temperature_threshold_label.setText(_translate("gui", "Set Temperature Threshold"))
                self.humidity_threshold_label.setText(_translate("gui", "Set Humidity Threshold"))
                self.main_heading.setText(_translate("gui", "TEMPERATURE AND HUMIDITY CONTROLLER"))
                self.pushButton_status.clicked.connect(self.pushButton_status_Fxn)
                self.humidity_graph_pushButton.clicked.connect(self.humidity_graph_pushButton_Fxn)
                self.temp_graph_pushButton.clicked.connect(self.temp_graph_pushButton_Fxn)
                self.temp_user.valueChanged.connect(self.temp_user_Fxn)
                self.humidity_user_2.valueChanged.connect(self.temp_user_Fxn)
                self.celsius_faren.clicked.connect(self.celsius_faren_Fxn)

        def pushButton_status_Fxn(self):
                #READING THE CURRENT HUMIDITY TEMPERATURE AND TIMESTAMP VALUES
                global conversion_type
                humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
                if conversion_type == 1:
                        temperature = (((9.0/5.0)*temperature) + 32)
                        self.main_display.setText("Humidity = {:0.2f} Temperature = {:0.2f} F Timestamp = {}".format(humidity, temperature, datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")))
                else:
                        self.main_display.setText("Humidity = {:0.2f} Temperature = {:0.2f} C Timestamp = {}".format(humidity, temperature, datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")))  
        
        def humidity_graph_pushButton_Fxn(self):
                #SELECTING THE HUMIDITY VALUES
                mycursor.execute("SELECT Humidity FROM {} ORDER BY id DESC LIMIT 10".format(table_name))
                humidity_data=list(mycursor)
                humidity_arr=[i[0] for i in humidity_data]
                #PLOTTING THE HUMIDITY VALUES
                humidity_fig=plt.figure(2)
                plt.plot(humidity_arr)
                plt.title('HUMIDITY GRAPH')
                plt.xlabel('INDEX')
                plt.ylabel('HUMIDITY (%)')
                plt.show()
        
              
        def temp_graph_pushButton_Fxn(self):
                #SELECTING THE TEMPERATURE VALUES
                global conversion_type
                mycursor.execute("SELECT Temperature FROM {} ORDER BY id DESC LIMIT 10".format(table_name))
                temp_data=list(mycursor)
                temp_arr=[i[0] for i in temp_data]
                if conversion_type == 1:
                        for j in range(10):
                                temp_arr[j]= (((9.0/5.0)*temp_arr[j]) + 32)
                #PLOTTING THE TEMPERATURE VALUES
                temp_fig=plt.figure(1)
                plt.plot(temp_arr)
                plt.title('TEMPERATURE GRAPH')
                plt.xlabel('INDEX')
                if conversion_type == 0:
                        plt.ylabel('TEMPERATURE (DEGREE CELSIUS)')
                else:
                        plt.ylabel('TEMPERATURE (FARENHEIT)')     
                plt.show()
        
        def display_15_Fxn(self, humidity, temperature, timestamp):
                #DISPLAYING THE SENSOR VALUES AFTER EVERY 15 SECONDS
                global conversion_type
                if humidity == "None1":
                        self.display_15.setText("Sensor not connected! Failed to Retrieve Data!")
                else:
                        if conversion_type == 1:
                                temperature = (((9.0/5.0)*temperature) + 32)
                                self.display_15.setText("Humidity = {:0.2f} Temperature = {:0.2f} F Timestamp = {}".format(humidity, temperature, timestamp))
                        else:
                                self.display_15.setText("Humidity = {:0.2f} Temperature = {:0.2f} C Timestamp = {}".format(humidity, temperature, timestamp))
                
        def temp_user_Fxn(self):
                #CHECKING FOR THE THRESHOLD VALUE SET BY USER
                humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
                if conversion_type == 1:
                        temperature = (((9.0/5.0)*temperature) + 32)
                temp_user1=self.temp_user.value()
                humidity_user1=self.humidity_user_2.value()
                if temperature > temp_user1 and humidity > humidity_user1:
                        self.threshold_label.setText("ALERT!! Maximum Temperature and Humidity exceeded!")
                elif humidity > humidity_user1:
                        self.threshold_label.setText("ALERT!! Maximum Humidity exceeded!")
                elif temperature > temp_user1:
                        self.threshold_label.setText("ALERT!! Maximum Temperature exceeded!")
                else:
                        self.threshold_label.setText("SAFE! Temperature and Humidity within limit!")
        
        def celsius_faren_Fxn(self):
                #CELSIUS TO FARENHEIT CONVERSION
                global conversion_type
                if conversion_type == 0:
                        conversion_type = 1
                else:
                        conversion_type = 0
        
        def exit_code_Fxn(self):
                #TO EXIT THE CODE AFTER 30 READS
                app.quit()

#SENDING DATA TO THE CLIENT THROUGH THE TORNADO SERVER
class WSHandler(tornado.websocket.WebSocketHandler):
        
        def open(self):
                print ('new connection')
      
        def on_message(self, message):
                if message == "Send the Current Value":
                        humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
                        if humidity is not None and temperature is not None:
                                timestamp=datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
                                refresh_data = {"Humidity":str(humidity),"Temperature":str(temperature),"Timestamp":str(timestamp)}
                                self.write_message(json.dumps(refresh_data))
                        else:
                                self.write_message("Error!")     
                                  
                elif message == "Send the table values":
                        mycursor_tor.execute("SELECT * FROM {} ORDER BY id DESC LIMIT 10".format(table_name))
                        d10_data= mycursor_tor.fetchall()
                        tor_dict = dict()
                        tor_list = list()
                        for i,j,k,l in d10_data:
                                tor_dict = {"ID":i, "Humidity":j, "Temperature":k, "Timestamp":l}
                                tor_list.append(tor_dict)
                        self.write_message(json.dumps(tor_list))
                    
        def on_close(self):
                print ('connection closed')
 
        def check_origin(self, origin):
                return True
 

application = tornado.web.Application([
(r'/ws', WSHandler),
])

#TORNADO SERVER CONNECTION
def tornado_server():
        asyncio.set_event_loop(asyncio.new_event_loop())
        http_server = tornado.httpserver.HTTPServer(application)
        http_server.listen(8800)
        myIP = socket.gethostbyname(socket.gethostname())
        print ('*** Websocket Server Started at %s***' % myIP)
        tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
        import sys
        app = QtWidgets.QApplication(sys.argv)
        gui = QtWidgets.QMainWindow()
        ui = Ui_gui()
        ui.setupUi(gui)
        gui.show()
        t1 = threading.Thread(target=tornado_server)
        t1.start() 
        sys.exit(app.exec_())
        t1.join() 

