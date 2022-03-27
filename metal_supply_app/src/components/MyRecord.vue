<template>
  <header class="jumbotron">
    <h3>Record  {{record.id}}</h3>
    <p class="card-title">Material Origin:  {{record.material_origin}}</p>
    <p class="card-text">Material Type: {{record.material_type}}</p>
    <p class="card-text">{{record.tonnes}} tonnes</p>
    <p class="card-text" v-if="record.published != null">{{record.published ? "Published" : "Private"}}</p>
  </header>
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
  <h3>History: </h3>
  <GMapMap
      :center="center2"
      :zoom="7"
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
/*global google*/

export default {
  name: "MyRecord",
  components: {
    LinkRecordModal,
    AddLocationModal,
    TransferRecordModal
  },
  data() {
    return {
      record: {},
      center2: {
        lat: 52.2985593,
        lng: 104.2455337,
      },
      heatData: [
        {location: new google.maps.LatLng({lat: 52.2985593, lng: 104.2455337})},
        {location: new google.maps.LatLng({lat: 52.2985593, lng: 105.2455337})},
        {location: new google.maps.LatLng({lat: 52.2985593, lng: 106.2455337})},
        {location: new google.maps.LatLng({lat: 52.2985593, lng: 107.2455337})},
        {location: new google.maps.LatLng({lat: 52.2985593, lng: 108.2455337})},
        {location: new google.maps.LatLng({lat: 52.2985593, lng: 109.2455337})},
        {location: new google.maps.LatLng({lat: 52.2985593, lng: 110.2455337})},
        {location: new google.maps.LatLng({lat: 52.2985593, lng: 111.2455337})},
      ],
      path: [
        {lat: 52.2985593, lng: 104.2455337},
        {lat: 52.2985593, lng: 105.2455337},
        {lat: 52.2985593, lng: 106.2455337},
        {lat: 52.2985593, lng: 107.2455337},
        {lat: 52.2985593, lng: 108.2455337},
        {lat: 52.2985593, lng: 109.2455337},
        {lat: 52.2985593, lng: 110.2455337},
        {lat: 52.2985593, lng: 111.2455337}
      ]
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
    },
    computeHistoryLocations() {

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