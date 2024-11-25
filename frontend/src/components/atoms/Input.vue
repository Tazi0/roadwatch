<script setup lang="ts">
import { defineProps, defineEmits } from 'vue'

const props = defineProps<{
  value?: string | number
  type: string
  placeholder?: string
  disabled?: boolean
  label: string
  inputClass?: string
  inputId: string
  required?: boolean
  options?: { value: string; label: string; disabled?: boolean }[]
}>()

defineEmits<{
  (e: 'input', value: string | number): void
}>()

const parentClasses = ['flex flex-col'].filter(Boolean).join(' ')

const classes = [
  'p-2 border border-gray-300 bg-gray-100 dark:bg-gray-800 rounded',
  props.disabled && 'cursor-not-allowed opacity-50',
  props.inputClass,
]
  .filter(Boolean)
  .join(' ')
</script>

<template>
  <div :class="parentClasses">
    <label v-if="label" :for="inputId">{{ label }}</label>
    <template v-if="type === 'select'">
      <select
        :id="inputId"
        :value="value"
        :disabled="disabled"
        @input="!disabled ? $emit('input', ($event.target as HTMLSelectElement).value) : null"
        :class="classes"
        :required="required"
      >
        <option value="" v-if="placeholder" disabled>{{ placeholder }}</option>
        <option
          v-for="option in options"
          :key="option.value"
          :value="option.value"
          :selected="option.value === value"
          :disabled="option.disabled"
        >
          {{ option.label }}
        </option>
      </select>
    </template>
    <input
      v-else
      :id="inputId"
      :type="type"
      :value="value"
      :placeholder="placeholder"
      :disabled="disabled"
      @input="$emit('input', ($event.target as HTMLInputElement).value)"
      :class="classes"
      :required="required"
    />
  </div>
</template>
