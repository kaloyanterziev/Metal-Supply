import axios from 'axios';
import authHeader from './auth-header';


class RecordService {
    getAllRecords() {
        return axios.get('/records');
    }

    getRecord(id) {
        return axios.get('/records/' + id, { headers: authHeader() });
    }

    createRecord(record) {
        return axios.post('/records', {
            latitude: record.latitude,
            longitude: record.longitude,
            material_type: record.material_type,
            material_origin: record.material_origin,
            contents: record.contents,
            tonnes: record.tonnes,
            public: record.public
        }, { headers: authHeader() });
    }

    updateRecordLocation(record_id, latitude, longitude) {
        return axios.post('/records/' + record_id + '/location', {
            latitude: latitude,
            longitude: longitude
        }, {headers: authHeader()})
    }
}

export default new RecordService();