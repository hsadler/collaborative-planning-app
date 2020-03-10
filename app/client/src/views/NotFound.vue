<template>
  <div>
    <h1>💩💩💩 PAGE NOT FOUND 💩💩💩</h1>
    <button @click="goBack()">Go back</button>
  </div>
</template>

<script>
export default {
  name: 'NotFound',
  components: {},
  methods: {
    goBack () {
      this.$router.go(-1)
    }
  }
}
</script>

<style scoped>
  button {
    cursor: pointer;
  }
</style>
