<template>
  <header class="jumbotron">
    <h3>Record  {{record.id}}</h3>
    <p class="card-title"> {{record.material_origin}}</p>
    <p class="card-text">{{record.material_type}}</p>
    <p class="card-text">{{record.tonnes}} tonnes</p>
    <p class="card-text" v-if="record.published">{{record.published}}</p>
  </header>
  <h3>Locations: </h3>
  <div v-if="record.locations">
  <GMapMap
      :center="center"
      :zoom="7"
      map-type-id="terrain"
      :options="options"
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
export default {
  name: "MyRecord",
  data() {
    return {
      record: {},
      options: {
        styles: [
          {
            elementType: 'vue-map',
            stylers: [
              {
                width: '10px'
              },
            ],
          }
        ]
      }
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
        console.log(this.record.locations.reduce((total, next) => total + next.latitude, 0) / this.record.locations.length)
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