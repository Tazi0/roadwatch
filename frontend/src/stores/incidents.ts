import { ref } from 'vue'
import { defineStore } from 'pinia'
import type { Incident } from '@/types/api'

export const useIncidentsStore = defineStore('incidents', () => {
  const incidents = ref<Incident[]>([])
  const selectedIncident = ref<Incident | null>(null)
  
  function set(newIncidents: Incident[]) {
    incidents.value = newIncidents
  }
  function add(incident: Incident) {
    incidents.value.push(incident)
  }

  function select(incident: Incident) {
    selectedIncident.value = incident
  }
  function unselect() {
    selectedIncident.value = null
  }

  return { incidents, selectedIncident, set, add, select, unselect }
})