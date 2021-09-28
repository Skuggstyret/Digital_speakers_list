<template>
  <v-container>
    <v-card class="mx-auto" width="150">
      <div>
        <v-btn v-on:click="raiseHand()"> Raise hand </v-btn>
      </div>
      <div>
        <v-btn v-on:click="nextSpeaker()"> Next </v-btn>
      </div>
      <div>
        <v-btn v-on:click="resetList()"> Reset list </v-btn>
      </div>
    </v-card>
  </v-container>
</template>

<script>
import Axios from "@/plugins/axios";
export default {
  name: "Interface",
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
          Axios({ url: "/list/add/" + this.$store.state.name, method: "POST" })
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
    },
    nextSpeaker() {
      this.btn_loader = true;
      this.$store
        .dispatch("nextSpeaker")
        .then(() => {
          this.btn_loader = false;
        })
        .catch(() => {
          this.btn_loader = false;
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
    }
  }
};
</script>
