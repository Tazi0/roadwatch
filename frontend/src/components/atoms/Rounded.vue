<script setup lang="ts">
import { defineProps } from 'vue'

const props = defineProps({
  href: {
    type: String,
    required: false,
  },
})

const element = props.href ? 'a' : 'div'
</script>

<template>
  <component :is="element" class="rounded-md bg-slate-200 dark:bg-slate-800 py-2 px-3 no-underline">
    <slot></slot>
  </component>
</template>
