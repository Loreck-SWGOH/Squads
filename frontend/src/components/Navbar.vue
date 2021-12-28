<template>
    <v-tabs>
        <v-tab v-for="tab in tabs" :key="tab.title">
            {{tab.title}}
        </v-tab>

        <v-tab-item v-for="tab in tabs" :key="tab.comp">
            <component :is="tab.comp"> </component>
        </v-tab-item>
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
                tabs: [
                    { title: 'Team Database', comp: ModDBApp },
                    { title: 'Team Mods', comp: TeamModApp },
                    { title: 'Defense Mods', comp: DefModApp},
                ]
            }
        },
    }
</script>