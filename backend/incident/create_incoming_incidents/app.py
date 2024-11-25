import boto3
import json
import os
import requests
from datetime import datetime

dynamodb = boto3.resource('dynamodb')
incident_table = dynamodb.Table(os.environ['INCIDENT_TABLE_NAME'])

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

            situation_record = incident_data['situation'][0]['situationRecord']
            
            created_at = datetime.strptime(situation_record['situationRecordCreationTime'], "%Y-%m-%dT%H:%M:%SZ")
              
            incident_table.put_item(
                Item={
                    'PK': 'INCIDENT',
                    'SK': f'INCIDENT#{incident_id}',
                    'type': 'INCIDENT',
                    'incidentId': incident_id,
                    'createdAt': created_at.isoformat(),
                    'updatedAt': datetime.now().isoformat(),
                    'incidentSituation': situation_record['@xsi:type'],
                    'incidentStatus': 'REPORTED',
                    'incidentLat': situation_record['groupOfLocations']['locationForDisplay']['latitude'],
                    'incidentLong': situation_record['groupOfLocations']['locationForDisplay']['longitude'],
                }
            )
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
            
    # Een incident kan handmatig afgesloten worden. Dit incident wordt niet meer weergegeven in de FE. Het incident blijft afgesloten ook al komt het incident opnieuw binnen via de incidenten API.

    