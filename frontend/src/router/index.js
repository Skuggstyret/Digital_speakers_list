import Vue from "vue";
import VueRouter from "vue-router";
import Home from "@/views/Home.vue";
import Speaker from "@/components/Speaker.vue";
import List from "@/components/List.vue";
import Meeting from "@/views/Meeting.vue";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home
  },
  {
    path: "/speaker",
    name: "Speaker",
    component: Speaker
  },
  {
    path: "/list",
    name: "List",
    component: List
  },
  {
    path: "/meeting",
    name: "Meeting",
    component: Meeting
  }
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes
});

export default router;
