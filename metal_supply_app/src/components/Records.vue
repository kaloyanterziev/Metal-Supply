<template>
  <header class="jumbotron ">
    <h3 class="display-4">Records</h3>
    <hr class="my-4">
    <p class="lead">
      All <strong>Public</strong> Records on the Platform
    </p>
  </header>
  <div class=" container row justify-content-between mb-4">
    <input v-model="search" class="form-control col-lg-10" type="search" placeholder="Search" aria-label="Search">
    <button type="button" class="btn btn-secondary" data-toggle="modal" data-target="#add-record-modal">
      <font-awesome-icon icon="plus" /> New Record
    </button>
  </div>
  <RecordCards :records="filteredRecords" :isCardLink="false" :isLastUpdate="true" />
  <AddRecordModal @onRecordCreate="getAllRecords"/>
</template>

<script>
import RecordService from "../services/record.service";
import RecordCards from "@/components/RecordCards";
import AddRecordModal from "@/components/AddRecordModal";
import GoogleApisService from "@/services/googleapis.service";


export default {
  name: "Records",
  components : {
    AddRecordModal,
    RecordCards
  },
  data() {
    return {
      records: [],
      search: ""
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
              if(record.locations && record.locations.length > 0) {
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
  },
  computed: {
    filteredRecords() {
      if(this.search === "") {
        return this.records
      }
      return this.records.filter(record => {
        return JSON.stringify(record).toLowerCase().includes(this.search.toLowerCase())
      })
    }
  }
}
</script>

<style scoped>

</style>