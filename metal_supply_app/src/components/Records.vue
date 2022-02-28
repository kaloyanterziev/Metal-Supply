<template>
  <header class="jumbotron">
    <h3>Records</h3>
  </header>
  <div class="card-columns">
    <div class="card"
         v-for="record in records"
         v-bind:key="record.id"
    >
      <div class="card-body">
        <h5 class="card-title">{{record.material_type}}</h5>
        <p class="card-text">{{record.material_origin}}</p>
        <p class="card-text">{{record.tonnes}} tonnes</p>
          <div class="card-text"
            v-for="owner in record.owners"
            v-bind:key="owner.id">
            {{owner.percentage_owner}}% {{owner.name}}
          </div>

        <p class="card-text"><small class="text-muted">Last updated 3 mins ago</small></p>
      </div>
    </div>
  </div>
</template>

<script>
import RecordService from "../services/record.service";


export default {
  name: "Records",
  data() {
    return {
      records: {},
    };
  },
  mounted() {
    RecordService.getAllRecords().then(
        (response) => {
          this.records = response.data;
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
}
</script>

<style scoped>

</style>