import boto3
import json
import os
from boto3.dynamodb.conditions import Key
from decorators import cors_headers

dynamodb = boto3.resource('dynamodb')
incident_table = dynamodb.Table(os.environ['INCIDENT_TABLE_NAME'])

@cors_headers('GET')
def lambda_handler(event, context):    
    print(f"Event: {event}")

    try:
        response = incident_table.query(
            KeyConditionExpression=Key('PK').eq('INCIDENT')
        )
        
        print(f"Response: {response}")

        return {
            'statusCode': 200,
            'body': json.dumps(response['Items']),
            'headers': {
                'content-type': 'application/json'
            },
            'isBase64Encoded': False
        }
    except Exception as e:
        print(f"Error fetching incidents: {str(e)}")
        return {
            'statusCode': 500,
            'body': json.dumps({'message': 'Error fetching incidents'}),
            'headers': {
                'content-type': 'application/json'
            },
            'isBase64Encoded': False
        }