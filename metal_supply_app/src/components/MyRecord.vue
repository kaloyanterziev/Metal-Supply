<template>
  <header class="jumbotron">
    <h3>Record  {{record.id}}</h3>
    <p class="card-title"> {{record.material_origin}}</p>
    <p class="card-text">{{record.material_type}}</p>
    <p class="card-text">{{record.tonnes}} tonnes</p>
    <p class="card-text" v-if="record.published">{{record.published}}</p>
  </header>
  <h3>Locations: </h3>
  <div class="d-flex justify-content-end  mb-4">
    <button type="button" class="btn btn-warning" data-toggle="modal" data-target="#transfer-record-modal">
      <font-awesome-icon icon="arrow-right" /> Transfer Record
    </button>
    <button type="button" class="btn btn-primary ml-4" data-toggle="modal" data-target="#add-location-modal">
      <font-awesome-icon icon="plus" /> Add Location
    </button>
  </div>
  <AddLocationModal @onLocationAdded="getRecord"/>
  <TransferRecordModal @onModalTransfered="this.$router.back()"/>
  <div v-if="record.locations">
  <GMapMap
      :center="center"
      :zoom="7"
      map-type-id="terrain"
      class="mb-5"
  >
    <GMapMarker
        :key="position.timestamp"
        v-for="position in record.locations"
        :position="{lng: position.longitude, lat: position.latitude}"
    />
  </GMapMap>
  </div>

</template>

<script>
import RecordService from "@/services/record.service";
import AddLocationModal from "@/components/AddLocationModal";
import TransferRecordModal from "@/components/TransferRecordModal";
export default {
  name: "MyRecord",
  components: {
    AddLocationModal,
    TransferRecordModal
  },
  data() {
    return {
      record: {}
    }
  },
  mounted() {
    this.getRecord();
  },
  methods : {
    getRecord() {
      RecordService.getRecord(this.$route.params.id).then(
          (response) => {
            this.record = response.data;
          }
      )
    }
  }, computed: {
    center() {
      if(this.record && this.record.locations && this.record.locations.length > 0) {
        return {
          lat: this.record.locations.reduce((total, next) => total + next.latitude, 0) / this.record.locations.length,
          lng: this.record.locations.reduce((total, next) => total + next.longitude, 0) / this.record.locations.length
        }
      }
      return {lat: 51.093048, lng: 6.842120}
    }
  }
}
</script>

<style>
.vue-map {
  /*position: absolute !important;*/
  display: flex !important;
  /*width: 100% !important;*/
  height: 35rem !important;
}
</style>