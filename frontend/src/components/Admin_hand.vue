<template>
    <v-container>
      <v-sheet>
      <v-card>
        <v-card-title> Raise someone elses hand </v-card-title>
        <v-form @submit.prevent="raiseHand()">
        <v-card-text>
          <v-text-field v-model="speaker" label="Name or number" required placeholder="Name or number" />
        </v-card-text>
        <v-card-actions>
          <v-btn class="primary" @click="raiseHand()" type="submit"> Raise their hand </v-btn>
          <v-btn class="primary" @click="lowerHand()"> Lower their hand </v-btn>
        </v-card-actions>
        </v-form>
    </v-card>
    </v-sheet>
    </v-container>
</template>

<script>
import Axios from "@/plugins/axios"

export default {
  data() { 
    return {
      speaker: ""
    }
  },
  methods: {
    lowerHand() {
      return new Promise((resolve, reject) => {
        Axios({ url: "/list/remove/" + this.speaker, method: "POST" })
          .then(resp => {
            resolve(resp);
            this.speaker = ""
          })
          .catch(err => {
            alert("Something went wrong. You probably already raised your hand. \n\n" + err);
            // Give feedback
            reject(err);
            this.speaker = ""
          });
      });
    },
    raiseHand() {
      return new Promise((resolve, reject) => {
        Axios({ url: "/list/add/" + this.speaker, method: "POST" })
          .then(resp => {
            resolve(resp);
            this.speaker = ""
          })
          .catch(err => {
            alert("Something went wrong. You probably already raised your hand. \n\n" + err);
            // Give feedback
            reject(err);
            this.speaker = ""
          });
      });
    },
  }
}
</script>
