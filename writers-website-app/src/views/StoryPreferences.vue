<template>
  <div>
    <form>
      <label for="writing-types">
        1. What types of writting do you like to read? (Select all that apply)
        <select id="writing-types" multiple="true" v-model="writingTypes">
          <option value="Poetry">Poetry</option>
          <option value="Scripts">Scripts</option>
          <option value="Long Form">Long Form</option>
        </select>
      </label>
      <label for="genres">
        2. What genres of writing do you like to read? (Select all that apply)
        <select id="genres" multiple="true" v-model="genres">
          <option value="Horror">Horror</option>
          <option value="Romance">Romance</option>
          <option value="Comedy">Comedy</option>
          <option value="Action">Action</option>
          <option value="Legal">Legal</option>
        </select>
      </label>
      <label for="time">
        3. How long would you like the story to be? (Select all that apply)
        <select id="time" multiple="true" v-model="time">
          <option value="5-10 minutes">5-10 minutes</option>
          <option value="10-30 minutes">10-30 minutes</option>
          <option value="30-60 minutes">30-60 minutes</option>
          <option value="60 minutes +">60 minutes +</option>
        </select>
      </label>
      <label for="theme">
        4. What themes do you like to read about? (Select all that apply)
        <select id="theme" multiple="true" v-model="theme">
          <option value="LGBTQ+">LGBTQ+</option>
          <option value="Being a person of color">Being a person of color</option>
          <option value="Family">Family</option>
        </select>
      </label> 
      <div>
        <button type="submit">Save</button>
      </div>
    </form>
  </div>
</template>

<script type="text/javascript">
export default {
  name: "StoryPreferences",
  props: {
    writingTypes: Array,
    genres: Array,
    storyLength: String,
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