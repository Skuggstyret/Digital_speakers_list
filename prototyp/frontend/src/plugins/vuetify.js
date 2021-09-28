import Vue from "vue";
import Vuetify from "vuetify/lib/framework";

Vue.use(Vuetify);

export default new Vuetify({
  theme: {
    options: {
      customProperties: true
    },
    themes: {
      light: {
        primary: "#d60000",
        secondary: "#9c0000",
        accent: "#82B1FF", //default
        error: "#d60000",
        info: "#2196F3", //default
        success: "#00D600",
        warning: "#D6D600"
      }
    }
  },
  icons: {
    iconfont: "mdi"
  }
});
