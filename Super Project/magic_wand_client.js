/*****************************************************************************************************************
* File Name: magic_wand.js
* Authors: Amreeta Sengupta and Ridhi Shah
* Description: This code is used to demonstrate Amazon Web Services (Lex, Polly, Rekognition)
* Date: 11/20/2019
* References: https://www.w3schools.com/nodejs/nodejs_raspberrypi_led_pushbutton.asp
*             https://nodejs.dev/nodejs-accept-arguments-from-the-command-line
*******************************************************************************************************************/


var myargs = process.argv.slice(2)
var Gpio = require('onoff').Gpio; 
var sleep = require('sleep');
var pushButton = new Gpio(14, 'in', 'falling'); 
const { exec } = require('child_process');

//Function to detect button press
pushButton.watch(function (err, value) { 
    if (err) { 
    console.error('There was an error', err); 
    return;
      }
      console.log('button pressed'); 
      //RECORDING AUDIO 
       exec('arecord -D plughw:1,0 -d 5 -r 16000 -f S16_LE -t wav test2.wav &&  aplay test2.wav');
       sleep.sleep(3);
       process.exit(0);
      
    });

//Capturing image
if(myargs[0] == 'Capture')
{
    exec('raspistill -o img1.jpg');
    process.exit(0);
}

//Playing audio mp3 file
if(myargs[0] == 'Audio')
{
    exec('omxplayer speech.mp3');
    process.exit(0);
}
