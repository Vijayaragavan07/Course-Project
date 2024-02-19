<template>
  <!-- <div class=" py-12 mx-auto h-100">
    <div class="container-fluid flex"> -->
      <aside class="sidebar aside">
        <router-link to='/dashboard' class="design">🏬 Dashboard</router-link><br>
        <router-link to="/skill" class="design">👤 Skill Assessment</router-link><br>
        <router-link to="" class="design">🆑 Certificates</router-link><br>
        <router-link to="" class="design">🔼 Leaderboard</router-link><br>
        <hr>
        <router-link to="" class="design">🎵 Notifications</router-link><br>
        <router-link to="" class="design">🧑‍🦽 Support</router-link><br>
        <router-link to="" class="design">📌 Settings</router-link><br>
      </aside>
    <!-- </div> -->
    <!-- <footer>
      <p class="bg-blue-900 text-center text-white">&copy; Copyrights reserved </p>
  </footer> -->
  <!-- </div> -->
</template>

<script setup>
</script>
<style>
.sidebar {
  font-size: 25px;
  transform: rotate(0deg);
}

.aside {
  padding: 30px;
  background-color: rgb(11, 97, 120);
  width: 430px;
  height: 100rem;
}

.design {
  color: rgb(212, 208, 208) !important;
  text-decoration: none;
}

.nav-item {
  display: inline-block;
  padding: 5px 10px;
  font-size: 22px;
}

.nav-link {
  text-decoration: none;
  color: inherit;
}

.router-link-active {
  color: white;
}

.input-box {
  width: 50%;
  /* Full width */
  padding: 10px;
  /* Add padding */
  border: 1px solid #ccc;
  /* Add border */
  border-radius: 5px;
  /* Add border radius */
  box-sizing: border-box;
  /* Include padding and border in width */
  font-size: 16px;
  /* Set font size */
  outline: none;
  /* Remove default outline */
  margin-left: 450px;
}
</style>
