<template>
  <div class="modal fade" tabindex="-1" role="dialog" ref="add-location-modal" id="add-location-modal">
    <div class="modal-dialog modal-dialog-centered" role="document">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title" id="exampleModalLongTitle">Add Location to Record {{record_id}}</h5>
          <button type="button" ref="close" class="close" data-dismiss="modal" aria-label="Close">
            <span aria-hidden="true">&times;</span>
          </button>
        </div>
        <div class="modal-body card p-4">
          <form name="form" @submit.prevent="addLocation">
<!--            <div v-if="!successful">-->
              <div class="form-group">
                <label for="latitude">Latitude</label>
                <input v-model="latitude" name="latitude" type="number" required step="any" min="-90" max="90" class="form-control" />
              </div>
              <div class="form-group">
                <label for="longitude">Longitude</label>
                <input v-model="longitude" name="longitude" type="number" required step="any" min="-180" max="180" class="form-control" />
              </div>

              <div class="form-group">
                <button type="submit" class="btn btn-primary btn-block" :disabled="loading">
                  <span
                      v-show="loading"
                      class="spinner-border spinner-border-sm"
                  ></span>
                  Add Location
                </button>
              </div>
<!--            </div>-->
          </form>
          <div
              v-if="message"
              class="alert"
              :class="successful ? 'alert-success' : 'alert-danger'"
          >
            {{ message }}
          </div>

        </div>
      </div>
    </div>
  </div>
</template>

<script>
import RecordService from '@/services/record.service'

export default {
  name: 'AddLocationModal',
  data() {
    return {
      successful: false,
      loading: false,
      message: "",
      latitude: 0,
      longitude: 0
    };
  },
  mounted() {
    this.message = "";
    this.successful = false;
  },
  methods: {
    addLocation() {
      this.message = "";
      this.successful = false;
      this.loading = true;

      RecordService.updateRecordLocation(this.record_id, this.latitude, this.longitude).then(
          data => {
            this.message = data.data.data;
            const self = this;
            setTimeout(function () {
              self.message = "";
              self.successful = true;
              self.$refs.close.click();
            }, 1000);
            this.loading = false;
            this.successful = true;
            this.$emit('onLocationAdded');

            this.longitude = 0;
            this.latitude = 0;
          }, error => {
            console.log(error)
            this.successful = false;
            this.message = error;
            this.loading = false;
          }
      );
    }
  },
  computed: {
    record_id() {
      return this.$route.params.id;
    }
  }
};
</script>

<style scoped>
/*label {*/
/*  display: block;*/
/*  margin-left: 10px;*/
/*}*/

/*.profile-img-card {*/
/*  display: block;*/
/*}*/

/*#hat {*/
/*  position: absolute;*/
/*  top: 1px;*/
/*  right: 1px;*/
/*}*/
</style>