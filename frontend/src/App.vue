<template>
<!-- v-app is root component -->
  <v-app>
    <v-app-bar app color="primary" dark>
      <span class="display-1"> SWGOH Modding </span>

    <!-- push items to far left and far right -->
      <v-spacer></v-spacer>

      <v-btn
        href="https://github.com/Loreck-SWGOH/Squads"
        target="_blank"
        text
      >
        <span class="mr-2">Latest Release</span>
        <v-icon>mdi-open-in-new</v-icon>
      </v-btn>
    </v-app-bar>

  <!-- route /about to About.vue, etc -->
    <v-main>
      <router-view> </router-view>
    </v-main>
  </v-app>
</template>

<script>

export default {
  name: 'App',

  data: () => ({
    //
  }),
};
</script>
