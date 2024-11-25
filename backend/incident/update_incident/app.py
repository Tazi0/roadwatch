import boto3
import json
import os
from datetime import datetime
from boto3.dynamodb.conditions import Key
from decorators import cors_headers

dynamodb = boto3.resource('dynamodb')
incident_table = dynamodb.Table(os.environ['INCIDENT_TABLE_NAME'])

@cors_headers('PUT')
def lambda_handler(event, context):
    print(f"Event: {event}")
    
    try:        
        body = json.loads(event.get('body'))
        
        print(f"Body: {body}")
                
        incident_id = event['pathParameters']['incident_id']
        
        existing_incident = incident_table.get_item(
            Key={
                'PK': 'INCIDENT',
                'SK': f'INCIDENT#{event['pathParameters']['incident_id']}'
            }
        )
                
        if 'Item' not in existing_incident:
            return {
                'statusCode': 404,
                'body': json.dumps({'message': 'Incident not found'}),
                'headers': {
                    'content-type': 'application/json'
                },
                "isBase64Encoded": False
            }

        incident_status = body.get('incidentStatus')
        
        update_expression = "SET createdAt = :c, incidentSituation = :s, updatedAt = :u, incidentLat = :lat, incidentLong = :long"
        expression_attribute_values = {
            ':c': body.get('createdAt'),
            ':s': body.get('incidentSituation'),
            ':u': datetime.now().isoformat(),
            ':lat': body.get('incidentLat'),
            ':long': body.get('incidentLong'),
        }
        
        if incident_status == 'REPORTED' or incident_status == 'COMPLETED':
            update_expression += ", incidentStatus = :status, GSI1SK = :GSI1SK"
            expression_attribute_values[':status'] = incident_status
            expression_attribute_values[':GSI1SK'] = f'{incident_status}#{incident_id}'
                 
        response = incident_table.update_item(
            Key={
                'PK': 'INCIDENT',
                'SK': f'INCIDENT#{incident_id}'
            },
            UpdateExpression=update_expression,
            ExpressionAttributeValues=expression_attribute_values,
            ReturnValues="UPDATED_NEW"
        )
        
        return {
            'statusCode': 200,
            'body': json.dumps({'message': 'Incident updated successfully', 'incidentId': incident_id}),
            'headers': {
                'content-type': 'application/json'
            },
            "isBase64Encoded": False
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
    