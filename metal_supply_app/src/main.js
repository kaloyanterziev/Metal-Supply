import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";
import "bootstrap";
import "bootstrap/dist/css/bootstrap.min.css";
import { FontAwesomeIcon } from './plugins/font-awesome'
import  VueGoogleMaps from '@fawmi/vue-google-maps'


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
    .mount("#app");
