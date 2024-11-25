import boto3
import json
import os
from datetime import datetime
import uuid
from decorators import cors_headers

dynamodb = boto3.resource('dynamodb')
incident_table = dynamodb.Table(os.environ['INCIDENT_TABLE_NAME'])

@cors_headers('POST')
def lambda_handler(event, context):
    print(f"Event: {event}")
    
    try:        
        body = json.loads(event.get('body'))
        
        print(f"Body: {body}")
                
        incident_id = str(uuid.uuid4())
                
        incident_table.put_item(
            Item={
                'PK': 'INCIDENT',
                'SK': f'INCIDENT#{incident_id}',
                'type': 'INCIDENT',
                'incidentId': incident_id,
                'createdAt': body.get('createdAt'),
                'updatedAt': datetime.now().isoformat(),
                'incidentSituation': body.get('incidentSituation'),
                'incidentStatus': 'REPORTED',
                'incidentLat': body.get('incidentLat'),
                'incidentLong': body.get('incidentLong'),
                'GSI1PK': 'INCIDENT',
                'GSI1SK': f'REPORTED#{incident_id}'
            }
        )
        
        return {
            'statusCode': 201,
            'body': json.dumps({'message': 'Incident created successfully', 'incidentId': incident_id}),
            'headers': {
                'content-type': 'application/json'
            },
            'isBase64Encoded': False
        }
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
    