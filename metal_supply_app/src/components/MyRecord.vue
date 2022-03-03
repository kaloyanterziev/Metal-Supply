<template>
  <header class="jumbotron">
    <h3>Record</h3>
  </header>

</template>

<script>
import UserService from "@/services/user.service";
export default {
  name: "MyRecord",
  data() {
    return {
      record: {}
    }
  },
  mounted() {
    this.getAgentRecords();
  },
  methods : {
    getAgentRecords() {
      UserService.getAgentRecords().then(
          (response) => {
            this.record = response.data;
          }
      )
    }
  }
}
</script>

<style scoped>

</style>