<script setup lang="ts">
import { defineProps, type PropType } from 'vue';

const props = defineProps({
    type: {
        type: String as PropType<'gray' | 'green' | 'red' | 'blue' | 'orange'>,
        default: 'gray',
    },
});

const classes = [
    'inline-block rounded-full px-3 py-1 text-sm font-semibold mr-2',
    props.type === 'gray' && 'bg-gray-200 text-gray-700',
    props.type === 'green' && 'bg-green-200 text-green-700',
    props.type === 'red' && 'bg-red-200 text-red-700',
    props.type === 'blue' && 'bg-blue-200 text-blue-700',
    props.type === 'orange' && 'bg-orange-200 text-orange-700',
].filter(Boolean).join(' ');
</script>

<template>
    <span :class="classes">
        <slot></slot>
    </span>
</template>