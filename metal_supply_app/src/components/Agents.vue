<template>
  <header class="jumbotron ">
    <h3 class="display-4">
      Agents
    </h3>
    <hr class="my-4">
    <p class="lead">
      All Agents on the Platform
    </p>
  </header>
  <div class="card-columns">
    <div class="card"
         v-for="agent in agents"
         v-bind:key="agent.id"
    >
      <router-link :to=" '/agents/' + agent.id" style="text-decoration: none; color: inherit;">
        <div class="card-body">
          <h5 class="card-title">{{agent.name}}</h5>
          <p class="card-text">{{agent.role}}</p>
        </div>
      </router-link>
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