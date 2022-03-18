<template>
    <v-container>
        <ModDBIntro />
        <v-list>
        </v-list>
    </v-container>
</template>

<script>
    import ModDBIntro from '@/components/ModDBIntro'

    export default {
        // Component name
        name: 'DesiredModApp',
    
        components: {
            ModDBIntro,
        },

        // Local data
        data () {
            return {
//                introModDB: 'Lorem'
            }
        },

        computed: {
            introModDB() {
                var request = new XMLHttpRequest();
                request.open('GET', '../assets/ModDBIntro.txt', false);
                request.send();
                return request.responseText;
//                return 'Welcome ' + this.allyCodeName
            }
        },

    }
</script>