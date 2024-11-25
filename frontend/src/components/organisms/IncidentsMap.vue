<script setup lang="ts">
import Map from '@/components/atoms/Map.vue'
import { useIncidentsStore } from '@/stores/incidents'
import type { Incident } from '@/types/api'
import { ref, type PropType } from 'vue'

const store = useIncidentsStore()

const props = defineProps({
  incidents: {
    type: Object as PropType<Incident[]>,
    required: true,
  },
})

const markers = ref<{ id: string; lat: number; lng: number }[]>(
  props.incidents.map((v) => ({
    id: v.id,
    lat: v.lat,
    lng: v.long,
  })),
)

function handleMarkerClick(id: string) {
  const incident = props.incidents.find((v) => v.id === id)
  if (!incident) return
  store.select(incident)
}
</script>

<template>
  <Map :markers="markers" @marker-clicked="handleMarkerClick" />
</template>
