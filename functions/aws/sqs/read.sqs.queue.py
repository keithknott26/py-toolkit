#!/usr/bin/python

"""
The following script creates an SQS queue and polls 
the queue for messages until no messages are 
received or it receives as many messages as it is 
expecting.  This script assumes a message format
published by its twin sqs_send_benchmark.py.
After receiving messages the script summarizes
the executiong with a count of messages received
and how many seconds the receipt took to execute.
"""

import boto3
import json
from time import sleep, time

sqs = boto3.resource ('sqs')

queue_name = 'q-abc-123'
print "Subscribing to queue with a name of {0}".format (queue_name)

queue = sqs.create_queue (QueueName = queue_name)

print "sleeping 5 seconds"
sleep (5)

expected_message_count = 999
message_recv_count = 0
start_time = time ()
while message_recv_count < expected_message_count:
    messages = queue.receive_messages (MaxNumberOfMessages = 10)

    if len(messages) == 0:
        print ("Queue is empty, exiting...")
        break

    for msg in messages:
        body = json.loads(msg.body)
        print ("Recv {0}, sent @ {1}".format (body['message'], body['sent']))
        message_recv_count += 1
        expected_message_count = body['seq_limit']
        msg.delete ()

print ("Received {0} messages in {1} sec".format (message_recv_count, time () - start_time))