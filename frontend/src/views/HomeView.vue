<script setup lang="ts">
import EditIncident from '@/components/organisms/EditIncident.vue'
import { useIncidentsStore } from '@/stores/incidents'
import {
  RequestStatus,
  type RoadSegment,
  type Incident,
  type Request,
  IncidentSituation,
  IncidentStatus,
} from '@/types/api'

const store = useIncidentsStore()

function fakeData() {
  const confirmedRequest: Request = {
    id: 'a1cd9a50-bd27-4926-8786-f2bad80b3484',
    salvorName: 'bergweg',
    status: RequestStatus.Confirmed,
    createdAt: new Date(),
    updatedAt: new Date(),
  }

  const pendingRequest: Request = {
    id: 'a1cd9a50-bd27-4926-8786-f2bad80b3485',
    salvorName: 'bergweg',
    status: RequestStatus.Pending,
    createdAt: new Date(),
    updatedAt: new Date(),
  }

  const deniedRequest: Request = {
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
    status: IncidentStatus.Searching,
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

  store.add(completedIncident)
  store.add(dispatchedIncident)
  store.add(reportedIncident)
  store.add(pendingIncident)
  store.add(failedIncident)
}

fakeData()
</script>

<template>
  <main>
    <!-- TODO: update to submit patch to api -->
    <EditIncident
      v-if="store.selected"
      :incident="store.selected"
      @update="(incident) => console.log(incident)"
      @submitSalvorRequest="(incident) => console.log(incident)"
    />
  </main>
</template>
