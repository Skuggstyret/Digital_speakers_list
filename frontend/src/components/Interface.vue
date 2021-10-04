<template>
  <v-container>
    <v-card>
      <v-list>
        <v-list-item>
          <v-btn v-on:click="raiseHand()"> Raise hand </v-btn>
        </v-list-item>
        <v-list-item>
          <v-btn v-on:click="lowerHand()"> Lower hand </v-btn>
        </v-list-item>
        <v-list-item v-if="admin">
          <v-btn v-on:click="nextSpeaker()"> Next </v-btn>
        </v-list-item>
        <v-list-item v-if="admin">
          <v-btn v-on:click="resetList()"> Reset list </v-btn>
        </v-list-item>
        <v-list-item v-if="admin">
          <v-btn v-on:click="addNestedList()"> Add nested list </v-btn>
        </v-list-item>
        <v-list-item v-if="admin">
          <v-btn v-on:click="removeNestedList()"> Remove nested list </v-btn>
        </v-list-item>
      </v-list>
    </v-card>
  </v-container>
</template>

<script>
import Axios from "@/plugins/axios";
export default {
  name: "Interface",
  props: ['admin'],
  data() {
    return { name: "", checked: false };
  },
  components: {},
  methods: {
    raiseHand() {
      if (this.$store.state.name == "") {
        // Need to select a speaker first
        alert("You need to pick a speaker before raising hand");
      } else {
        return new Promise((resolve, reject) => {
          Axios({ url: "/list/add/" + this.$store.state.number , method: "POST" })
            .then(resp => {
              resolve(resp);
            })
            .catch(err => {
              alert("Something went wrong. You probably already raised your hand. \n\n" + err);
              // Give feedback
              reject(err);
            });
        });
      }
    },
    lowerHand() {
      if (this.$store.state.name == "") {
        // Need to select a speaker first
        alert("You need to pick a speaker before raising hand");
      } else {
        return new Promise((resolve, reject) => {
          Axios({ url: "/list/remove/" + this.$store.state.number , method: "POST" })
            .then(resp => {
              resolve(resp);
            })
            .catch(err => {
              alert("Something went wrong. You probably already have your hand lowered. \n\n" + err);
              // Give feedback
              reject(err);
            });
        });
      }
    },
    nextSpeaker() {
      return new Promise((resolve, reject) => {
        Axios({ url: "/list/next", method: "POST" })
          .then(resp => {
            resolve(resp)
          })
          .catch(err => {
            alert("Something went wrong. \n\n" + err);
            reject(err)
          });
      });
    },
    resetList() {
      return new Promise((resolve, reject) => {
        Axios({ url: "/list/reset", method: "POST" })
          .then(resp => {
            resolve(resp);
          })
          .catch(err => {
            alert("Something went wrong" + err);
            // Give feedback
            reject(err);
          });
      });
    },
    addNestedList() {
      return new Promise((resolve, reject) => {
        Axios({ url: "/list/push", method: "POST" })
          .then(resp => {
            resolve(resp);
          })
          .catch(err => {
            alert("Something went wrong" + err);
            // Give feedback
            reject(err);
          });
      });
    },
    removeNestedList() {
      return new Promise((resolve, reject) => {
        Axios({ url: "/list/pop", method: "POST" })
          .then(resp => {
            resolve(resp);
          })
          .catch(err => {
            alert("Something went wrong" + err);
            // Give feedback
            reject(err);
          });
      });
    }
  }
};
</script>
