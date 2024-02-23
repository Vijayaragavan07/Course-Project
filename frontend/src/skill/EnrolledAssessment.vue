<template>
    <div>
        <pre>

        </pre>
        <div v-for="a in doc.data" :key="a">
            <div v-if="props.name === a.name">
                <h1 class="text-gray-900 font-bold text-[32px]">Course Title : {{ a.title }} ({{ a.level }}) </h1>
                <div class="mt-11 flex flex-row items-center justify-between">
                    <div class="flex flex-col space-y-3">
                        <h2 class="text-gray-700 text-base font-bold uppercase">Duration</h2>
                        <p class="text-gray-600 text-xl font-semibold uppercase">{{ a.duration }} months</p>
                    </div>
                    <div class="flex flex-col space-y-3">
                        <h2 class="text-gray-700 text-base font-bold uppercase">Level</h2>
                        <p class="text-gray-600 text-xl font-semibold uppercase">{{ a.level }} </p>
                    </div>
                </div>
                <div>
                    <h3 class="mt-5">Questions</h3>
                    <form>
                        <div class="row row-cols- g-1 gap-4 m-2">
                            <div class="card" v-for="(q, index) in question.data" :key="index">
                                <ul class="list-group list-group-flush">
                                    <li class="list-group-item">
                                        <h4 class="font-bold">{{ q.sno }} </h4>
                                        <p>{{ q.question }}</p>
                                        <input type="text" placeholder="Ans:" class="w-100" v-model="newData[index]">
                                        <Button @click="saveAnswer($event, index)">Save</Button>
                                    </li>
                                </ul>
                            </div>
                        </div>
                        <Button type="submit" class="bg-green-700 text-white font-bold"
                            @click="finalsubmit($event)">Submit</Button>
                    </form>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup>
import { createListResource } from 'frappe-ui';
import { defineProps, reactive } from 'vue';

const props = defineProps({
    name: {
        type: String,
        required: true
    },
    title: {
        type: String,
        required: true
    },
    level: {
        type: String,
        required: true
    }
});
console.log('Props data',props.name,props.title, props.level);

const doc = createListResource({
    name: props.name,
    doctype: 'Course Details',
    fields: ['name', 'title', 'fees', 'description', 'duration', 'level'],
    auto: true,
    onSuccess(doc) {
        console.log('course page', doc);
    },
});

const question = reactive(createListResource({
    doctype: 'Questions',
    fields: ['name', 'question', 'sno'],
    auto: true,
    onSuccess(doc) {
        console.log('question page', doc);
    }
}));
console.log('hi vijay', question.fields)

const newData = reactive([]);

const finalAnswer = createListResource({
    doctype: "Answers",
});

let answers = []
function saveAnswer(event, index) {
    event.preventDefault(); // Prevent default form submission

    answers.push({
        questions: question.data[index].question,
        answer: newData[index],
        sno: question.data[index].sno,
    });
    newData.forEach((_, index) => {
        newData[index] = '';
    });
    console.log('savebutton answer', answers);
}

function finalsubmit(e) {
    e.preventDefault();
    console.log('final submission', answers);
    finalAnswer.insert.submit({
        items: answers,
        title: props.title,
        level: props.level
    });
    answers = []
}

</script>

<style scoped>
/* Add your styles here */
</style>
