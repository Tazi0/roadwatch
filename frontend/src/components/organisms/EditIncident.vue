<script setup lang="ts">
import { IncidentSituation, IncidentStatus, type Incident } from '@/types/api'
import { defineProps, ref, type PropType } from 'vue'
import Input from '@/components/atoms/Input.vue'
import Heading from '@/components/atoms/Heading.vue'
import Button from '@/components/atoms/Button.vue'

const emit = defineEmits<{
  (e: 'update', value: Incident): void
  (e: 'submitSalvorRequest', value: Incident): void
}>()

const props = defineProps({
  incident: {
    type: Object as PropType<Incident>,
    required: true,
  },
})

const incident = ref(props.incident)

const incidentSituationOptions = [
  { value: IncidentSituation.VehicleObstruction, label: 'Vehicle Obstruction' },
  { value: IncidentSituation.Accident, label: 'Accident' },
]

const incidentStatusOptions = [
  { value: IncidentStatus.Reported, label: 'Reported' },
  { value: IncidentStatus.Completed, label: 'Completed' },
  { value: IncidentStatus.Failed, label: 'Failed', disabled: true },
  { value: IncidentStatus.Dispatched, label: 'Dispatched', disabled: true },
  { value: IncidentStatus.Searching, label: 'Searching', disabled: true },
]

function handleSubmit(event: Event) {
  event.preventDefault()
  emit('update', props.incident)
}
</script>

<template>
  <div>
    <Heading level="1">Edit Incident</Heading>

    <form class="flex flex-col gap-3">
      <Input
        label="Incident ID"
        :value="incident.id"
        type="text"
        placeholder="Incident ID"
        required
        disabled
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
      <Button type="button" theme="primary" @click="() => emit('submitSalvorRequest', incident)">
        Verstuur berger
      </Button>
      <Button type="submit" theme="secondary" @click="handleSubmit">Wijzigingen opslaan</Button>
    </div>
  </div>
</template>
