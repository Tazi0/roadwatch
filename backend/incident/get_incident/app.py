import boto3
import json
import os
from boto3.dynamodb.conditions import Key

dynamodb = boto3.resource('dynamodb')
table_name = os.environ['TABLE_NAME']
table = dynamodb.Table(table_name)

def lambda_handler(event, context):    
    print(f"Event: {event}")

    try:
        response = table.get_item(
            Key={
                'PK': 'INCIDENT',
                'SK': f'INCIDENT#{event['pathParameters']['incident_id']}'
            }
        )
        
        print(f"Response: {response}")
        
        if 'Item' not in response:
            return {
                'statusCode': 404,
                'body': json.dumps({'message': 'Incident not found'}),
                'headers': {
                    'content-type': 'application/json'
                },
                "isBase64Encoded": False
            }

        return {
            'statusCode': 200,
            'body': json.dumps(response['Item']),
            'headers': {
                'content-type': 'application/json'
            },
            "isBase64Encoded": False
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