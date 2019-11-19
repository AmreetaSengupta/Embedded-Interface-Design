#*****************************************************************************************************************
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
from contextlib import closing
from tempfile import gettempdir
from botocore.exceptions import BotoCoreError, ClientError

s3 = boto3.resource('s3')
s3client = boto3.client('s3')
#transcribe = boto3.client('transcribe')
sqs_client = boto3.client('sqs')
polly_client = boto3.client('polly')
rekognition_client=boto3.client('rekognition')

max_confidence = 0

#ADDING OBJECTS TO S3 BUCKET
response = s3client.list_buckets()
s3.Object('magic-wand','male.wav').upload_file(Filename='/home/pi/male.wav')
s3.Object('magic-wand','pen.jpg').upload_file(Filename='/home/pi/pen.jpg')
for bucket in response["Buckets"]:
    print(bucket['Name'])


'''
job_name = "magicwand5"
job_uri = "https://magic-wand.s3.amazonaws.com/male.wav"
transcribe.start_transcription_job(
    TranscriptionJobName=job_name,
    Media={'MediaFileUri': job_uri},
    MediaFormat='wav',
    LanguageCode='en-US'
)
while True:
    status = transcribe.get_transcription_job(TranscriptionJobName=job_name)
    if status['TranscriptionJob']['TranscriptionJobStatus'] in ['COMPLETED', 'FAILED']:
        break
    print("Not ready yet...")
    time.sleep(5)
print(status)

'''

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
   

