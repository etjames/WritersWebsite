<template>
  <div>
    <form>
      <label for="writing-types">
        1. What types of writting is this piece? (Select all that apply)
        <select id="writing-types" multiple="true" v-model="writingTypes">
          <option value="Poetry">Poetry</option>
          <option value="Scripts">Scripts</option>
          <option value="Long Form">Long Form</option>
        </select>
      </label>
      <label for="genres">
        2. What genres does this piece of writing fit under? (Select all that apply)
        <select id="genres" multiple="true" v-model="genres">
          <option value="Horror">Horror</option>
          <option value="Romance">Romance</option>
          <option value="Comedy">Comedy</option>
          <option value="Action">Action</option>
          <option value="Legal">Legal</option>
        </select>
      </label>
      <label for="time">
        3. How much time do you expect the reader to dedicate to this piece?
        <select id="time" multiple="true" v-model="time">
          <option value="5-10 minutes">5-10 minutes</option>
          <option value="10-30 minutes">10-30 minutes</option>
          <option value="30-60 minutes">30-60 minutes</option>
          <option value="60 minutes +">60 minutes +</option>
        </select>
      </label>
      <label for="themes">
        4. What themes does this piece contain? (Select all that apply)
        <select id="themes" multiple="true" v-model="themes">
          <option value="LGBTQ+">LGBTQ+</option>
          <option value="Being a person of color">Being a person of color</option>
          <option value="Family">Family</option>
        </select>
      </label> 
      <label for="people">
        5. How many people would you like to read your piece?
        <select id="people" multiple="true" v-model="people">
          <option value="Only 1">Only 1</option>
          <option value="2-3">2-3</option>
          <option value="4-5">4-5</option>
          <option value="5-10">5-10</option>
        </select>
      </label> 
      <label for="people">
        6. Please list any aspects you would like the reader's feedback to focus on.
        <span>Multiline message is:</span>
        <p style="white-space: pre-line;">{{ message }}</p>
        <br>
        <textarea v-model="message" placeholder="dialogue, word choice, etc."></textarea>
      </label> 
      
      <div>
        <button v-on:click="warn('Form cannot be submitted yet.', $event)">
        Submit
        </button>
      </div>
    </form>
  </div>
</template>

<script type="text/javascript">
export default {
  name: "StoryContent",
  props: {
    writingTypes: Array,
    genres: Array,
    storyLength: String,
  },  
  methods: {
  warn: function (message, event) {
    // now we have access to the native event
    if (event) {
      event.preventDefault()
    }
    alert(message)
  }
}
};
</script>

<style type="scss">
label {
  max-width: 300px;
  display: inline-block;
  padding: 10px;
  text-align: left;
}
select {
  display: block;
  width: 300px;
}
</style>