<template>
  <div class="container">
    <header class="jumbotron ">
      <h3 class="display-4">
        <strong>{{currentUser.name}}</strong>
      </h3>
      <hr class="my-4">
      <p class="lead">
        <strong>Company:</strong>
        {{currentUser.company}}
      </p>
      <p class="lead">
        <strong>Email:</strong>
        {{currentUser.email}}
      </p>
      <p class="lead">
        <strong>Role:</strong>
        {{roles[currentUser.role]}}
      </p>
    </header>
    <hr />
    <h5 class="mt-4">My Records:</h5>
    <div class=" container row justify-content-between mb-4">
      <input class="form-control col-lg-10" type="search" placeholder="Search" aria-label="Search">
      <button type="button" class="btn btn-secondary" data-toggle="modal" data-target="#add-record-modal">
        <font-awesome-icon icon="plus" /> New Record
      </button>
    </div>
    <AddRecordModal @onRecordCreate="getAgentRecords"/>
    <RecordCards :records="records" :isCardLink="true" :isLastUpdate="true" />
  </div>
</template>

<script>
import UserService from "@/services/user.service";
import AddRecordModal from "@/components/AddRecordModal";
import GoogleApisService from "@/services/googleapis.service";

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
      records: [],
      roles: {
        0: "Recycler",
        1: "Converter",
        2: "Waste Owner"
      }
    }
  },
  mounted() {
    if (!this.currentUser) {
      this.$router.push('/login');
    }
    console.log(this.currentUser)
    this.getAgentRecords()
  },
  methods: {
    getAgentRecords() {
      UserService.getAgentRecords().then(
          (response) => {
            this.records = response.data;
            this.records.forEach((record, index) => {
              if(record.locations) {
                let location = record.locations.reduce((prev, current) => (prev.timestamp > current.timestamp) ? prev : current)
                this.getAddress(location, index)
              }
            })
          }, (error) => {
            this.message = error;
          }
      )
    },
    getAddress(location, index) {
      GoogleApisService.reverseGeocoding(location.latitude, location.longitude)
        .then((response) => {
          if(response.data.results.length > 0)
            this.records[index]['address'] = response.data.results[0].formatted_address;
        })
    }
  }
};
</script>