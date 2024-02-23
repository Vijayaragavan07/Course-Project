import './index.css'
import 'bootstrap/dist/css/bootstrap.css'
/* import the fontawesome core */
import { library } from '@fortawesome/fontawesome-svg-core'
/* import font awesome icon component */
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
import { faMagnifyingGlass } from '@fortawesome/free-solid-svg-icons'
import { faPuzzlePiece } from '@fortawesome/free-solid-svg-icons'
import {faHandsHoldingCircle} from '@fortawesome/free-solid-svg-icons'
import {faCalendarCheck} from '@fortawesome/free-solid-svg-icons'
import { faSpinner } from '@fortawesome/free-solid-svg-icons'
import { faTableColumns } from '@fortawesome/free-solid-svg-icons'
import { faCalendarPlus } from '@fortawesome/free-regular-svg-icons'
import { faSquarePollVertical } from '@fortawesome/free-solid-svg-icons'
import { faReceipt } from '@fortawesome/free-solid-svg-icons'
import { faBell } from '@fortawesome/free-solid-svg-icons'
import { faLifeRing } from '@fortawesome/free-solid-svg-icons'
import { faGear } from '@fortawesome/free-solid-svg-icons'
import { faCircle } from '@fortawesome/free-solid-svg-icons'
import { faLock } from '@fortawesome/free-solid-svg-icons'
import { faRotateRight } from '@fortawesome/free-solid-svg-icons'
import { faRectangleList } from '@fortawesome/free-solid-svg-icons'
import { createApp } from 'vue'
import router from './router'
import App from './App.vue'

library.add(
  faMagnifyingGlass,
  faPuzzlePiece,
  faHandsHoldingCircle,
  faCalendarCheck,
  faSpinner,
  faTableColumns,
  faCalendarPlus,
  faSquarePollVertical,
  faReceipt,
  faBell,
  faLifeRing,
  faGear,
  faCircle,
  faLock,
  faRotateRight,
  faRectangleList
)

import {
  Button,
  Card,
  Input,
  setConfig,
  frappeRequest,
  resourcesPlugin,
} from 'frappe-ui'

let app = createApp(App)

setConfig('resourceFetcher', frappeRequest)

app.use(router)
app.use(resourcesPlugin)
app.component('font-awesome-icon', FontAwesomeIcon)
app.component('Button', Button)
app.component('Card', Card)
app.component('Input', Input)
app.mount('#app')
