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
  <input v-model="search" class="form-control mb-3" type="search" placeholder="Search" aria-label="Search">
  <div class="card-columns">
    <div class="card"
         v-for="agent in filteredAgents"
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
      search: ""
    };
  },
  mounted() {
    UserService.getAllAgents().then(
        (response) => {
          this.agents = response.data;
          this.convertRoleInAgents();
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
  computed: {
    filteredAgents() {
      if(this.search === "") {
        return this.agents
      }
      return this.agents.filter(agent => {
        return JSON.stringify(agent).toLowerCase().includes(this.search.toLowerCase())
      })
    }
  },
  methods: {
    convertRoleInAgents() {
      this.agents.forEach(agent => {
        let result = agent.role.split('_').join(" ").toLowerCase();
        agent.role = result[0].toUpperCase() + result.slice(1);
      })
    }
  }
}
</script>

<style scoped>

</style>