import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";
import "bootstrap";
import "bootstrap/dist/css/bootstrap.min.css";
import "bootstrap-select"
import { FontAwesomeIcon } from './plugins/font-awesome'
import  VueGoogleMaps from '@fawmi/vue-google-maps'
import RecordCards from "@/components/RecordCards";
import ContentChart from "@/components/ContentChart";


createApp(App)
    .use(router)
    .use(store)
    .use(VueGoogleMaps, {
        load: {
            key: 'AIzaSyCeog1wzuKJwMOgd3_gX-nwmuCf1liBW-M',
            libraries: "visualization"
        },
    })
    .component("font-awesome-icon", FontAwesomeIcon)
    .component("RecordCards", RecordCards)
    .component("ContentChart", ContentChart)
    .mount("#app");
