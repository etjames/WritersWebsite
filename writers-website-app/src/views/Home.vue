<template>
  <div class="home">
    <img alt="Writer's logo" src="../assets/writerlogo.png" />
    <h1> Welcome to The Writer's Website! </h1>
    <router-link to="/storycontent">Submit Some Writing</router-link> |
    <router-link to="/storypreferences">Read and Give Feedback</router-link>
  </div>
</template>

<script>
// @ is an alias to /src
//import HelloWorld from "@/components/HelloWorld.vue";

export default {
  name: "Home",
  //components: {
  //  HelloWorld
  //}
  props: {
    writingTypes: Array,
    genres: Array,
    storyLength: String,
  } 
};
</script>
