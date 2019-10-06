/*****************************************************************************************************************
* File Name: websocket-server.js
* Description: 
* Author: Amreeta Sengupta and Ridhi Shah
* Date: 10/04/2019
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
 
    /* // To display contents of the Table
    var show_table = 'select * from ' + table_name + '';
    con.query(show_table, function (err, result) {
    if (err) throw err;
    console.log("table shown");
    console.log(result);
});*/


// Node.js WebSocket server script
});

wsServer.on('request', function(request) {
    const connection = request.accept(null, request.origin);
    connection.on('message', function(message) {
     if(message.utf8Data == "Hi this is web client."){
      con.query('SELECT * from ' + table_name + ' ORDER BY id DESC LIMIT 1', function(err, rows, fields) {
        if (!err)
         var string_rows = JSON.stringify(rows);
         console.log(string_rows);
         connection.sendUTF(string_rows);
        //else
         //console.log('Error while performing Query.');  
      //console.log('Received Message:', message.utf8Data);
      //connection.sendUTF(server_string);
    
  });
}
});
    connection.on('close', function(reasonCode, description) {
        console.log('Client has disconnected.');
    });

});

/*
con.query('SELECT * from ' + table_name + ' ORDER BY id DESC LIMIT 1', function(err, rows, fields) {
  if (!err)
    var string_rows = JSON.stringify(rows);
    console.log(string_rows);
  else
    console.log('Error while performing Query.');  
  
  //console.log(rows[0].id);
  //console.log(rows[0].temperature);
  //console.log(rows[0].humidity);
  //console.log(rows[0].timestamp);
  
});
});

*/

