<script setup lang="ts">

import Tag from '@/components/atoms/Tag.vue';
import { IncidentStatus, type Incident } from '@/types/api';
import { defineProps, type PropType } from 'vue';

const props = defineProps({
    incident: {
        type: Object as PropType<Incident>,
        required: true,
    },
});

const getTagColor = (status: string) => {
    switch (status) {
        case IncidentStatus.Reported:
            return 'gray';
        case IncidentStatus.Completed:
            return 'green';
        case IncidentStatus.Failed:
            return 'red';
        case IncidentStatus.Dispatched:
            return 'blue';
        case IncidentStatus.Searching:
            return 'orange';
        default:
            return 'gray';
    }
}

const tagColor = getTagColor(props.incident.status);

</script>

<template>
    <Tag :type="tagColor">{{ incident.status.toLowerCase() }}</Tag>
</template>