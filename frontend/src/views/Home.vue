<template>
  <v-container> 
    <Speaker />
  </v-container>
</template>

<script>
// @ is an alias to /src
import Speaker from "@/components/Speaker.vue"

export default {
  name: "Home",
  components: { Speaker }
};
</script>
