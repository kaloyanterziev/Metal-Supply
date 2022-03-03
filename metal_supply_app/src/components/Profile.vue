<template>
  <div class="container">
    <header class="jumbotron">
      <h3>
        <strong>{{currentUser.name}}</strong> Profile
      </h3>
    </header>
    <p>
      <strong>Email:</strong>
      {{currentUser.email}}
    </p>
    <p>
      <strong>Role:</strong>
      {{currentUser.role}}
    </p>
    <h5>My Records:</h5>
    <div class=" container row justify-content-between mb-4">
      <input class="form-control col-lg-10" type="search" placeholder="Search" aria-label="Search">
      <button type="button" class="btn btn-secondary" data-toggle="modal" data-target="#add-record-modal">
        <font-awesome-icon icon="plus" /> New Record
      </button>
    </div>
    <AddRecordModal @onRecordCreate="getAgentRecords"/>
    <div class="card-columns">
      <router-link class="card"
           v-for="record in records"
           v-bind:key="record.id"
           :to="'/my-records/' + record.id"
           style="text-decoration: none; color: inherit;"
      >
        <div class="card-body">
          <h5 class="card-title">{{record.material_origin}}</h5>
          <p class="card-text">{{record.material_type}}</p>
          <p class="card-text">{{record.tonnes}} tonnes</p>
          <p class="card-text">{{record.published ? "Published" : ""}}</p>
          <div class="card-text"
               v-for="location in record.locations"
               v-bind:key="location.timestamp">
            Lat: {{location.latitude}},  Long:{{location.longitude}}
          </div>
          <p class="card-text"><small class="text-muted">Last updated 3 mins ago</small></p>
        </div>
      </router-link>
    </div>
  </div>
</template>

<script>
import UserService from "@/services/user.service";
import AddRecordModal from "@/components/AddRecordModal";

export default {
  name: 'Profile',
  computed: {
    currentUser() {
      return this.$store.state.auth.user;
    }
  },
  components : {
    AddRecordModal
  },
  data() {
    return {
      message: "",
      records: []
    }
  },
  mounted() {
    if (!this.currentUser) {
      this.$router.push('/login');
    }
    this.getAgentRecords()
  },
  methods: {
    getAgentRecords() {
      UserService.getAgentRecords().then(
          (response) => {
            this.records = response.data;
          }, (error) => {
            this.message = error;
          }
      )
    }
  }
};
</script>