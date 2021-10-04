<template>
  <v-container>
    <v-row>
      <v-col cols="">
        <List />
      </v-col>
      <v-col cols="3">
        <Interface />
      </v-col>
    </v-row>
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
