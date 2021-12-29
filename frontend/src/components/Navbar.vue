<template>
    <v-toolbar tabs class="ma-4" flat>
        <v-text-field class="shrink ma-2" prefix="Ally Code"
            single-line outlined counter=11
            v-model="allyCodeNum"></v-text-field>

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
                ],

                allyCodeNum: ''
            }
        },

        watch: {
            allyCodeNum() {
                // Card number without dash (-)
                let realNumber = this.allyCodeNum.replace(/-/gi, '')
        
                // Generate dashed number
                let dashedNumber = realNumber.match(/.{1,3}/g)

                // Replace the dashed number with the real one
                this.allyCodeNum = dashedNumber.join('-')                
            }
        }
    }
</script>