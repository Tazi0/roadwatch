<script setup lang="ts">
import ErrorMessage from '@/components/atoms/ErrorMessage.vue'
import LoadingCircle from '@/components/atoms/LoadingCircle.vue'
import Analytics from '@/components/organisms/Analytics.vue'
import EditIncident from '@/components/organisms/EditIncident.vue'
import { Tabs, TabsContent, TabsList, TabsTrigger } from '@/components/ui/tabs'
import { getIncidents } from '@/gateway/api'
import { useIncidentsStore } from '@/stores/incidents'

const store = useIncidentsStore()

store.loading = true
getIncidents()
  .then((incidents) => {
    store.set(incidents)
    store.loading = false
  })
  .catch((error) => {
    store.setError(error)
  })
</script>

<template>
  <main>
    <template v-if="store.loading">
      <LoadingCircle class="min-h-[inherit]" message="Bezig met het laden van de incidenten" />
    </template>
    <template v-else-if="store.error">
      <ErrorMessage class="min-h-[inherit]" message="Er ging iets fout" :error="store.error" />
    </template>
    <template v-else>
      <Tabs default-value="analytics" class="py-5">
        <TabsList class="mx-auto">
          <TabsTrigger value="map">Globale map</TabsTrigger>
          <TabsTrigger value="edit"
            >{{ store.selected ? 'Bewerk' : 'Creeër' }} Incident</TabsTrigger
          >
          <TabsTrigger value="analytics">Analytics</TabsTrigger>
        </TabsList>
        <TabsContent value="map">
          <p>Map</p>
        </TabsContent>
        <TabsContent value="edit">
          <!-- TODO: update to submit patch to api (wss met watch) -->
          <EditIncident
            :incident="store.selected"
            auto-update
            @create="(incident) => console.log(incident)"
            @update="(incident) => console.log(incident)"
            @submitSalvorRequest="(incident) => console.log(incident)"
          />
        </TabsContent>
        <TabsContent value="analytics">
          <Analytics :incidents="store.incidents" />
        </TabsContent>
      </Tabs>
    </template>
  </main>
</template>
