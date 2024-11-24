<script setup lang="ts">
import { RequestStatus, type Incident } from '@/types/api'
import { type PropType } from 'vue'
import Card from '@/components/atoms/Card.vue'

defineProps({
  incidents: {
    type: Object as PropType<Incident[]>,
    required: true,
  },
})
</script>

<template>
  <div class="grid grid-cols-6 grid-rows-6 gap-5 aspect-square">
    <Card class="col-span-2 row-span-2">
      <p>Total incidents this week</p>
      <p>{{ incidents.length }}</p>
    </Card>
    <Card class="col-span-2 row-span-2">
      <p>Berger Geaccepteerd</p>
      <p>
        {{
          incidents.filter((v) => v.requests?.some((r) => r.status === RequestStatus.Accepted))
            .length / incidents.length
        }}
        %
      </p>
    </Card>
    <Card class="col-span-1 row-span-1">
      <p>Incidents today</p>
      <p>{{ incidents.length }}</p>
    </Card>
  </div>
</template>
