#*****************************************************************************************************************
# File Name: magic_wand.py
# Description: This code is used to demonstrate Amazon Web Services (Lex, Polly, Rekognition)
# Date: 11/20/2019
# References: https://www.edureka.co/community/31884/how-to-upload-a-file-in-s3-bucket-using-boto3-in-python
#******************************************************************************************************************

#Import required Libraries
import boto3
import time
import os
import sys
import subprocess
import wave
from contextlib import closing
from tempfile import gettempdir
from botocore.exceptions import BotoCoreError, ClientError

__author__ = "Amreeta Sengupta, Ridhi Shah"
__copyright__ = "Copyright (C) 2019 by Amreeta Sengupta and Ridhi Shah"

s3 = boto3.resource('s3')
s3client = boto3.client('s3')
sqs_client = boto3.client('sqs')
polly_client = boto3.client('polly')
rekognition_client=boto3.client('rekognition')
lex_client = boto3.client('lex-runtime')

max_confidence = 0

while True:
   
    #Waiting for button press and user command
    os.system('node magic_wand_client.js')
    
    #ADDING OBJECTS TO S3 BUCKET
    response = s3client.list_buckets()
    for bucket in response["Buckets"]:
        print(bucket['Name'])


    #CONVERTING SPEECH TO TEXT USING AMAZON LEX
    obj = wave.open('/home/pi/Embedded-Interface-Design/Super Project/test2.wav','rb')

    response_lex = lex_client.post_content(
        botName='Magic_Wand',
        botAlias='Magicwand',
        userId='eid',
        contentType='audio/l16; rate=16000; channels=1',
        accept='text/plain; charset=utf-8',
        inputStream=obj.readframes(96044)
    )

    msg = response_lex['message']
    print(msg)

    #SENDING COMMAND TO SQS
    response = sqs_client.send_message(
        QueueUrl='https://sqs.us-east-1.amazonaws.com/229856064192/SuperProject_Cmd',
        MessageBody = msg
    )
    
    if(msg == 'Image Identified'):
        print('Capturing Image...')
        os.system('node magic_wand_client.js Capture')
        #os.system('raspistill -o img1.jpg')
        s3.Object('magic-wand','img1.jpg').upload_file(Filename='./img1.jpg')
        


        #IMAGE RECOGNITION USING AMAZON REKOGNITION
        image_s3 = {
        'S3Object': {
        'Bucket': "magic-wand", 'Name': "img1.jpg"
        }
        }

        response = rekognition_client.detect_labels(
        Image=image_s3,
        MaxLabels=10
        )

        for i in response["Labels"]:
            if (max_confidence < i['Confidence']):
                max_confidence = i['Confidence']
                label = i['Name']
                print(i['Name'])

        #CONVERTING TEXT TO SPEECH USING AMAZON POLLY
        str1 = "identified .huh."
        response = polly_client.synthesize_speech(VoiceId='Joanna',
                        OutputFormat='mp3', 
                        Text = label + str1)

        file = open('speech.mp3', 'wb')
        file.write(response['AudioStream'].read())
        file.close()
        
        os.system('node magic_wand_client.js Audio')
        #SENDING LABEL TO SQS
        response = sqs_client.send_message(
            QueueUrl='https://sqs.us-east-1.amazonaws.com/229856064192/Superproject_Queue',
            MessageBody = label
        )
       

