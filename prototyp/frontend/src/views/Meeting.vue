<template>
  <v-container grid-list-md text-xs-center>
    <v-layout row wrap>
      <v-flex> <List /> </v-flex>
      <v-flex> <Interface /></v-flex>
    </v-layout>
  </v-container>
</template>

<script>
// @ is an alias to /src
// Display current speaker
import List from "@/components/List.vue";
import Interface from "@/components/Interface.vue";
export default {
  name: "Meeting",
  components: { List, Interface }
};
</script>
