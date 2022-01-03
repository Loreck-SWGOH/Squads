<template>
    <v-text-field class="shrink ma-2" prefix="Ally Code"
        single-line outlined counter=11 maxlength=11
        v-model="allyCodeNum">
        <template slot="append-outer">
            <span> Welcome {{name}} </span>
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
                name: 'Loreck Avery'
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