<script setup lang="ts">
import 'leaflet/dist/leaflet.css'
import leaflet, { type LatLngTuple } from 'leaflet'
import { onMounted, onUnmounted, watch, type PropType } from 'vue'

const props = defineProps({
  markers: {
    type: Array as PropType<{ id?: string; lat: number; lng: number }[]>,
    required: false,
  },
  zoom: {
    type: Number,
    default: 26,
    required: false,
  },
  width: {
    type: String,
    default: '100%',
    required: false,
  },
  minHeight: {
    type: String,
    default: '600px',
    required: false,
  },
})

const emit = defineEmits<{
  (e: 'markerClicked', value: string): void
}>()

let map: leaflet.Map
const mapId = 'map-' + Math.random().toString(36).substring(2, 9)

onMounted(() => {
  map = leaflet.map(mapId, {
    zoom: props.zoom,
    preferCanvas: true,
  })

  leaflet
    .tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
      attribution:
        '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
    })
    .addTo(map)

  // centralize on the netherlands if no markers are provided
  if (!props.markers) {
    setTimeout(() => {
      const center = leaflet.latLng(52.1326, 5.2913)
      map.fitBounds(leaflet.latLngBounds(center, center))
      map.zoomOut(10)
      map.invalidateSize()
    })
    return
  }

  // create markers
  const markers = props.markers.map((marker) => [marker.lat, marker.lng]) as LatLngTuple[]

  // wait for the map to be rendered
  // otherwise it would cause a bug centering the map on top left
  setTimeout(() => {
    const bounds = leaflet.latLngBounds(markers)
    map.fitBounds(bounds)
    map.invalidateSize()
  }, 0)

  markers.forEach((marker) => {
    leaflet
      .marker(marker)
      .addTo(map)
      .on('click', () => {
        const idOfMarker = props.markers!.find(
          (m) => m.lat === marker[0] && m.lng === marker[1],
        )?.id
        if (idOfMarker) emit('markerClicked', idOfMarker)
      })
  })
})

onUnmounted(() => {
  if (!map) return
  map.remove()
})

// watch for changes in markers
watch(
  () => props.markers,
  (newMarkers) => {
    if (!map) return
    // remove old markers
    map.eachLayer((layer) => {
      if (layer instanceof leaflet.Marker) {
        map.removeLayer(layer)
      }
    })

    if (!newMarkers) return

    const bounds = leaflet.latLngBounds(newMarkers.map((marker) => [marker.lat, marker.lng]))
    map.fitBounds(bounds)
    newMarkers.forEach((marker) => {
      leaflet.marker([marker.lat, marker.lng]).addTo(map)
    })
  },
)
</script>

<template>
  <div :id="mapId" class="z-0" :style="{ width, minHeight }"></div>
</template>
