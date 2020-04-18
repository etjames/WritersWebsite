import Vue from "vue";
import VueRouter from "vue-router";
import Home from "../views/Home.vue";
import StoryPreferences from "../views/StoryPreferences.vue";
import StoryContent from "../views/StoryContent.vue";
import AnonymousFeedback from "../views/AnonymousFeedback.vue"
import Prompts from "../views/Prompts.vue"

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home
  },
  {
    path: "/about",
    name: "About",
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/About.vue")
  },
  {
    path: "/storypreferences",
    name: "Story Preferences",
    component: StoryPreferences
  },
  {
    path: "/storycontent",
    name: "Story Content",
    component: StoryContent
  },
  {
    path: "/anonymousfeedback",
    name: "Anonymous Feedback",
    component: AnonymousFeedback
  },
  {
    path: "/prompts",
    name: "Prompts",
    component: Prompts
  }
];

const router = new VueRouter({
  routes
});

export default router;
