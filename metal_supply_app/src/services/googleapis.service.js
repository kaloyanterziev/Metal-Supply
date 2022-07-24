import axios from 'axios';


class GoogleApisService {
    reverseGeocoding(lat, lng) {
        return axios.get('https://maps.googleapis.com/maps/api/geocode/json?latlng=' + lat + ',' + lng +'&key=' +
            process.env.GOOGLE_API_KEY +'&result_type=administrative_area_level_1');
    }
}

export default new GoogleApisService();