<template>
    <div>
        <!-- <h1>{{ doc.data }}</h1> -->
        <div class="container p-3">
            <div class="row g-1 gap-3">
                <div class="card w-25 shadow-lg" v-for="a in doc.data" :key="a">
                    <h3 class="card-title text-center mt-3">
                        {{ a.title }}
                        <span
                            :class="a.level === 'Intermediate' ? 'text-primary' : a.level === 'Basic' ? 'text-success' : 'text-danger'">({{
                                a.level }})</span>
                    </h3>
                    <div class="card-body">
                        <p><span class="text-primary"></span>{{ a.description }} </p>
                    </div>
                    <div class="card-footer">
                        <h6><span>Total Fee :</span> Rs. {{ a.fees }} </h6>
                        <h6><span>Duration :</span>{{ a.duration }} Months </h6>
                        <router-link :to="`/coursedetail/${a.name}`">
                            <Button class="bg-primary text-white font-bold m-auto">View Details</Button>
                        </router-link>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>
<script setup>
import { createListResource } from 'frappe-ui';
const doc = createListResource({
    doctype: 'Course Details',
    fields: ['name', 'title', 'description', 'duration', 'fees', 'level'],
    auto: true,
    onSuccess(doc) {
        console.log(doc)
    },
})
</script>
<style>
.sidebar {
    font-size: 20px;
    transform: rotate(0deg);
}
</style>