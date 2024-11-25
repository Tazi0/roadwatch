<script setup lang="ts">
import { PhSkull } from '@phosphor-icons/vue'

defineProps({
  message: {
    type: String,
    required: true,
  },
  error: {
    type: String,
    required: true,
  },
})
</script>

<template>
  <div class="flex flex-col gap-5 justify-center items-center">
    <PhSkull class="text-red-500 h-16 w-16" />
    <p>{{ message }}</p>
    <pre>{{ error }}</pre>
  </div>
</template>
