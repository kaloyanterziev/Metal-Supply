<template>
  <div class="modal fade" tabindex="-1" role="dialog" ref="add-record-modal" id="add-record-modal">
    <div class="modal-dialog modal-dialog-centered" role="document">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title" id="exampleModalLongTitle">Add Record</h5>
          <button type="button" ref="close" class="close" data-dismiss="modal" aria-label="Close">
            <span aria-hidden="true">&times;</span>
          </button>
        </div>
        <div class="modal-body card p-4">
          <form name="form" @submit.prevent="addRecord">
            <div v-if="!successful">
              <div class="form-group">
                <label for="record.material_origin">Material Origin</label>
                <input v-model="record.material_origin" name="record.material_origin" required type="text" class="form-control" />
              </div>
              <div class="form-group">
                <label for="material_type">Material Type</label>
                <input v-model="record.material_type" name="material_type" type="text" required class="form-control" />
              </div>
              <div class="form-group">
                <label for="record.tonnes">Tonnes</label>
                <input v-model="record.tonnes" name="record.tonnes" type="number" required class="form-control" min="0" />
              </div>
              <div class="form-group">
                <label for="record.latitude">Latitude</label>
                <input v-model="record.latitude" name="record.latitude" type="number" required step="any" min="-90" max="90" class="form-control" />
              </div>
              <div class="form-group">
                <label for="record.longitude">Longitude</label>
                <input v-model="record.longitude" name="record.longitude" type="number" required step="any" min="-180" max="180" class="form-control" />
              </div>
              <div class="form-group">
                <div class="container row justify-content-between">
                  <label for="record.public">Would you like this Record to be publicly visible?</label>
                  <input v-model="record.public" name="record.public" type="checkbox" class="form-control" />
                </div>
              </div>
              <div class="form-group">
                <div class="container row justify-content-between">
                  <label for="contents">Contents</label>
                  <button type="button" class="btn btn-secondary" @click="addEmptyContentToRecord">
                    <font-awesome-icon icon="plus" /> Add Content
                  </button>
                </div>
                <div class="mt-5" v-for="(content, index) in record.contents" v-bind:key="index" >
                  <select v-model="content.metal" name="content_metal" class="form-control">
                    <option value="" selected disabled>Please select metal</option>
                    <option value="Cu">Copper</option>
                    <option value="Al">Aluminum</option>
                    <option value="Pb">Lead</option>
                    <option value="Fe">Iron</option>
                    <option value="Zn">Zinc</option>
                    <option value="Ni">Nickel</option>
                    <option value="Ag">Gold</option>
                    <option value="Au">Silver</option>
                    <option value="Pt">Platinum</option>
                    <option value="Pd">Palladium</option>
                  </select>
                  <div class="container row mt-1">
                    <input class="col-9" v-model="content.percentage" name="content_percentage" type="range" min="0" max="100" />
                    <input class="col-3" v-model="content.percentage" name="content_percentage_text_box" type="number" step="any" min="0" max="100" />
                  </div>
                </div>
              </div>
              <div class="form-group">
                <button type="submit" class="btn btn-primary btn-block" :disabled="loading">
                  <span
                      v-show="loading"
                      class="spinner-border spinner-border-sm"
                  ></span>
                  Create Record
                </button>
              </div>
            </div>
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
  name: 'AddRecordModal',
  data() {
    return {
      successful: false,
      loading: false,
      message: "",
      record: {
        contents: [{"percentage": 0, "metal": ""}]
      },
    };
  },
  methods: {
    addRecord() {
      this.message = "";
      this.successful = false;
      this.loading = true;

      let sumOfContentPercentages = this.record.contents.reduce((prev, curr) => prev + curr.percentage, 0)
      if(sumOfContentPercentages>100) {
        this.message = "Contents should not exceed 100%"
        this.loading = false;
        return
      }

      RecordService.createRecord(this.record).then(
          data => {
            this.message = data.data.data;
            this.loading = false;
            this.successful = true;
            const self = this;
            setTimeout(function () {
              self.message = "";
              self.successful = false;
              self.record = {
                contents: [{"percentage": 0, "metal": ""}]
              }
              self.$refs.close.click();
            }, 1000);
            this.$emit('onRecordCreate');
            this.$refs['add-record-modal'].hide();
          }, error => {
            console.log(error)
            this.successful = false;
            this.message = error.data.error;
            this.loading = false;
          }
      );
    },
    addEmptyContentToRecord() {
      this.record.contents.push({"percentage": 0, "metal": ""});
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