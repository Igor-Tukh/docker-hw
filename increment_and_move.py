import boto3
import sys
import time

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Expected arguments: [first queue name] [second queue name]")
        print("Got only " + str(len(sys.argv) - 1) + " arguments")
        exit(-1)

    sqs = boto3.resource(service_name='sqs', endpoint_url='http://localstack:4576')
     
    from_queue = sqs.get_queue_by_name(QueueName=sys.argv[1])
    to_queue = sqs.get_queue_by_name(QueueName=sys.argv[2])
 
    while True:
        for message in from_queue.receive_messages():
            value = int(message.body)
            message.delete()
            to_queue.send_message(MessageBody=str(value + 1))
            print('{} receive {} from {}'.format(sys.argv[1], value, sys.argv[2]), flush=True)
