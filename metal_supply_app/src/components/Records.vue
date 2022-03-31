<template>
  <header class="jumbotron ">
    <h3 class="display-4">Records</h3>
    <hr class="my-4">
    <p class="lead">
      All <strong>Public</strong> Records on the Platform
    </p>
  </header>
  <div class=" container row justify-content-between mb-4">
    <input class="form-control col-lg-10" type="search" placeholder="Search" aria-label="Search">
    <button type="button" class="btn btn-secondary" data-toggle="modal" data-target="#add-record-modal">
      <font-awesome-icon icon="plus" /> New Record
    </button>
  </div>
  <RecordCards :records="records" :isCardLink="false" :isLastUpdate="true" />
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
  }
}
</script>

<style scoped>

</style>