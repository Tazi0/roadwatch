import boto3
import json
import os
from boto3.dynamodb.conditions import Key

dynamodb = boto3.resource('dynamodb')
table_name = os.environ['TABLE_NAME']
table = dynamodb.Table(table_name)

def lambda_handler(event, context):    
    print(f"{event} {type(event)}")

    # try:
    #     response = table.query(
    #         KeyConditionExpression=Key('PK').eq('INCIDENT')
    #     )
        
    #     incidents = response['Items']
        
    #     incidents_json = json.dumps(incidents)

    #     return {
    #         'statusCode': 200,
    #         'body': incidents_json,
    #         'headers': {
    #             'content-type': 'application/json'
    #         },
    #         'isBase64Encoded': False
    #     }
    # except Exception as e:
    #     print(f"Error fetching incidents: {str(e)}")
    #     return {
    #         'statusCode': 500,
    #         'body': json.dumps({'message': 'Error fetching incidents'}),
    #         'headers': {
    #             'content-type': 'application/json'
    #         },
    #         'isBase64Encoded': False
    #     }