<script setup lang="ts">
import { defineProps, type PropType } from 'vue'

const props = defineProps({
  level: {
    type: String as PropType<'1' | '2' | '3' | '4' | '5'>,
    required: true,
  },
})

const classes = [
  props.level === '1' && 'text-4xl font-bold',
  props.level === '2' && 'text-3xl font-bold',
  props.level === '3' && 'text-2xl',
  props.level === '4' && 'text-xl',
  props.level === '5' && 'text-lg',
]
  .filter(Boolean)
  .join(' ')

const element = `h${props.level}`
</script>

<template>
  <component :is="element" :class="classes">
    <slot></slot>
  </component>
</template>
