import axios from 'axios'
import { API_BASE_URL } from '@/config'

const api = axios.create({
  baseURL: API_BASE_URL,
  timeout: 5000
})

export const getMotorException = () => api.get('/getdata/motorexception')