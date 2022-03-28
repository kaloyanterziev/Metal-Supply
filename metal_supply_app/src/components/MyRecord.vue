<template>
  <header class="jumbotron">
    <h3>Record  {{record.id}}</h3>
    <p class="card-title">Material Origin:  {{record.material_origin}}</p>
    <p class="card-text">Material Type: {{record.material_type}}</p>
    <p class="card-text">{{record.tonnes}} tonnes</p>
    <p class="card-text" v-if="record.published != null">{{record.published ? "Published" : "Private"}}</p>
  </header>
  <h3>Contents: </h3>
  <ContentChart v-if="record.contents"
                :dataLabels="record.contents.map(function(item){return item.metal;})"
                :dataValues="record.contents.map(function(item){return item.percentage;})"/>
  <h3>Locations: </h3>
  <div class="d-flex justify-content-end  mb-4">
    <button type="button" class="btn btn-success" data-toggle="modal" data-target="#link-record-modal">
      <font-awesome-icon icon="link" /> Link Record
    </button>
    <button type="button" class="btn btn-warning ml-3" data-toggle="modal" data-target="#transfer-record-modal">
      <font-awesome-icon icon="arrow-right" /> Transfer Record
    </button>
    <button type="button" class="btn btn-primary ml-3" data-toggle="modal" data-target="#add-location-modal">
      <font-awesome-icon icon="plus" /> Add Location
    </button>
  </div>
  <AddLocationModal @onLocationAdded="getRecord"/>
  <LinkRecordModal @onRecordLinked="getRecord" />
  <TransferRecordModal @onRecordTransferred="this.$router.push('/profile')"/>
  <div v-if="record.locations">
    <GMapMap
        :center="center"
        :zoom="3"
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
  <h3>History: </h3>
  <GMapMap
      :center="history_center"
      :zoom="3"
      style="width: 100%; height: 600px"
  >
    <GMapHeatmap :data="heatData"></GMapHeatmap>
    <GMapPolyline
        :path="path"
        :editable="false"
        ref="polyline" />
  </GMapMap>



</template>

<script>
import RecordService from "@/services/record.service";
import AddLocationModal from "@/components/AddLocationModal";
import TransferRecordModal from "@/components/TransferRecordModal";
import LinkRecordModal from "@/components/LinkRecordModal";
import ContentChart from "@/components/ContentChart";
/*global google*/

export default {
  name: "MyRecord",
  components: {
    LinkRecordModal,
    AddLocationModal,
    TransferRecordModal,
    ContentChart
  },
  data() {
    return {
      record: {},
      heatData: [
      ],
      path: [
      ],
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
            this.heatData = []
            this.path = []
            this.computeHistoryLocations(this.record)
          }
      )
    },
    computeHistoryLocations(record) {
      if(record.prev_records && record.prev_records.length > 0) {
        for (let prev_record of record.prev_records) {
          this.computeHistoryLocations(prev_record)
        }
      }
      if(record.locations && record.locations.length > 0) {
        for(let location of record.locations) {
          this.heatData.push({location: new google.maps.LatLng({lat: location.latitude, lng: location.longitude})})
          this.path.push({lat: location.latitude, lng: location.longitude})
        }
      }
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
    },
    history_center() {
      if(this.path.length > 0) {
        return {
          lat: this.path.reduce((total, next) => total + next.lat, 0) / this.path.length,
          lng: this.path.reduce((total, next) => total + next.lng, 0) / this.path.length
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