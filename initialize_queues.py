import boto3
import time

if __name__ == '__main__':
    sqs = None
    while True:
        try:
            sqs = boto3.resource(service_name='sqs', endpoint_url='http://localstack:4576')
            break
        except:
            time.sleep(1)
            continue

    A_queue = sqs.create_queue(QueueName='A')
    B_queue = sqs.create_queue(QueueName='B')

    A_queue.send_message(MessageBody='1')
