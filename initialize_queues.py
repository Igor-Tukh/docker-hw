import boto3
import time

if __name__ == '__main__':
    time.sleep(12) # reducing number of exceptions by waiting

    sqs = boto3.resource(service_name='sqs', endpoint_url='http://localstack:4576')
    
    A_queue = sqs.create_queue(QueueName='A')
    B_queue = sqs.create_queue(QueueName='B')

    A_queue.send_message(MessageBody='1')
