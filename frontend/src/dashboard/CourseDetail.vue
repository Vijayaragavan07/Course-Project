<template>
    <div>
        <h1 class="text-center mt-5">Course Full Details</h1>
         <div class="container p-3 text-center"> 
            <div class="row g-1 gap-3" v-for="a of doc.data" :key="a">
                <div class="card w-25 shadow-lg" v-if="props.name === a.name">
                    <h3 class="card-title text-center mt-3">
                        {{ a.title }}
                        <span :class="a.level === 'Intermediate'?'text-primary':a.level === 'Basic'?'text-success':'text-danger'">({{ a.level }})</span>
                    </h3>
                    <div class="card-body">
                        <p><span class="text-primary"></span>{{ a.description }} </p>
                    </div>
                    <div class="card-footer">
                        <h6><span>Total Fee :</span> Rs. {{ a.fees }} </h6>
                        <h6><span>Duration :</span>{{ a.duration }} Months </h6>
                        <router-link :to="`/skill`">
                            <Button class="bg-primary text-white font-bold m-auto">Enroll Now</Button>
                        </router-link>
                    </div>
                </div>
            </div>
        </div> 

    </div>
</template>
<script setup>
import { createListResource } from 'frappe-ui';
import { defineProps } from 'vue';

const props = defineProps({name:String})

const doc = createListResource({
    name:props.name,
    doctype:'Course Details',
    fields:['name','title','fees','description','duration','level'],
    auto: true,
    onSuccess(doc) {
        console.log(doc)
    },

})


</script>
<style>

</style>