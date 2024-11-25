<script setup lang="ts">
import type { Incident } from '@/types/api'
import type { PropType } from 'vue'
import IncidentTag from '@/components/atoms/IncidentTag.vue'
import Button from '@/components/ui/button/Button.vue'

defineProps({
  incident: {
    type: Object as PropType<Incident>,
    required: true,
  },
})

const emit = defineEmits(['deselect'])
</script>

<template>
  <div class="grid grid-cols-12 gap-4">
    <div class="col-span-8">
      <!-- Title -->
      <template v-if="incident.segment">
        <p>{{ incident.segment.firstName }}</p>
        <p>{{ incident.segment.secondName }}</p>
      </template>
      <template v-else>
        <pre>{{ incident.id }}</pre>
      </template>
    </div>

    <div class="col-span-4">
      <div class="flex justify-between items-center">
        <IncidentTag :incident="incident" />
        <Button variant="outline" :onclick="() => emit('deselect')">Deselecteer</Button>
      </div>
      <p>Situatie: {{ incident.situation }}</p>
    </div>
  </div>
</template>
