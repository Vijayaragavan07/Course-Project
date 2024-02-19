import { createRouter, createWebHistory } from 'vue-router'
import { session } from './data/session'
import { userResource } from '@/data/user'

const routes = [
  {
    path: '/',
    name: 'Home',
    components: {
      default: () => import('@/home/HomePage.vue'),
      sidebar: () => import('@/pages/SideBar.vue'),
    }
  },
  {
    path: '/userpage',
    name: 'UserPage',
    components: {
      default: () => import('@/users/UserPage.vue'),
      sidebar: () => import('@/pages/SideBar.vue'),
    }

  },
  {
    path: '/account/login',
    name: 'Login',
    components: {
      default: () => import('@/pages/Login.vue'),
      sidebar: () => import('@/pages/SideBar.vue'),

    }
  },
  {
    path: '/dashboard',
    name: 'DashBoard',
    components: {
      default: () => import('@/dashboard/DashBoard.vue'),
      sidebar: () => import('@/pages/SideBar.vue'),

    },
  },
  {
    path: '/coursedetail/:name',
    name: 'CourseDetail',
    components: {
      default: () => import('@/dashboard/CourseDetail.vue'),
      sidebar: () => import('@/pages/SideBar.vue'),

    },
    props:true
  },
  {
    path: '/skill',
    name: 'SkillAssessment',
    components: {
      default: () => import('@/skill/SkillAssessment.vue'),
      sidebar: () => import('@/pages/SideBar.vue'),

    },
  }
]

let router = createRouter({
  history: createWebHistory('/frontend'),
  routes,
})

router.beforeEach(async (to, from, next) => {
  let isLoggedIn = session.isLoggedIn
  try {
    await userResource.promise
  } catch (error) {
    isLoggedIn = false
  }

  if (to.name === 'Login' && isLoggedIn) {
    next({ name: 'Home' })
  } else if (to.name !== 'Login' && !isLoggedIn) {
    next({ name: 'Login' })
  } else {
    next()
  }
})


export default router
