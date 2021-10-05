<template>
  <v-container>
    <interface :admin="true"/>
    <Admin_hand />
  </v-container>
</template>

<script>
import Interface from "@/components/Interface";
import Admin_hand from "@/components/Admin_hand";

export default {
  name: "Admin",
  components: {
    Interface,
    Admin_hand
  },
  data() {
    return {
    };
  }
}

</script>
