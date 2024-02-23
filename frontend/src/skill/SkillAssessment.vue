<template>
    <div>
        <div class="border-2 bg-white">
            <div class="row">
                <div class="col-6">
                    <h5 class="float-start pt-2 ps-2">Skill Assessment</h5>
                </div>
                <div class="col-6">
                    <input type="text" placeholder="Search.." class="float-right border-2 rounded">
                </div>
            </div>
        </div>
        <div>
            <div>
                <div class="row">
                    <div class="col-9">
                        <h4 class="font-bold m-2">My Assessment</h4>
                        <div class="row row-cols-3 g-1 m-2">
                            <template v-for="test in doc.data">
                                <template v-for="check in retrievingData.data">
                                    <template v-if="test.title === check.title && test.level === check.level">
                                        <div class="col">
                                            <div class="card" style="width: 18rem;">
                                                <div class="row">
                                                    <div class="col-9">
                                                        <h4 class="card-title font-bold mt-3 ms-2">{{ test.title }} ({{
                                                            test.level
                                                        }})</h4>
                                                        <div class="card-body">
                                                            <p class="text-gray-600 font-bold">{{ test.description }} </p>
                                                        </div>
                                                    </div>
                                                    <div class="col-3">
                                                        <font-awesome-icon icon="fa-solid fa-spinner"
                                                            class="fontHeight mt-3" style="color: #10e028;" />
                                                    </div>
                                                </div>
                                                <div class="card-footer">
                                                    <div class="row font-bold text-gray-600">
                                                        <div class="col-6">
                                                            <p>Attempts</p>
                                                            <p>5</p>
                                                        </div>
                                                        <div class="col-3">
                                                            <p>Test</p>
                                                            <p>15</p>
                                                        </div>
                                                        <div class="col-3 float-left">
                                                            <img :src="test.image" class="corner-image" alt="jkjkj">
                                                        </div>
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
                                    </template>
                                </template>
                            </template>
                        </div>
                        <h4 class="font-bold m-2 pt-2">Get Your Skills Certified</h4>
                        <div class="row row-cols-3 g-2 gap-5 m-2">
                            <div class="card" style="width: 18rem;" v-for="a in doc.data" :key="a">
                                <h4 class="card-title font-bold mt-3 ms-2">{{ a.title }} ({{ a.level }})</h4>
                                <div class="card-body">
                                    <p>{{ a.description }}</p>
                                    <p
                                        class="border border-orange-400 rounded-lg w-50 bg-orange-100 m-1 text-center text-orange-700 font-bold ">
                                        {{ a.max_time }} </p>
                                </div>
                                <div class="card-footer">
                                    <router-link :to="{
                                        name: 'EnrolledAssessment',
                                        params: { name: a.name, title: a.title, level: a.level }
                                    }"><Button class="border"><b>Start
                                                Assessment</b></Button></router-link>
                                    <span class="float-end"><img
                                            :src="a.image"
                                            class="corner-image" alt="jkjkj"></span>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="col-2 float-start">
                        <div class="mt-5">
                            <div class="card" style="width: 18rem;">
                                <ul class="list-group list-group-flush">
                                    <li class="list-group-item">
                                        <h4 class="font-bold">Your Stats</h4>
                                        <p><font-awesome-icon icon="fa-solid fa-puzzle-piece" style="color: #9b83e2;"
                                                class="fontHeight" /><span class="ms-3"> Problem Solved<br><b
                                                    class="ms-5">15</b></span></p>
                                        <p><font-awesome-icon icon="fa-solid fa-hands-holding-circle"
                                                style="color: #74C0FC;" class="fontHeight" /><span class="ms-3">Points
                                                Collected<br><b class="ms-5">275</b></span></p>
                                        <p><font-awesome-icon icon="fa-solid fa-calendar-check" class="fontHeight"
                                                style="color: #e98716;" /> <span class="ms-3">Solution Submitted<br><b
                                                    class="ms-5">15</b></span></p>
                                    </li>
                                    <li class="list-group-item">
                                        <div class="row">
                                            <div class="col-2">
                                                <font-awesome-icon icon="fa-solid fa-spinner" class="fontHeight"
                                                    style="color: #10e028;" />
                                                <div class="circle-percentage__text"></div>
                                            </div>
                                            <div class="col-10">
                                                <b> Complete Your Profile</b><br> Add Your Work Experience
                                            </div>
                                        </div>
                                    </li>
                                </ul>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>

    </div>
</template>
<script setup>
import { createDocumentResource, createListResource } from 'frappe-ui';
import { ref, computed } from 'vue';
const doc = createListResource({
    doctype: 'Course Details',
    fields: ['name', 'title', 'description', 'duration', 'fees', 'level', 'max_time','image'],
    auto: true,
    onSuccess(doc) {
        console.log(doc)
    },
})
const completion = ref('70');

const retrievingData = createListResource({
    doctype: 'Answers',
    fields: ['name', 'title', 'level',],
    auto: true,
    insert: {
        onsuccess(doc) {
            console.log("Answering completed", doc);
        }
    },
});
console.log('parent checking', doc);

// const getChildDocument = computed(() => {
//     if(retrievingData.data){
//         let childData = {}
//         for(const a of retrievingData.data){
//             let doc = createDocumentResource({
//                 doctype: 'Answers',
//                 name: a.name,
//                 fields: ['name', 'items'],
//             })
//             childData[a.name] = doc
//         }
//     }
//     return childData
// })






// const childResources = []
// const retrievingChildData = createListResource({
//     doctype: 'Answers',
//     fields: ['name', 'title', 'level'],
//     auto: true,
//     onSuccess(docs) {
//         console.log('All documents from Answers doctype:', docs);

//         docs.forEach((doc) => {
//             const childResource = createListResource({
//                 doctype: 'Answers Child', // Adjust to your child doctype name
//                 name:'ANS0001',
//                 filters: [['items', '=', doc.name]], // Adjust to your parent field name in the child doctype
//                 fields: ['sno', 'questions','answer'], // Specify fields from the child doctype
//                 auto: true,
//                 onSuccess(childDocs) {
//                     console.log('Child documents for parent document:', childDocs);
//                     // Process child documents as needed
//                 },
//                 onError(error) {
//                     console.error('Error fetching child documents:', error);
//                 }
//             });
//             childResources.push(childResource)
//             console.log('child document',childResource);
//         });
//     },
//     onError(error) {
//         console.error('Error fetching documents from Answers doctype:', error);
//     }
// });
// console.log('checking parent', retrievingChildData);
// console.log('checking child data', childResources);
</script>

<style scoped>
.fontHeight {
    height: 30px;
}

.circle-percentage {
    position: relative;
    width: 100px;
    height: 100px;
}

.circle-percentage__progress {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    clip: rect(0, 100px, 100px, 50px);
    /* Hide the left half */
}

.circle-percentage__fill {
    position: absolute;
    width: 100%;
    height: 100%;
    clip: rect(0, 50px, 100px, 0);
    /* Clip the right half */
    background-color: #4caf50;
    /* Completed portion color */
    border-radius: 50%;
    /* Make it a circle */
}

.circle-percentage__text {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    font-size: 16px;
}

.card {
    position: relative;
    /* Ensure the card serves as the positioning context */
}

.corner-image {
    position: absolute;
    /* top: 0;*/
    right: 0;
    max-width: 350px;
    height: 35px;
}
</style>