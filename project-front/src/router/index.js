import { createRouter, createWebHistory } from "vue-router";
import MainView from "@/views/MainView.vue";
import SignUpView from "@/views/SignUpView.vue";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: "Main",
      component: MainView,
    },
    {
      path: "/sign_up",
      name: "SignUp",
      component: SignUpView,
    },
  ],
});

export default router;
