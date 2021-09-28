import Vue from "vue";
import Vuex from "vuex";

import Axios from "@/plugins/axios";

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    name: ""
  },
  mutations: {
    setName(state, name) {
      state.name = name;
    }
  },
  actions: {
    addSpeaker({ commit }, name) {
      return new Promise((resolve, reject) => {
        Axios({ url: "/speaker/add/" + name, method: "POST" })
          .then(resp => {
            console.log(resp);
            commit("setName", name);
            resolve(resp);
          })
          .catch(err => {
            reject(err);
          });
      });
    }
  },
  getters: {},
  modules: {}
});
