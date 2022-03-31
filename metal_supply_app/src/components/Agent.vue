<template>
  <header class="jumbotron ">
    <h3 class="display-4">
      <strong>{{agent.name}}</strong>
    </h3>
    <hr class="my-4">
    <p class="lead">
      <strong>Company:</strong>
      {{agent.company}}
    </p>
    <p class="lead">
      <strong>Email:</strong>
      {{agent.email}}
    </p>
    <p class="lead" v-if="agent.role">
      <strong>Role:</strong>
      {{agent.role}}
    </p>
  </header>
</template>

<script>
import UserService from "@/services/user.service";

export default {
  name: "Agent",
  data() {
    return {
      agent: {},
    };
  },
  mounted() {
    UserService.getAgent(this.$route.params.id).then(
        (response) => {
          this.agent = response.data;
          this.agent.role = this.convertRole(this.agent.role)
        },
        (error) => {
          this.content =
              (error.response &&
                  error.response.data &&
                  error.response.data.message) ||
              error.message ||
              error.toString();
        }
    );
  },
  methods: {
    convertRole(word) {
      let result = word.split('_').join(" ").toLowerCase();
      return result[0].toUpperCase() + result.slice(1);
    }
  }
}
</script>

<style scoped>

</style>