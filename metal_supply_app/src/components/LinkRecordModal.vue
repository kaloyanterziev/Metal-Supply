<template>
  <div class="modal fade" tabindex="-1" role="dialog" ref="link-record-modal" id="link-record-modal">
    <div class="modal-dialog modal-dialog-centered" role="document">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title" id="exampleModalLongTitle">Link To Previous Record {{record_id}}</h5>
          <button type="button" ref="close" class="close" data-dismiss="modal" aria-label="Close">
            <span aria-hidden="true">&times;</span>
          </button>
        </div>
        <div class="modal-body card p-4">
          <form name="form" @submit.prevent="linkRecord">
            <!--            <div v-if="!successful">-->

            <div class="form-group">
              <select v-model="prev_record_id" name="prev_record_id" class="form-control">
                <option v-for="record in records" v-bind:key="record.id"
                        :value="record.id">{{record.material_type}} {{record.material_origin}} {{record.tonnes}}
                </option>
              </select>
            </div>
            <div class="form-group">
              <button type="submit" class="btn btn-primary btn-block" :disabled="loading">
                  <span
                      v-show="loading"
                      class="spinner-border spinner-border-sm"
                  ></span>
                Link Record
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
import UserService from "@/services/user.service";

export default {
  name: 'LinkRecordModal',
  data() {
    return {
      successful: false,
      loading: false,
      message: "",
      records: [],
      prev_record_id: null
    };
  },
  mounted() {
    UserService.getAgentRecords().then(
        (response) => {
          this.records = response.data;
        },
        (error) => {
          console.log(error)
        }
    );
  },
  methods: {
    linkRecord() {
      this.message = "";
      this.successful = false;
      this.loading = true;

      RecordService.linkRecord(this.record_id, this.prev_record_id).then(
          data => {
            this.message = data.data.data;
            this.successful = true;
            const self = this;
            setTimeout(function () {
              self.message = "";
              self.successful = false;
              self.$refs.close.click();
            }, 1000);
            this.loading = false;
            this.$emit('onRecordLinked');
            this.prev_record_id = null;
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