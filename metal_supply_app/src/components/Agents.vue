<template>
  <header class="jumbotron">
    <h3>Agents</h3>
  </header>
  <div class="card-columns">
    <div class="card"
         v-for="agent in agents"
         v-bind:key="agent.id"
    >
      <div class="card-body">
        <h5 class="card-title">{{agent.name}}</h5>
        <p class="card-text">{{agent.role}}</p>
      </div>
    </div>
  </div>
</template>

<script>
import UserService from "../services/user.service";


export default {
  name: "Agents",
  data() {
    return {
      agents: {},
    };
  },
  mounted() {
    UserService.getAllAgents().then(
        (response) => {
          this.agents = response.data;
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