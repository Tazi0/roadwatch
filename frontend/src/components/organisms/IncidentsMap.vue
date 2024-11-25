<script setup lang="ts">
import Map from '@/components/atoms/Map.vue'
import type { Incident } from '@/types/api'
import { ref, type PropType } from 'vue'

const props = defineProps({
  incidents: {
    type: Object as PropType<Incident[]>,
    required: true,
  },
})

const markers = ref<{ lat: number; lng: number }[]>(
  props.incidents.map((v) => ({
    lat: v.lat,
    lng: v.long,
  })),
)
</script>

<template>
  <Map :markers="markers" />
</template>
