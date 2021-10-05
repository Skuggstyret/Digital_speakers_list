<template>
  <v-container>
    <NestedList :list_depth="list_depth" :items="items"/>
  </v-container>
</template>

<script>
import NestedList from "@/components/Nested_list.vue"

export default {
  name: "List",
  components: {
    NestedList
  },
  data() {
    return {
      items: [[]],
      list_depth: 0,
      timer: ""
    };
  },
  created() {
    this.fetchEventsList();
    this.timer = setInterval(this.fetchEventsList, 1000);
  },
  methods: {
    fetchEventsList() {
      this.$store.dispatch("updateLists");
      this.items = this.$store.state.lists;
    },
    cancelAutoUpdate() {
      clearInterval(this.timer);
    }
  },
  beforeDestroy() {
    this.cancelAutoUpdate();
  }
};
</script>

<style scoped>
</style>
