<script setup lang="ts">
import 'leaflet/dist/leaflet.css'
import leaflet from 'leaflet'
import { onMounted, type PropType } from 'vue'

const props = defineProps({
  markers: {
    type: Array as PropType<{ lat: number; lng: number }[]>,
    required: true,
  },
  zoom: {
    type: Number,
    default: 26,
    required: false,
  },
  width: {
    type: Number,
    default: 600,
    required: false,
  },
  height: {
    type: Number,
    default: 600,
    required: false,
  },
})

let map: leaflet.Map
const mapId = 'map-' + Math.random().toString(36).substring(2, 9)

onMounted(() => {
  map = leaflet.map(mapId, {
    zoom: props.zoom,
    preferCanvas: true,
  })

  const bounds = leaflet.latLngBounds(props.markers.map((marker) => [marker.lat, marker.lng]))
  map.fitBounds(bounds)

  leaflet
    .tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
      attribution:
        '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
    })
    .addTo(map)

  props.markers.forEach((marker) => {
    leaflet.marker([marker.lat, marker.lng]).addTo(map)
  })
})
</script>

<template>
  <div :id="mapId" style="width: 100%; min-height: 600px"></div>
</template>
