FROM python:3
WORKDIR .
RUN pip install boto3
COPY . .