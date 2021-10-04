<template>
  <v-container>
    <v-card class="mx-auto" width="500">
      <v-card-title class="text-center">Speaker Managent</v-card-title>
      <v-card-text>
        <v-form @submit.prevent="btnClick()">
            <v-text-field v-model="name" label="Name" required placeholder="Name" />
            <v-text-field v-model="number" :rules="numberRules" label="Number" required placeholder="0" />
          <v-btn class="primary" type="submit"> Submit </v-btn>
        </v-form>
      </v-card-text>
    </v-card>
  </v-container>
</template>

<script>
export default {
  name: "SpeakerMangement",
  data() {
    return { 
      name: "", 
      number: "",
      checked: false,
      numberRules: [v => { if(!v.trim()) return true; if(!isNaN(parseInt(v)) && v >= 0) return true; return "Has to be a positive number"; }],
    };
  },
  components: {},
  methods: {
    btnClick() {
      this.btn_loader = true;
      this.$store
        .dispatch("addSpeaker", { name: this.name, number: this.number })
        .then(() => {
          this.btn_loader = false;
          this.$router.push("Meeting");
        })
        .catch(() => {
          this.btn_loader = false;
        });
    }
  }
};
</script>
