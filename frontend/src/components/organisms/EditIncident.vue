<script setup lang="ts">
import { IncidentSituation, IncidentStatus, type Incident } from '@/types/api'
import { defineProps, ref, watch, type PropType } from 'vue'
import Input from '@/components/atoms/Input.vue'
import Heading from '@/components/atoms/Heading.vue'
import { Button } from '@/components/ui/button'
import { useIncidentsStore } from '@/stores/incidents'

const store = useIncidentsStore()

const emit = defineEmits<{
  (e: 'update', value: Incident): void
  (e: 'create', value: Incident): void
  (e: 'submitSalvorRequest', value: Incident): void
}>()

const props = defineProps({
  incident: {
    type: Object as PropType<Incident>,
    required: false,
  },
  autoUpdate: {
    type: Boolean,
    required: false,
    default: false,
  },
})

let oldIncident = props.incident || ({} as Incident)
const incident = ref<Incident>(props.incident || ({} as Incident))
const isNewIncident = ref<boolean>(!oldIncident.id)

if (props.autoUpdate) {
  if (store.selected) {
    incident.value = store.selected
  }

  watch(store, (newStore) => {
    if (newStore.selected) {
      incident.value = newStore.selected
      oldIncident = newStore.selected
      isNewIncident.value = false
    }
  })

  watch(incident, (newIncident) => {
    if (!newIncident.id) {
      store.selected = undefined
    } else if (!isNewIncident.value) {
      emit('update', newIncident)
    }
  })
}

const incidentSituationOptions = [
  { value: IncidentSituation.VehicleObstruction, label: 'Vehicle Obstruction' },
  { value: IncidentSituation.Accident, label: 'Accident' },
]

const incidentStatusOptions = [
  { value: IncidentStatus.Reported, label: 'Reported' },
  { value: IncidentStatus.Completed, label: 'Completed' },
  { value: IncidentStatus.Failed, label: 'Failed', disabled: true },
  { value: IncidentStatus.Dispatched, label: 'Dispatched', disabled: true },
  { value: IncidentStatus.Pending, label: 'Pending', disabled: true },
]

function handleSubmit(event: Event) {
  event.preventDefault()
  emit('create', incident.value)
  oldIncident = incident.value
}

function handeClear() {
  incident.value = {} as Incident
  oldIncident = {} as Incident
  isNewIncident.value = true
}
</script>

<template>
  <div>
    <Heading level="1" v-if="!isNewIncident">Bewerk Incident</Heading>
    <Heading level="1" v-else>Creeër Incident</Heading>

    <form class="flex flex-col gap-3 mb-6">
      <Input
        label="Incident ID"
        :value="incident.id"
        type="text"
        placeholder="Incident ID"
        required
        :disabled="!isNewIncident"
        inputId="incident-id"
        @input="incident.id = $event as string"
      />

      <!-- input for situation -->
      <Input
        label="Situation"
        :value="incident.situation"
        type="select"
        inputId="situation"
        :options="incidentSituationOptions"
        @input="incident.situation = $event as IncidentSituation"
      />

      <!-- input for status -->
      <Input
        label="Status"
        :value="incident.status"
        type="select"
        inputId="status"
        :options="incidentStatusOptions"
        @input="incident.status = $event as IncidentStatus"
      />

      <div class="grid grid-cols-2 gap-10">
        <Input
          label="Latitude"
          :value="incident.lat"
          type="number"
          placeholder="Latitude"
          inputId="latitude"
          @input="incident.lat = $event as number"
        />

        <Input
          label="Longitude"
          :value="incident.long"
          type="number"
          placeholder="Longitude"
          inputId="longitude"
          @input="incident.long = $event as number"
        />
      </div>
    </form>

    <div class="flex gap-5 mb-6">
      <template v-if="!isNewIncident">
        <Button @click="() => emit('submitSalvorRequest', incident)">Verstuur berger</Button>
        <Button variant="destructive" @click="handeClear">Annuleren</Button>
      </template>
      <template v-else>
        <Button @click="handleSubmit">Incident aanmaken</Button>
      </template>
    </div>

    <div>
      <div v-if="incident.requests">
        <Heading level="2">Requests</Heading>
        <div v-for="request in incident.requests" :key="request.id">
          <p>ID: {{ request.id }}</p>
          <p>Berger: {{ request.salvorName }}</p>
          <p>Status: {{ request.status }}</p>
        </div>
      </div>
      <div v-if="incident.segment"></div>
    </div>
  </div>
</template>
