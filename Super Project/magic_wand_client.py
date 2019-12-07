sudo#*****************************************************************************************************************
# File Name: magic_wand.py
# Description: This code is used to demonstrate Amazon Web Services (Lex, Polly, Rekognition)
# Date: 11/20/2019
# References: https://www.edureka.co/community/31884/how-to-upload-a-file-in-s3-bucket-using-boto3-in-python
#******************************************************************************************************************

import boto3
import time
import os
import sys
import subprocess
import wave
from contextlib import closing
from tempfile import gettempdir
from botocore.exceptions import BotoCoreError, ClientError

s3 = boto3.resource('s3')
s3client = boto3.client('s3')
sqs_client = boto3.client('sqs')
polly_client = boto3.client('polly')
rekognition_client=boto3.client('rekognition')
lex_client = boto3.client('lex-runtime')

max_confidence = 0

#CAPTURING IMAGE USING CAMERA
os.system('raspistill -o img1.jpg')

#RECORDING AUDIO 
os.system('arecord -D plughw:1,0 -d 3 -r 16000 -f S16_LE -t wav test2.wav &&  aplay test2.wav')

#ADDING OBJECTS TO S3 BUCKET
response = s3client.list_buckets()
s3.Object('magic-wand','male.wav').upload_file(Filename='./male.wav')
s3.Object('magic-wand','pen.jpg').upload_file(Filename='./pen.jpg')
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
print(response_lex['message'])

#CONVERTING TEXT TO SPEECH USING AMAZON POLLY
response = polly_client.synthesize_speech(VoiceId='Joanna',
                OutputFormat='mp3', 
                Text = 'This is a sample text to be synthesized.')

file = open('speech.mp3', 'wb')
file.write(response['AudioStream'].read())
file.close()

#IMAGE RECOGNITION USING AMAZON REKOGNITION
image_s3 = {
  'S3Object': {
    'Bucket': "magic-wand", 'Name': "pen.jpg"
  }
}

response = rekognition_client.detect_labels(
  Image=image_s3,
  MaxLabels=10
)

for i in response["Labels"]:
    if (max_confidence < i['Confidence']):
        max_confidence = i['Confidence']
        print(i['Name'])

#SENDING DATA TO SQS
response = sqs_client.send_message(
    QueueUrl='https://sqs.us-east-1.amazonaws.com/229856064192/Superproject_Queue',
    MessageBody='AMY'
)
   

