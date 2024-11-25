import {
  type Incident,
  IncidentSituation,
  IncidentStatus,
  RequestStatus,
  type RoadSegment,
  type SalvorRequest,
} from '@/types/api'
import axios from 'axios'
import type { UUID } from 'crypto'

export const apiClient = axios.create({
  baseURL: import.meta.env.VITE_PROD_URL + '/incidents',
  headers: {
    'Content-Type': 'application/json',
    'Allow-Control-Allow-Origin': '*',
  },
})

function randomUUID(): UUID {
  return 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, function (c) {
    const r = (Math.random() * 16) | 0,
      v = c === 'x' ? r : (r & 0x3) | 0x8
    return v.toString(16)
  }) as UUID
}

export const getIncidents = async (): Promise<Incident[]> => {
  return apiClient
    .get('/')
    .then((response) => response.data)
    .then((data) => data.map(mapIncidentFromAPI)) as Promise<Incident[]>
}

// Fake API call
// export const getIncidents = async (): Promise<Incident[]> => {
//   return new Promise((resolve) => {
//     setTimeout(() => {
//       const dateOneHourFuture = new Date()
//       dateOneHourFuture.setHours(dateOneHourFuture.getHours() + 1)

//       const confirmedRequest: SalvorRequest = {
//         id: 'a1cd9a50-bd27-4926-8786-f2bad80b3484',
//         salvorName: 'bergweg',
//         status: RequestStatus.Confirmed,
//         createdAt: new Date(),
//         updatedAt: dateOneHourFuture,
//       }
//       const pendingRequest: SalvorRequest = {
//         id: 'a1cd9a50-bd27-4926-8786-f2bad80b3485',
//         salvorName: 'bergweg',
//         status: RequestStatus.Pending,
//         createdAt: new Date(),
//         updatedAt: new Date(),
//       }
//       const deniedRequest: SalvorRequest = {
//         id: 'a1cd9a50-bd27-4926-8786-f2bad80b3486',
//         salvorName: 'bergweg',
//         status: RequestStatus.Denied,
//         createdAt: new Date(),
//         updatedAt: new Date(),
//       }
//       const roadSegment: RoadSegment = {
//         id: '123',
//         roadNumber: 'A15',
//         firstName: 'A15 vanuit Europoort',
//         secondName: 'A16 richting Rotterdam (parallelbaan)',
//       }

//       const completedIncident: Incident = {
//         id: randomUUID(),
//         situation: IncidentSituation.VehicleObstruction,
//         status: IncidentStatus.Completed,
//         lat: 52.3079872,
//         long: 4.811863,
//         createdAt: new Date(),
//         updatedAt: new Date(),
//         segment: roadSegment,
//         requests: [confirmedRequest],
//       }

//       const dispatchedIncident: Incident = {
//         id: randomUUID(),
//         situation: IncidentSituation.VehicleObstruction,
//         status: IncidentStatus.Dispatched,
//         lat: 52.3079872,
//         long: 4.811863,
//         createdAt: new Date(),
//         updatedAt: new Date(),
//         segment: roadSegment,
//         requests: [confirmedRequest],
//       }

//       const reportedIncident: Incident = {
//         id: randomUUID(),
//         situation: IncidentSituation.VehicleObstruction,
//         status: IncidentStatus.Reported,
//         lat: 52.3079872,
//         long: 4.811863,
//         createdAt: new Date(),
//         updatedAt: new Date(),
//         segment: roadSegment,
//       }

//       const pendingIncident: Incident = {
//         id: randomUUID(),
//         situation: IncidentSituation.VehicleObstruction,
//         status: IncidentStatus.Pending,
//         lat: 52.3079872,
//         long: 4.811863,
//         createdAt: new Date(),
//         updatedAt: new Date(),
//         segment: roadSegment,
//         requests: [pendingRequest],
//       }

//       const failedIncident: Incident = {
//         id: randomUUID(),
//         situation: IncidentSituation.VehicleObstruction,
//         status: IncidentStatus.Failed,
//         lat: 52.3079872,
//         long: 4.811863,
//         createdAt: new Date(),
//         updatedAt: new Date(),
//         segment: roadSegment,
//         requests: [deniedRequest],
//       }

//       resolve([
//         completedIncident,
//         dispatchedIncident,
//         reportedIncident,
//         pendingIncident,
//         failedIncident,
//       ])
//     }, 100)
//   })
// }

export const createIncident = async (incident: Incident): Promise<Incident> => {
  return apiClient
    .post('/incidents', mapIncidentToApi(incident))
    .then((response) => response.data) as Promise<Incident>
}

function mapIncidentFromAPI(data: Record<string, string | number>): Incident {
  return {
    id: data.incidentId as UUID,
    situation: data.incidentSituation as IncidentSituation,
    status: data.incidentStatus as IncidentStatus,
    lat: data.incidentLat as number,
    long: data.incidentLong as number,
    createdAt: new Date(data.createdAt),
    updatedAt: new Date(data.updatedAt),
    // segment: incident.segment as RoadSegment,
    // requests: incident.requests,
  }
}

function mapIncidentToApi(data: Incident): Record<string, string | number> {
  // TODO: implement once map FROM api is implemented
  return {}
}
