<template>
  <v-container>
    <add-speaker />
  </v-container>
</template>

<script>
// @ is an alias to /src
import AddSpeaker from "../components/AddSpeaker.vue";

export default {
  name: "Home",
  components: { AddSpeaker }
};
</script>
