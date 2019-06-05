import boto3

sqs = boto3.resource(service_name='sqs', endpoint_url='http://localstack:4576')

def create_queue(name):
    return sqs.create_queue(name)
    
A_queue = sqs.create_queue('A')
B_queue = sqs.create_queue('B')

A_queue.send_message('1')    
