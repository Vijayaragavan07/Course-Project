<template>
  <div class="container-fluid">
    <nav class="bg-light">
      <ul class="flex items-center">
        <li class="nav-item flex items-center ">
          <b class="mt-5">
            <font-awesome-icon class="p-1" icon="fa-solid fa-circle" style="color: #f10943;" />
            <font-awesome-icon class="p-1" icon="fa-solid fa-circle" style="color: #fc9904;" />
            <font-awesome-icon class="p-1" icon="fa-solid fa-circle" style="color: #04f304;" />
          </b>
        </li>
        <li class="m-auto mt-1">
          <p class="border p-1 bg-gray-200 w-64 rounded-lg  flex items-center justify-center"><font-awesome-icon icon="fa-solid fa-lock" style="color: #5b5c5e;" class="ms-5"/>  app.cogbee.io<font-awesome-icon icon="fa-solid fa-rotate-right" style="color: #1b1616;" class="ms-5"/></p></li>
      </ul>
    </nav>
        <div class="row">
      <div class="col-2">
        <router-view name="sidebar" />
      </div>
      <div class="col-10 bg-white">
        <router-view />
      </div>
      <!-- <p class="bg-blue-900 text-center text-white">&copy; Copyrights reserved </p> -->
    </div>
  </div></template>
