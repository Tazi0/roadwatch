<script setup lang="ts">
import { RouterLink } from 'vue-router'
import Logo from '@/assets/logo.svg?component'
import { useIncidentsStore } from '@/stores/incidents';
import IncidentCard from '@/components/molecules/IncidentCard.vue';
import { IncidentStatus, type Incident } from '@/types/api';
import Heading from '@/components/atoms/Heading.vue';
import { ref, watch } from 'vue';

const { incidents } = useIncidentsStore();

const filter = (incident: Incident) => incident.status !== IncidentStatus.Completed;

const activeIncidents = ref(incidents.filter(filter));

watch(incidents, (newIncidents) => {
    activeIncidents.value = newIncidents.filter(filter);
});

</script>

<template>
    <aside class="border-r border-black dark:border-gray-300 p-3">
        <RouterLink to="/"><Logo /></RouterLink>
        <br />
        
        <Heading level="4">Actieve Incidenten</Heading>
        <div class="grid grid-cols-1 gap-2">
            <IncidentCard v-for="(incident, i) in activeIncidents" :key="i" :incident="incident" />
        </div>
    </aside>
</template>