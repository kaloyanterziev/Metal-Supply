<template>
  <div class="modal fade" tabindex="-1" role="dialog" ref="transfer-record-modal" id="transfer-record-modal">
    <div class="modal-dialog modal-dialog-centered" role="document">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title" id="exampleModalLongTitle">Transfer Record {{record_id}}</h5>
          <button type="button" ref="close" class="close" data-dismiss="modal" aria-label="Close">
            <span aria-hidden="true">&times;</span>
          </button>
        </div>
        <div class="modal-body card p-4">
          <form name="form" @submit.prevent="transferRecord">
            <!--            <div v-if="!successful">-->

            <div class="form-group">
              <select v-model="receiving_agent_id" name="receiving_agent_id" class="form-control">
                <option v-for="agent in agents" v-bind:key="agent.id"
                        :value="agent.id">{{agent.name}} {{agent.role}}
                </option>
              </select>
              <div class="container row mt-1">
                <input class="col-9" v-model="percentage" name="content_percentage" type="range" min="0" max="100" />
                <input class="col-3" v-model="percentage" name="content_percentage_text_box" type="number" step="any" min="0" max="100" />
              </div>
            </div>
            <div class="form-group">
              <button type="submit" class="btn btn-primary btn-block" :disabled="loading">
                  <span
                      v-show="loading"
                      class="spinner-border spinner-border-sm"
                  ></span>
                Transfer Location
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
  name: 'TransferRecordModal',
  data() {
    return {
      successful: false,
      loading: false,
      message: "",
      agents: [],
      receiving_agent_id: null,
      percentage:0.1
    };
  },
  mounted() {
    UserService.getAllAgents().then(
        (response) => {
          this.agents = response.data;
        },
        (error) => {
          console.log(error)
        }
    );
  },
  methods: {
    transferRecord() {
      this.message = "";
      this.successful = false;
      this.loading = true;

      RecordService.transferRecord(this.record_id, this.receiving_agent_id, this.percentage).then(
          data => {
            this.message = data.data.data;
            const self = this;
            setTimeout(function () {
              self.message = "";
              self.successful = true;
              self.$refs.close.click();
              this.$emit('onRecordTransferred');
            }, 3000);
            this.loading = false;
            this.receiving_agent_id = null;
            this.percentage = 0.1;
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