import type { UUID } from 'crypto'

export enum IncidentStatus {
  Reported = 'REPORTED',
  Completed = 'COMPLETED',
  Failed = 'FAILED',
  Dispatched = 'DISPATCHED',
  Searching = 'SEARCHING', // custom status (if request is pending or accepted)
}

export enum IncidentSituation {
  VehicleObstruction = 'VehicleObstruction',
  Accident = 'Accident',
}

export enum RequestStatus {
  Pending = 'PENDING',
  Accepted = 'ACCEPTED',
  Denied = 'DENIED',
  Failed = 'FAILED',
  Cancelled = 'CANCELLED',
  Confirmed = 'CONFIRMED',
}

export interface Incident {
  id: string // RijksWaterStaat ID
  situation: IncidentSituation
  status: IncidentStatus
  lat: number
  long: number
  createdAt: Date
  updatedAt: Date
  segment?: RoadSegment
  requests?: Request[]
}

export type RoadSegment = {
  id: string
  roadNumber: string
  firstName: string
  secondName: string
}

export type Request = {
  id: UUID
  salvorName: string
  status: RequestStatus
  createdAt: Date
  updatedAt: Date
}
