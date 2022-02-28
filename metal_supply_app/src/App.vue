<template>
  <div id="app">
    <nav class="navbar navbar-expand navbar-dark bg-dark mb-5">
      <router-link to="/" class="navbar-brand">Metal Supply</router-link>
      <div class="navbar-nav mr-auto">
        <li class="nav-item">
          <router-link to="/home" class="nav-link">
            <font-awesome-icon icon="home" /> Home
          </router-link>
        </li>
<!--        <li v-if="showAdminBoard" class="nav-item">-->
<!--          <router-link to="/admin" class="nav-link">Admin Board</router-link>-->
<!--        </li>-->
<!--        <li v-if="showModeratorBoard" class="nav-item">-->
<!--          <router-link to="/mod" class="nav-link">Moderator Board</router-link>-->
<!--        </li>-->
<!--        <li class="nav-item">-->
<!--          <router-link v-if="currentUser" to="/user" class="nav-link">User</router-link>-->
<!--        </li>-->
        <li class="nav-item">
          <router-link v-if="currentUser" to="/records" class="nav-link">Records</router-link>
        </li>
        <li class="nav-item">
          <router-link v-if="currentUser" to="/agents" class="nav-link">Agents</router-link>
        </li>
      </div>

      <div v-if="!currentUser" class="navbar-nav ml-auto">
        <li class="nav-item">
          <router-link to="/register" class="nav-link">
            <font-awesome-icon icon="user-plus" /> Sign Up
          </router-link>
        </li>
        <li class="nav-item">
          <router-link to="/login" class="nav-link">
            <font-awesome-icon icon="sign-in-alt" /> Login
          </router-link>
        </li>
      </div>

      <div v-if="currentUser" class="navbar-nav ml-auto">
        <li class="nav-item">
          <router-link to="/profile" class="nav-link">
            <font-awesome-icon icon="user" />
            {{ currentUser.name }}
          </router-link>
        </li>
        <li class="nav-item">
          <a class="nav-link" @click.prevent="logOut">
            <font-awesome-icon icon="sign-out-alt" /> LogOut
          </a>
        </li>
      </div>
    </nav>

    <div class="container">
      <router-view />
    </div>
  </div>
</template>

<script>
export default {
  computed: {
    currentUser() {
      return this.$store.state.auth.user;
    } //,
    // showWasteOwnerBoard() {
    //   if (this.currentUser && this.currentUser['roles']) {
    //     return this.currentUser['roles'].includes('WASTE_OWNER');
    //   }
    //
    //   return false;
    // },
    // showRecyclerBoard() {
    //   if (this.currentUser && this.currentUser['roles']) {
    //     return this.currentUser['roles'].includes('RECYCLER');
    //   }
    //
    //   return false;
    // },
    // showConverterBoard() {
    //   if (this.currentUser && this.currentUser['roles']) {
    //     return this.currentUser['roles'].includes('CONVERTER');
    //   }
    //
    //   return false;
    // }
  },
  methods: {
    logOut() {
      this.$store.dispatch('auth/logout');
      this.$router.push('/login');
    }
  }
};
</script>
