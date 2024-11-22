<script setup lang="ts">
import { RouterLink } from 'vue-router'
import Rounded from '@/components/atoms/Rounded.vue'
import Logo from '@/assets/logo.svg?component'
</script>

<template>
    <aside class="border-r border-black dark:border-gray-300 p-3">
        <RouterLink to="/"><Logo /></RouterLink>
        <div class="grid grid-cols-1 gap-2">
            <Rounded>
                <p>Incident</p>
            </Rounded>
            <Rounded>
                <p>Incident</p>
            </Rounded>
        </div>
    </aside>
</template>