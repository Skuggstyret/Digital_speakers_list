<template>
  <v-container>
    <v-card class="mx-auto" width="500">
      <v-card-title class="text-center">Speakers List</v-card-title>
      <div id="row">
        <div>
          <h2>First list</h2>
          <ul>
            <li v-for="item in items[0]" :key="item.message">
              {{ item }}
            </li>
          </ul>
        </div>
        <div>
          <h2>Second list</h2>
          <ul>
            <li v-for="item in items[1]" :key="item.message">
              {{ item }}
            </li>
          </ul>
        </div>
      </div>
    </v-card>
  </v-container>
</template>

<script>
export default {
  name: "List",
  data() {
    return {
      items: [[], []],
      timer: ""
    };
  },
  created() {
    this.fetchEventsList();
    this.timer = setInterval(this.fetchEventsList, 5000);
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
#row {
  display: flex;
}

#row > div {
  width: 50%;
  padding: 5px;
}

ul {
  list-style: none;
  padding: 0;
  box-shadow: 0px 1px 5px #aaa;
}
li {
  padding: 10px;
}
li:nth-child(odd) {
  background: white;
}
</style>
