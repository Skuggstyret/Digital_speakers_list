<template>
  <v-card class="pa-2" elevation="6">
    <v-card-title>Speakers List</v-card-title>
    <NestedList v-if="list_depth < items.length - 1" :list_depth="list_depth + 1" :items="items"/>
    <v-list>
      <v-list-item v-for="item in items[list_depth]" :key="item.number"> {{ item.number }}: {{ item.name }} </v-list-item>
    </v-list>
  </v-card>
</template>

<script>
export default {
  name: "NestedList",
  props: ["items", "list_depth"]

}
</script>

