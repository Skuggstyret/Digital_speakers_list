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
    setName(state, name) {
      state.name = name;
    },
    setList(state, lists) {
      state.lists = lists;
    },
    setCurrentSpeaker(state, name) {
      state.current_speaker = name;
    }
  },
  actions: {
    addSpeaker({ commit }, name) {
      return new Promise((resolve, reject) => {
        Axios({ url: "/speaker/add/" + name, method: "POST" })
          .then(resp => {
            commit("setName", name);
            resolve(resp);
          })
          .catch(err => {
            reject(err);
          });
      });
    },
    updateLists({ commit }) {
      return new Promise((resolve, reject) => {
        Axios({ url: "/list/get", method: "GET" })
          .then(resp => {
            commit("setList", resp.data.data);
            resolve(resp);
          })
          .catch(err => {
            reject(err);
          });
      });
    },
    nextSpeaker({ commit }) {
      return new Promise((resolve, reject) => {
        Axios({ url: "/list/next", method: "POST" })
          .then(resp => {
            commit("setCurrentSpeaker", resp.data);
            resolve(resp);
          })
          .catch(err => {
            commit("setCurrentSpeaker", "");
            reject(err);
          });
      });
    }
  },
  getters: {},
  modules: {}
});
