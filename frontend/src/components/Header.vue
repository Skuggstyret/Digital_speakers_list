<template>
  <v-app-bar app color="white" dark>
    <v-spacer></v-spacer>
    <router-link to="/meeting">
      <v-btn class="primary--text" text>
        <span class="mr-2">Meeting</span>
      </v-btn>
    </router-link>
    <router-link to="/list">
      <v-btn class="primary--text" text>
        <span class="mr-2">Speakers List</span>
      </v-btn>
    </router-link>

    <router-link to="/speaker">
      <v-btn class="primary--text" text>
        <span class="mr-2">Speaker Managent</span>
      </v-btn>
    </router-link>

    <v-spacer></v-spacer>
    <v-btn class="primary--text" text>
      <span class="mr-2"> {{ this.$store.state.number }} {{ this.$store.state.name }} </span>
    </v-btn>
  </v-app-bar>
</template>
