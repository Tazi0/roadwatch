<script setup lang="ts">
defineProps({
  message: {
    type: String,
    required: false,
  },
})
</script>

<template>
  <div class="flex flex-col gap-5 justify-center items-center">
    <div class="animate-spin rounded-full h-16 w-16 border-t-4 border-blue-500"></div>
    <p v-if="message">{{ message }}</p>
  </div>
</template>
