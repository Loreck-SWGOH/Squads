<template>
    <v-tabs>
        <v-tab ripple> Team Database </v-tab>
        <v-tab-item> <ModDBApp /> </v-tab-item>

        <v-tab ripple> Team Mods </v-tab>
        <v-tab-item> <TeamModApp /> </v-tab-item>

        <v-tab ripple> Defense Mods </v-tab>
        <v-tab-item> <DefModApp /> </v-tab-item>
    </v-tabs>

</template>

<script>
  import ModDBApp from '@/components/ModDBApp'
  import TeamModApp from '@/components/TeamModApp'
  import DefModApp from '@/components/DefModApp'

export default {
    name: 'Navbar',

    components: {
      ModDBApp,
      TeamModApp,
      DefModApp
    },
    
}
</script>