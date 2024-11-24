import boto3
import json
import os

def lambda_handler(event, context):
    print(f"{event} {type(event)}")  