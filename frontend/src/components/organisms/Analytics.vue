<script setup lang="ts">
import { IncidentStatus, RequestStatus, type Incident } from '@/types/api'
import { type PropType } from 'vue'
import Card from '@/components/atoms/Card.vue'

const props = defineProps({
  incidents: {
    type: Object as PropType<Incident[]>,
    required: true,
  },
})

// ----

const incidentsThisWeek = props.incidents.filter((v) => {
  const now = new Date()
  const weekAgo = new Date()
  weekAgo.setDate(now.getDate() - 7)
  return v.createdAt > weekAgo
})

// ----

const completedIncidents = props.incidents.filter((v) => v.status === IncidentStatus.Completed)

const requestsAccepted = completedIncidents.filter(
  (v) =>
    v.status === IncidentStatus.Completed &&
    v.requests?.some((r) => r.status === RequestStatus.Confirmed),
)

const percentage = (requestsAccepted.length / completedIncidents.length) * 100

// ----

const averageResponseTime = requestsAccepted.reduce((acc, curr) => {
  const request = curr.requests?.find(
    (r) => r.status === RequestStatus.Confirmed || r.status === RequestStatus.Accepted,
  )

  if (request) {
    const diff = request.updatedAt.getTime() - request.createdAt.getTime()
    return acc + diff
  }

  return acc
}, 0)

const avgResponseTimeToMinutes = averageResponseTime / requestsAccepted.length / 1000 / 60
</script>

<template>
  <div class="grid grid-cols-6 grid-rows-6 gap-5 aspect-square">
    <Card class="col-span-2 row-span-2">
      <p>Total incidents this week</p>
      <p class="text-3xl font-bold">{{ incidentsThisWeek.length }}</p>
    </Card>
    <Card class="col-span-2 row-span-2">
      <p>Bergers geaccepteerd van gesloten incidenten</p>
      <p class="text-3xl font-bold">{{ percentage }}%</p>
    </Card>
    <Card class="col-span-1 row-span-1">
      <p>Gemiddelde antwoord tijd van Bergers</p>
      <p class="text-3xl font-bold">{{ avgResponseTimeToMinutes }} min.</p>
    </Card>
  </div>
</template>
