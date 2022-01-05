<!-- The Ally Code consists of an input and displays the associated name -->
<template>
    <v-text-field class="shrink text-sm-h6"
        prefix="Ally Code" single-line outlined
        counter=11 maxlength=11
        append-icon="mdi-magnify" v-model="allyCodeNum">
        <template v-slot:append-outer>
            <v-btn class="text-sm-h6" depressed plain> {{allyName}} </v-btn>
        </template>
    </v-text-field>
</template>

<script>
    export default {
        // Name of component
        name: 'AllyCode',

        // Components used
        components: {
        },

        // Local data
        data () {
            return {
                allyCodeNum: '',
            }
        },

        computed: {
            allyName() {
                return 'Welcome Loreck Avery'
            }
        },

        watch: {
            allyCodeNum() {
                // Ally code without dash (-)
                let realNumber = this.allyCodeNum.replace(/-/gi, '')
        
                // Generate dashed number
                let dashedNumber = realNumber.match(/.{1,3}/g)

                // Replace dashed number with real one
                this.allyCodeNum = dashedNumber.join('-')
            }
        }
    }
</script>