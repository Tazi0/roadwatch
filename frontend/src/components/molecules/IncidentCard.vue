<script setup lang="ts">
import Rounded from '@/components/atoms/Rounded.vue'
import { IncidentStatus, RequestStatus, type Incident } from '@/types/api'
import type { PropType } from 'vue'
import IncidentTag from '@/components/atoms/IncidentTag.vue'
import { useIncidentsStore } from '@/stores/incidents'
import { computed } from 'vue'

const props = defineProps({
  incident: {
    type: Object as PropType<Incident>,
    required: true,
  },
  active: {
    type: Boolean,
    required: false,
    default: false,
  },
})

const { select } = useIncidentsStore()

const confirmed = props.incident.requests?.find((r) => r.status === RequestStatus.Confirmed)

const onClick = () => {
  select(props.incident)
}

const classes = computed(() =>
  ['cursor-pointer border', props.active ? 'border-blue-500' : 'border-transparent']
    .filter(Boolean)
    .join(' '),
)
</script>

<template>
  <Rounded :class="classes" :onclick="onClick">
    <div class="flex justify-between">
      <p>{{ incident.segment?.roadNumber ?? incident.id }}</p>
      <IncidentTag :incident="incident" />
    </div>
    <p>{{ incident.situation.toLocaleLowerCase() }}</p>

    <template v-if="incident.requests && incident.status !== IncidentStatus.Completed">
      <p v-if="confirmed">'{{ confirmed.salvorName }}' onderweg</p>
      <p v-else-if="incident.requests.every((r) => r.status === RequestStatus.Denied)">
        Geen bergers beschikbaar
      </p>
      <p v-else-if="incident.requests.length > 0">Berger zoeken</p>
      <p v-else>Niet aan het zoeken</p>
    </template>
    <p v-else-if="incident.status === IncidentStatus.Completed">Berger klaar</p>
    <p v-else>Niet aan het zoeken</p>
  </Rounded>
</template>
