#*****************************************************************************************************************
# File Name: sensor_reading_gui.py
# Description: This code is used to send data to SQS and SNS services in AWS.
# Date: 10/23/2019
# References: https://startupnextdoor.com/adding-to-sqs-queue-using-aws-lambda-and-a-serverless-api-endpoint/
#			  https://docs.aws.amazon.com/iot/latest/developerguide/iot-lambda-rule.html 
#******************************************************************************************************************

from __future__ import print_function
  
import json
import boto3
  
print('Loading function')
  
def lambda_handler(event, context):

  
  evt = json.dumps(event)
  
  if "Alert" in evt:
    # Parse the JSON message 
    eventText = json.dumps(event["Alert"]);
    # Create an SNS client
    sns = boto3.client('sns',region_name='us-east-1')
    # Publish a message to the specified topic
    response = sns.publish (
      TopicArn = 'arn:aws:sns:us-east-1:229856064192:Sensor_SNS_Topic',
      Message = eventText
    )
  
  # Send Data to the SQS service
  elif "Data" in evt:
    sqs = boto3.resource('sqs')
    queue = sqs.get_queue_by_name(QueueName='New_Queue')
    response = queue.send_message(MessageBody=json.dumps(event["Data"]))
  
    
