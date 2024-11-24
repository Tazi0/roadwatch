import axios from 'axios'

export const apiClient = axios.create({
  baseURL: import.meta.env.VITE_PROD_URL + '/api',
  headers: {
    'Content-Type': 'application/json',
  },
})

// TODO: replace object with the type of the response
export const getExample = async (id: string): Promise<object> => {
  return apiClient.get(`/example/${id}`).then((response) => response.data) as Promise<object>
}
