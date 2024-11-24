<script setup lang="ts">
import { defineProps, defineEmits } from 'vue'

const props = defineProps({
  type: {
    type: String as () => 'button' | 'submit' | 'reset',
    default: 'button',
  },
  theme: {
    type: String as () => 'primary' | 'secondary' | 'danger',
    default: 'primary',
  },
  size: {
    type: String as () => 'small' | 'medium' | 'large',
    default: 'medium',
  },
  disabled: {
    type: Boolean,
    default: false,
  },
})

const emit = defineEmits(['click'])

const handleClick = (event: Event) => {
  if (props.disabled) return
  emit('click', event)
}

const classes = [
  'transition',
  'rounded',
  'text-white',
  'focus:outline-none',
  props.size === 'small' ? 'text-xs py-2 px-4' : '',
  props.size === 'medium' ? 'text-sm py-3 px-6' : '',
  props.size === 'large' ? 'text-lg py-4 px-8' : '',
  props.disabled ? 'opacity-60 cursor-not-allowed' : 'hover:bg-opacity-75',
  props.theme === 'primary' ? 'bg-blue-500 hover:bg-blue-600' : '',
  props.theme === 'secondary' ? 'bg-gray-500 hover:bg-gray-600' : '',
  props.theme === 'danger' ? 'bg-red-500 hover:bg-red-600' : '',
]
  .filter(Boolean)
  .join(' ')
</script>

<template>
  <button :type="type" :class="classes" @click="handleClick">
    <slot></slot>
  </button>
</template>
