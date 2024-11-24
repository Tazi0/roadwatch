import boto3
import json
import os
import requests

dynamodb = boto3.resource('dynamodb')
table_name = os.environ['TABLE_NAME']
table = dynamodb.Table(table_name)

def lambda_handler(event, context):
    print(f"Event: {event}")
    
    for record in event['Records']:
        try:
            sns_message = json.loads(record['Sns']['Message'])
            incident_id = sns_message['id']
                
            response = requests.get(f"https://roadinfo.cloud-native-minor.it/roadIncidents/{incident_id}")
            
            if response.status_code != 200:
                print(f"Failed to fetch incident data. Status code: {response.status_code}")
                continue
            
            incident_data = response.json()
            print(f"Incident data: {incident_data}")
        except Exception as e:
            print(f"Error fetching incident data: {str(e)}")
            return {
                'statusCode': 500,
                'body': json.dumps({'message': 'Error fetching incident data'}),
                'headers': {
                    'content-type': 'application/json'
                },
                'isBase64Encoded': False
            }
    