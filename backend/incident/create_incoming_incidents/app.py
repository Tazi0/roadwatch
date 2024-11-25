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
            
            existing_incident = incident_table.get_item(
                Key={
                    'PK': 'INCIDENT',
                    'SK': f'INCIDENT#{incident_id}'
                }
            )
            
            if 'Item' in existing_incident and existing_incident['Item']['incidentStatus'] == 'COMPLETED':
                print(f"Incident already exists and is completed: {incident_id}")
                continue
            
            incident_data = response.json()
            print(f"Incident data: {incident_data}")

            situation_record = incident_data['situation'][0]['situationRecord']
            group_of_locations = situation_record['groupOfLocations']
                            
            if 'alertCLinear' in group_of_locations:
                road_segment_id = group_of_locations['alertCLinear']['alertCMethod4PrimaryPointLocation']['alertCLocation']['specificLocation']
            elif 'alertCPoint' in group_of_locations:
                road_segment_id = group_of_locations['alertCPoint']['alertCMethod4PrimaryPointLocation']['alertCLocation']['specificLocation']
            else:
                road_segment_id = None
              
            incident_table.put_item(
                Item={
                    'PK': 'INCIDENT',
                    'SK': f'INCIDENT#{incident_id}',
                    'type': 'INCIDENT',
                    'incidentId': incident_id,
                    'createdAt': situation_record['situationRecordCreationTime'],
                    'updatedAt': datetime.now().isoformat(),
                    'incidentSituation': situation_record['@xsi:type'],
                    'incidentStatus': 'REPORTED',
                    'incidentLat': group_of_locations['locationForDisplay']['latitude'],
                    'incidentLong': group_of_locations['locationForDisplay']['longitude'],
                    'GSI1PK': 'INCIDENT',
                    'GSI1SK': f'REPORTED#{incident_id}',
                    'incidentRoadSegmentId': road_segment_id,
                }
            )
        except Exception as e:
            print(f"Error fetching incident data: {str(e)}")
    