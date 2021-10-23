#!/usr/bin/python

"""
The following script creates an SQS queue and publishes
MESSAGE_COUNT messages as quickly as possible.  It provides
a report of the messages sent as it sends them and 
notifies of any publication errors.  It summarizes the
execution with a count of messages published, how many
publications had errors, and how many seconds it took
to publish the messages.
"""

import boto3
import json
import time
from uuid import uuid4

MESSAGE_COUNT = 103

sqs = boto3.client ('sqs', region_name = 'eu-west-1')

q_name = 'q-abc-123'

print "Publishing a message to queue {0}".format (q_name)

queue = sqs.create_queue (QueueName = q_name)
queue_url = queue['QueueUrl']

error_count = 0
start_time = time.time ()
for i in range(MESSAGE_COUNT):
    # forge a new message
    message = {
        'seq': i, 
        'seq_limit': MESSAGE_COUNT,
        'sent': time.time (), 
        'message_id': str(uuid4 ()), 
        'message': "Message {0} of {1}".format (i, MESSAGE_COUNT)
        }

    resp = sqs.send_message (QueueUrl = queue_url, MessageBody = json.dumps (message))

    # check to ensure the publication was successful
    if resp['ResponseMetadata']['HTTPStatusCode'] != 200:
        print ("Error publishing message: {0}".format (message))
        print ("Response: {0}".format (resp))
        error_count += 1
    else:
        print ("Sent {0} @ {1}".format (message['message'], message['sent']))

# print a summary report
print ("Sent {0} messages with {1} errors in {2} sec".format (MESSAGE_COUNT, error_count, time.time () - start_time))