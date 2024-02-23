<template>
      <aside class="sidebar bg-black p-4 h-100">
        <h1 class="text-white"> COGBEE <font-awesome-icon icon="fa-solid fa-rectangle-list" style="color: #f4013e;" /></h1>
        <hr>
        <router-link to='/dashboard' class="design"><font-awesome-icon icon="fa-solid fa-table-columns" style="color: #f4f5f6;" /> Dashboard</router-link><br>
        <router-link to="/skill" class="design"><font-awesome-icon icon="fa-regular fa-calendar-plus" style="color: #f5f5f5;" /> Skill Assessment</router-link><br>
        <router-link to="" class="design"><font-awesome-icon icon="fa-solid fa-receipt" style="color: #ffffff;" /> Certificates</router-link><br>
        <router-link to="" class="design"><font-awesome-icon icon="fa-solid fa-square-poll-vertical" style="color: #ffffff;" /> Leaderboard</router-link><br>
        <hr>
        <router-link to="" class="design"><font-awesome-icon icon="fa-solid fa-bell" style="color: #fcfcfd;" /> Notifications</router-link><br>
        <router-link to="" class="design"><font-awesome-icon icon="fa-solid fa-life-ring" style="color: #ffffff;" /> Support</router-link><br>
        <router-link to="" class="design"><font-awesome-icon icon="fa-solid fa-gear" style="color: #ffffff;" /> Settings</router-link><br>
      </aside>
</template>

<script setup>
</script>
<style>
.sidebar {
  font-size: 25px;
  transform: rotate(0deg);
}

/*.aside {
  padding: 30px;
  background-color: rgb(0, 9, 11);
  width: 430px;
  height: 50rem;
}*/

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
