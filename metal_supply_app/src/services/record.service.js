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

    transferRecord(record_id, receiving_agent_id, percentage) {
        return axios.post('/records/' + record_id + '/transfer', {
            receiving_agent: receiving_agent_id,
            percentage: parseFloat(percentage)
        }, {headers: authHeader()})
    }

    linkRecord(record_id, next_record_id) {
        return axios.post('/records/' + record_id + '/link/' + next_record_id, {}, {headers: authHeader()})
    }
}

export default new RecordService();