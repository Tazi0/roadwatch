import {
  type SalvorRequest,
  RequestStatus,
  type RoadSegment,
  type Incident,
  IncidentSituation,
  IncidentStatus,
} from '@/types/api'
import axios from 'axios'

export const apiClient = axios.create({
  baseURL: import.meta.env.VITE_PROD_URL + '/api',
  headers: {
    'Content-Type': 'application/json',
  },
})

// TODO: replace object with the type of the response
// export const getExample = async (id: string): Promise<object> => {
//   return apiClient.get(`/example/${id}`).then((response) => response.data) as Promise<object>
// }

// Fake API call
export const getIncidents = async (): Promise<Incident[]> => {
  return new Promise((resolve) => {
    setTimeout(() => {
      const dateOneHourFuture = new Date()
      dateOneHourFuture.setHours(dateOneHourFuture.getHours() + 1)

      const confirmedRequest: SalvorRequest = {
        id: 'a1cd9a50-bd27-4926-8786-f2bad80b3484',
        salvorName: 'bergweg',
        status: RequestStatus.Confirmed,
        createdAt: new Date(),
        updatedAt: dateOneHourFuture,
      }
      const pendingRequest: SalvorRequest = {
        id: 'a1cd9a50-bd27-4926-8786-f2bad80b3485',
        salvorName: 'bergweg',
        status: RequestStatus.Pending,
        createdAt: new Date(),
        updatedAt: new Date(),
      }
      const deniedRequest: SalvorRequest = {
        id: 'a1cd9a50-bd27-4926-8786-f2bad80b3486',
        salvorName: 'bergweg',
        status: RequestStatus.Denied,
        createdAt: new Date(),
        updatedAt: new Date(),
      }
      const roadSegment: RoadSegment = {
        id: '123',
        roadNumber: 'A15',
        firstName: 'A15 vanuit Europoort',
        secondName: 'A16 richting Rotterdam (parallelbaan)',
      }

      const completedIncident: Incident = {
        id: 'RS03_944632',
        situation: IncidentSituation.VehicleObstruction,
        status: IncidentStatus.Completed,
        lat: 52.3079872,
        long: 4.811863,
        createdAt: new Date(),
        updatedAt: new Date(),
        segment: roadSegment,
        requests: [confirmedRequest],
      }

      const dispatchedIncident: Incident = {
        id: 'RS03_944633',
        situation: IncidentSituation.VehicleObstruction,
        status: IncidentStatus.Dispatched,
        lat: 52.3079872,
        long: 4.811863,
        createdAt: new Date(),
        updatedAt: new Date(),
        segment: roadSegment,
        requests: [confirmedRequest],
      }

      const reportedIncident: Incident = {
        id: 'RS03_944634',
        situation: IncidentSituation.VehicleObstruction,
        status: IncidentStatus.Reported,
        lat: 52.3079872,
        long: 4.811863,
        createdAt: new Date(),
        updatedAt: new Date(),
        segment: roadSegment,
      }

      const pendingIncident: Incident = {
        id: 'RS03_944635',
        situation: IncidentSituation.VehicleObstruction,
        status: IncidentStatus.Pending,
        lat: 52.3079872,
        long: 4.811863,
        createdAt: new Date(),
        updatedAt: new Date(),
        segment: roadSegment,
        requests: [pendingRequest],
      }

      const failedIncident: Incident = {
        id: 'RS03_944636',
        situation: IncidentSituation.VehicleObstruction,
        status: IncidentStatus.Failed,
        lat: 52.3079872,
        long: 4.811863,
        createdAt: new Date(),
        updatedAt: new Date(),
        segment: roadSegment,
        requests: [deniedRequest],
      }

      resolve([
        completedIncident,
        dispatchedIncident,
        reportedIncident,
        pendingIncident,
        failedIncident,
      ])
    }, 100)
  })
}
