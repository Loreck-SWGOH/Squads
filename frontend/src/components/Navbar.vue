<template>
    <v-tabs>
        <v-tab v-for="item in items" :key="item">
            {{nameDict[item]}}
        </v-tab>

        <v-tab-item> <ModDBApp /> </v-tab-item>
        <v-tab-item> <TeamModApp /> </v-tab-item>

        <v-tab-item> <DefModApp /> </v-tab-item>
    </v-tabs>

</template>

<script>
  import ModDBApp from '@/components/ModDBApp'
  import TeamModApp from '@/components/TeamModApp'
  import DefModApp from '@/components/DefModApp'

    export default {
        name: 'NavBar',

        components: {
          ModDBApp,
          TeamModApp,
          DefModApp
        },

        data () {
            return {
                items: ['db', 'teammod', 'defmod'],
                nameDict: { 'db': 'Team Database',
                            'teammod': 'Team Mods',
                            'defmod': 'Defense Mods'},
                vueDict: {  'db': <ModDBApp />,
                            'teammod': <TeamModApp />,
                            'defmod': <DefModApp />},
            }
        },
    }
</script>