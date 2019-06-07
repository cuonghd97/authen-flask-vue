<template>
  <div>
    <h3>Dashboard</h3>
    <div>
      <button v-on:click="getProfile">Profile</button>
    </div>
    <div>
      <button v-on:click="postProfile">Post Profile</button>
    </div>
    <a href="#" v-on:click="logoutAccess">Logout</a>
  </div>
</template>
<script>
import Axios from 'axios'
export default {
  methods: {
    logoutAccess: function(e) {
      e.preventDefault();
      const url = "http://localhost:5000/logout/access";
      const token = localStorage.getItem("jwt")
      Axios.defaults.headers.common["Authorization"] = `Bearer ${token}`
      Axios
        .post(url, {
          headers: {
            "Content-Type": "application/json",
          }
        })
        .then(res => {
          console.log(res);
          this.$router.push("login");
        });
    },
    getProfile: function() {
      const url = "http://localhost:5000/profile";
      const token = localStorage.getItem("jwt")
      Axios
        .get(url, {
          headers: {
            "Authorization": `Bearer ${token}`,
            "Content-Type": "application/json",
          }
        })
        .then(res => {
          console.log(res);
        });
    },
    postProfile: function() {
      const url = "http://localhost:5000/profile";
      const token = localStorage.getItem("jwt")
      // Axios.defaults.headers.common["Authorization"] = `Bearer ${token}`
      // Axios.post(url)
        // .then(res => {
          // console.log(res)
        // })
      Axios.post(url, {
        headers: {
          "Authorization": `Bearer ${token}`,
          'Content-Type': 'application/json',
        }
      })
        .then(res => {
          console.log(res)
        })
    }
  }
};
</script>
