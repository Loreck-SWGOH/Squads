<template>
    <v-toolbar tabs>
        <v-text-field class="shrink mx-4" prefix="Ally Code"
            single-line outlined counter=9></v-text-field>
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
    import ModDBApp from '@/components/ModDBApp'
    import TeamModApp from '@/components/TeamModApp'
    import DefModApp from '@/components/DefModApp'

    export default {
        // What is this component
        name: 'NavBar',

        // What components does this use
        components: {
          ModDBApp,
          TeamModApp,
          DefModApp
        },

        // What kind of data is needed internally
        data () {
            return {
                // Entries dictate order of tabs
                tabs: [
                    { title: 'Team Database', comp: ModDBApp },
                    { title: 'Team Mods', comp: TeamModApp },
                    { title: 'Defense Mods', comp: DefModApp},
                ]
            }
        },
    }
</script>