FROM python:3.7
WORKDIR .
RUN pip install boto3
COPY . .