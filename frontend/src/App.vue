<template>
  <div class="container-fluid">
    <div class="row">
      <div class="col-3">
        <router-view name="sidebar" />
      </div>
      <div class="col-9 bg-dark-subtle">
        <nav class="bg-light">
          <router-link to='/userpage' class="float-right btn btn-primary font-bold m-1"><button
              class="font-bold text-white">Login</button></router-link>
          <ul class="">
            <li class="nav-item">COGBEE</li>
            <li class="nav-item">Online Courses</li>
            <li class="nav-item">
            </li>
            <li class="">
            </li>
          </ul>
        </nav>
        <router-view />
      </div>
      <p class="bg-blue-900 text-center text-white">&copy; Copyrights reserved </p>
    </div>
  </div>
</template>
