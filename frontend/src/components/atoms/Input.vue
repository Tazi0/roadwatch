<script setup lang="ts">
import { Input } from '@/components/ui/input'
import {
  Select,
  SelectContent,
  SelectGroup,
  SelectItem,
  SelectLabel,
  SelectTrigger,
  SelectValue,
} from '@/components/ui/select'
import { Label } from '@/components/ui/label'
import { defineProps } from 'vue'

const props = defineProps<{
  type: string
  placeholder?: string
  disabled?: boolean
  label: string
  inputClass?: string
  inputId: string
  required?: boolean
  options?: { value: string; label: string; disabled?: boolean }[]
}>()

const model = defineModel<string | number | Date>()
</script>

<template>
  <div>
    <Label v-if="label" :for="inputId">{{ label }}</Label>
    <Select v-if="type === 'select'" v-model="model as string" :defaultValue="model as string">
      <SelectTrigger>
        <SelectValue v-if="model" :placeholder="options?.find((v) => v.value === model)?.label" />
      </SelectTrigger>
      <SelectContent class="z-50">
        <SelectGroup>
          <SelectLabel>Selecteer een optie</SelectLabel>
          <SelectItem
            v-for="option in options"
            :key="option.value"
            :value="option.value"
            :disabled="option.disabled"
          >
            {{ option.label }}
          </SelectItem>
        </SelectGroup>
      </SelectContent>
    </Select>

    <Input
      v-else
      v-model="model"
      :value="model instanceof Date ? model.toISOString().slice(0, 16) : model"
      :type="type"
      :placeholder="props.placeholder"
      :disabled="props.disabled"
      :id="props.inputId"
      :required="props.required"
      :options="props.options"
    />
  </div>
</template>
