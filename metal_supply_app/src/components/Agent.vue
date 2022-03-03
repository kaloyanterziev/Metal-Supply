<template>
  <div class="container">
    <header class="jumbotron">
      <h3>
        <strong>{{agent.name}}</strong>'s Profile
      </h3>
    </header>
    <p>
      <strong>Email:</strong>
      {{agent.email}}
    </p>
    <p>
      <strong>Role:</strong>
      {{agent.role}}
    </p>
  </div>
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
}
</script>

<style scoped>

</style>