<!-- Toolbar with a place to enter the Ally Code and a set of tabs -->
<template>
    <v-toolbar tabs class="ma-4" flat>
        <AllyCode />

        <v-tabs slot="extension">
            <v-tab v-for="tab in tabs" :key="tab">
                {{tab.title}}
            </v-tab>

            <v-tab-item v-for="tab in tabs" :key="tab">
                <component :is="tab.comp"> </component>
            </v-tab-item>
        </v-tabs>
    </v-toolbar>
</template>

<script>
    import AllyCode from '@/components/AllyCode'
    import DesiredModApp from '@/components/DesiredModApp'
    import TeamModApp from '@/components/TeamModApp'
    import DefenseModApp from '@/components/DefenseModApp'

    export default {
        // Component name
        name: 'NavTabs',

        // Components used
        components: {
          AllyCode, 
          DesiredModApp,
          TeamModApp,
          DefenseModApp
        },

        // Internal data
        data () {
            return {
                // Entries dictate order of tabs
                tabs: [
                    { title: 'Team Database', comp: DesiredModApp },
                    { title: 'Team Mods', comp: TeamModApp },
                    { title: 'Defense Mods', comp: DefenseModApp},
                ],
            }
        },
    }
</script>