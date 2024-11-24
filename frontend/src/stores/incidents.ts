import { ref } from 'vue'
import { defineStore } from 'pinia'
import type { Incident } from '@/types/api'

export const useIncidentsStore = defineStore('incidents', () => {
  const incidents = ref<Incident[]>([])
  const selected = ref<Incident | null>(null)

  function set(newIncidents: Incident[]) {
    incidents.value = newIncidents
  }
  function add(incident: Incident) {
    incidents.value.push(incident)
  }

  function select(incident: Incident) {
    selected.value = incident
  }
  function unselect() {
    selected.value = null
  }

  return { incidents, selected, set, add, select, unselect }
})
