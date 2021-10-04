import Vue from "vue";
import Vuex from "vuex";

import Axios from "@/plugins/axios";

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    name: "",
    current_speaker: "",
    lists: [[], []]
  },
  mutations: {
    setName(state, {name, number}) {
      state.name = name;
      state.number = number;

    },
    setList(state, lists) {
      state.lists = lists;
    },
  },
  actions: {
    addSpeaker({ commit }, speaker) {
      return new Promise((resolve, reject) => {
        Axios({ url: "/speaker/add/" + JSON.stringify(speaker), method: "POST"})
          .then(resp => {
            commit("setName", speaker);
            resolve(resp);
          })
          .catch(err => {
            reject(err);
          });
      });
    },
    updateLists({ commit }) {
      return new Promise((resolve, reject) => {
        Axios({ url: "/list", method: "GET" })
          .then(resp => {
            commit("setList", resp.data);
            resolve(resp);
          })
          .catch(err => {
            reject(err);
          });
      });
    },
    nextSpeaker() {
      return new Promise((resolve, reject) => {
        Axios({ url: "/list/next", method: "POST" })
          .then(resp => {
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
