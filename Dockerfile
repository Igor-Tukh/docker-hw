FROM python:3.7
WORKDIR .
ENV AWS_DEFAULT_REGION cn-north-1
RUN pip install boto3
COPY . .