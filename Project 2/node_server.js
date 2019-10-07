/*****************************************************************************************************************
* File Name: node_server.js
* Description: This code implements a Node.js server and communicates with a HTML client.
* Author: Amreeta Sengupta and Ridhi Shah
* Date: 10/07/2019
* References: https://www.w3schools.com/nodejs/nodejs_mysql.asp
*             https://www.pubnub.com/blog/nodejs-websocket-programming-examples/
******************************************************************************************************************/

const http = require('http');
var mysql = require('mysql');

const WebSocketServer = require('websocket').server;
const server = http.createServer();
server.listen(9898);
const wsServer = new WebSocketServer({
    httpServer: server
});
// Update Username and Password before running the code
var host_name = "localhost"
var user_name = "ridhi_amreeta"
var passwd_name = "eid19"
var database_name = "sensor_readings"
var table_name = "Sensor_Reading"
var server_string = 'Hi this is WebSocket server!'

// Create Connection with mysql server
var con = mysql.createConnection({
  host: host_name,
  user: user_name,  
  password: passwd_name
});

con.connect(function(err) {
  if (err) throw err;  
});

// Create Connection with database
var con = mysql.createConnection({
  host: host_name,
  user: user_name,
  password: passwd_name,
  database: database_name
});

con.connect(function(err) {
  if (err) throw err;  
});

// Sending Data to the client
wsServer.on('request', function(request) {
    const connection = request.accept(null, request.origin);
    connection.on('message', function(message) {
     if(message.utf8Data == "Hi this is web client."){
     con.query('SELECT * from ' + table_name + ' ORDER BY id DESC LIMIT 10', function(err, rows, fields) {
     if (!err)
         var string_rows_10 = JSON.stringify(rows);
         console.log(string_rows_10);
         connection.sendUTF(string_rows_10);
      
      });
    }
  });
    connection.on('close', function(reasonCode, description) {
      console.log('Client has disconnected.');
  });
});

