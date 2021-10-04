<template>
  <v-app>
    <Header />
    <v-main>
      <router-view />
    </v-main>
  </v-app>
</template>

<script>
import Header from "@/components/Header.vue";

export default {
  name: "App",
  components: {
    Header
  },

  data: () => ({})
};
</script>

<style>
a {
  text-decoration: none;
}

.v-application--wrap {
  background-color: grey;
}
</style>
