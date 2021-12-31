<template>
    <v-text-field class="shrink ma-2" prefix="Ally Code"
        single-line outlined counter=11
        v-model="allyCodeNum"></v-text-field>
</template>

<script>
    export default {
        // What is this component
        name: 'AllyCode',

        // What components does this use
        components: {
        },

        // What kind of data is needed internally
        data () {
            return {
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