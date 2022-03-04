<template>
  <header class="jumbotron">
    <h3>Records</h3>
  </header>
  <div class=" container row justify-content-between mb-4">
    <input class="form-control col-lg-10" type="search" placeholder="Search" aria-label="Search">
    <button type="button" class="btn btn-secondary" data-toggle="modal" data-target="#add-record-modal">
      <font-awesome-icon icon="plus" /> New Record
    </button>
  </div>
  <div class="card-columns">
    <div class="card"
         v-for="record in records"
         v-bind:key="record.id"
    >
      <div class="card-body">
        <h5 class="card-title">{{record.material_origin}}</h5>
        <p class="card-text">{{record.material_type}}</p>
        <p class="card-text">{{record.tonnes}} tonnes</p>
          <div class="card-text"
            v-for="owner in record.owners"
            v-bind:key="owner.id">
            <router-link :to="'/agents/' + owner.id">{{owner.name}}</router-link>
          </div>
        <p class="card-text">{{record.address}}</p>
        <p class="card-text"><small class="text-muted">Last updated 3 mins ago</small></p>
      </div>
    </div>
  </div>
  <AddRecordModal @onRecordCreate="getAllRecords"/>
</template>

<script>
import RecordService from "../services/record.service";
import AddRecordModal from "@/components/AddRecordModal";
import GoogleApisService from "@/services/googleapis.service";


export default {
  name: "Records",
  components : {
    AddRecordModal
  },
  data() {
    return {
      records: [],
    };
  },
  mounted() {
    this.getAllRecords();
  },
  methods: {
    getAllRecords() {
      RecordService.getAllRecords().then(
          (response) => {
            this.records = response.data;
            this.records.forEach((record, index) => {
              if(record.locations) {
                let location = record.locations.reduce((prev, current) => (prev.timestamp > current.timestamp) ? prev : current)
                this.getAddress(location, index)
              }
            })
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
    getAddress(location, index) {
      GoogleApisService.reverseGeocoding(location.latitude, location.longitude)
          .then((response) => {
            this.records[index]['address'] = response.data.results[0].formatted_address;
          })
    }
  }
}
</script>

<style scoped>

</style>