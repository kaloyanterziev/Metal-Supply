<template>
  <div class="card-columns">
    <div v-if="isCardLink">
      <router-link class="card"
                   v-for="record in records"
                   v-bind:key="record.id"
                   :to="'/my-records/' + record.id"
                   style="text-decoration: none; color: inherit;"
      >
        <div class="card-body">
          <h5 class="card-title" v-if="record.material_origin">{{record.material_origin}}</h5>
          <p class="card-text" v-if="record.material_type">{{record.material_type}}</p>
          <p class="card-text" v-if="record.tonnes">{{record.tonnes}} tonnes</p>
          <p class="card-text" v-if="record.published">{{record.published ? "Published" : "Private"}}</p>
          <p class="card-text" v-if="record.address">{{record.address}}</p>
          <ContentChart v-if="record.contents"
                        :dataLabels="record.contents.map(function(item){return item.metal;})"
                        :dataValues="record.contents.map(function(item){return item.percentage;})"
                        :large="false"/>
          <p class="card-text" v-if="isLastUpdate"><small class="text-muted">Last updated 3 mins ago</small></p>
        </div>
      </router-link>
    </div>

    <div v-else>
      <div class="card"

                   v-for="(record, index) in records"
                   v-bind:key="index"
      >
        <div class="card-body">
          <h5 class="card-title" v-if="record.material_origin">{{record.material_origin}}</h5>
          <p class="card-text" v-if="record.material_type">{{record.material_type}}</p>
          <p class="card-text" v-if="record.tonnes">{{record.tonnes}} tonnes</p>
          <p class="card-text" v-if="record.published">{{record.published ? "Published" : "Private"}}</p>
          <p class="card-text" v-if="record.address">{{record.address}}</p>
          <div v-if="record.owners">
            <div class="card-text"
                 v-for="owner in record.owners"
                 v-bind:key="owner.id">
              <router-link :to="'/agents/' + owner.id">{{owner.name}}</router-link>
            </div>
          </div>
          <ContentChart v-if="record.contents"
                        :dataLabels="record.contents.map(function(item){return item.metal;})"
                        :dataValues="record.contents.map(function(item){return item.percentage;})"
                        :large="false"/>
          <p class="card-text" v-if="isLastUpdate"><small class="text-muted">Last updated 3 mins ago</small></p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "RecordCards",
  props: ['records', 'isCardLink', 'isLastUpdate']
}
</script>

<style scoped>

</style>