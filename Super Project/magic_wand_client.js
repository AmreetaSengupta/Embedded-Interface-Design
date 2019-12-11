/*****************************************************************************************************************
* File Name: magic_wand.js
* Description: This code is used to demonstrate Amazon Web Services (Lex, Polly, Rekognition)
* Date: 11/20/2019
* References: 
*******************************************************************************************************************/


var myargs = process.argv.slice(2)
var Gpio = require('onoff').Gpio; 
var sleep = require('sleep');
var pushButton = new Gpio(14, 'in', 'falling'); 
const { exec } = require('child_process');

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


if(myargs[0] == 'Capture')
{
    exec('raspistill -o img1.jpg');
    process.exit(0);
}
        
if(myargs[0] == 'Audio')
{
    exec('omxplayer speech.mp3');
    process.exit(0);
}
