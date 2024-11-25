<script setup lang="ts">
import { IncidentSituation, IncidentStatus, type Incident } from '@/types/api'
import { defineProps, watch, type PropType } from 'vue'
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
let incident = props.incident || ({} as Incident)

if (props.autoUpdate) {
  if (store.selected) {
    incident = store.selected
  }

  watch(store, (newStore) => {
    if (newStore.selected) {
      incident = newStore.selected
      oldIncident = newStore.selected
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
  emit('create', incident)
  oldIncident = incident
}

function handeClear() {
  incident = {} as Incident
  oldIncident = {} as Incident
}
</script>

<template>
  <div>
    <Heading level="1" v-if="oldIncident.id">Edit Incident</Heading>
    <Heading level="1" v-else>Creeër Incident</Heading>

    <form class="flex flex-col gap-3">
      <Input
        label="Incident ID"
        :value="incident.id"
        type="text"
        placeholder="Incident ID"
        required
        :disabled="!!oldIncident.id"
        inputId="incident-id"
        @input="incident.id = $event as string"
      />

      <!-- input for situation -->
      <Input
        label="Situation"
        :value="incident.situation"
        type="select"
        placeholder="Situation"
        inputId="situation"
        :options="incidentSituationOptions"
        @input="incident.situation = $event as IncidentSituation"
      />

      <!-- input for status -->
      <Input
        label="Status"
        :value="incident.status"
        type="select"
        placeholder="Status"
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

    <div class="flex gap-5 mt-6">
      <template v-if="oldIncident.id">
        <Button type="button" @click="() => emit('submitSalvorRequest', incident)">
          Verstuur berger
        </Button>
        <Button type="button" variant="destructive" @click="handeClear">Schoonmaken</Button>
      </template>
      <template v-else>
        <Button type="submit" @click="handleSubmit">Incident aanmaken</Button>
      </template>
    </div>
  </div>
</template>
