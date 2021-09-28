<template>
  <v-container>
    <v-card class="mx-auto" width="500">
      <v-card-title class="text-center">Speaker Managent</v-card-title>
      <v-card-text>
        <v-form @submit.prevent="btnClick()">
          <div>
            <v-text-field v-model="name" required placeholder="Name" />
            <input type="checkbox" id="checkbox" v-model="checked" /> Create new
            speaker
          </div>
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
    return { name: "", checked: false };
  },
  components: {},
  methods: {
    btnClick() {
      this.btn_loader = true;
      if (this.checked) {
        this.$store
          .dispatch("addSpeaker", this.name)
          .then(() => {
            this.btn_loader = false;
          })
          .catch(() => {
            this.btn_loader = false;
          });
      } else {
        this.$store.state.name = this.name;
      }
    }
  }
};
</script>
