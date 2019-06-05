import boto3

if __name__ == '__main__':
    sqs = boto3.resource(service_name='sqs', endpoint_url='http://localstack:4576')

    A_queue = sqs.create_queue('A')
    B_queue = sqs.create_queue('B')

    A_queue.send_message('1')
