
import axios from 'axios'

class HttpService {
	get (url, params) {
		if(params) {
			var config = { 
				params: params 
			}
			return axios.get(url, config).then(res => {
				return res.data
			})  
		} else {
			return axios.get(url).then(res => {
				return res.data
			})
		}
	}
	post (url, data) {
		return axios.post(url, data).then(res => {
			return res.data
		})
	}
}

export default new HttpService()
