import { ref } from 'vue'
import { useApiFetch } from '@/composables/useApi'

export default function useSendRequest() {
  const response: any = ref(null)
  const loading = ref(false)

  // API Method to get Flag
  async function sendRequest(payloadForm: any) {
    loading.value = true

    // call api
    try {
      const { data: apiData, error: renormalizeError } = await useApiFetch(
        'signin'
      )
        .post({
          form: Object.values(payloadForm).map((element) => element)
        })
        .json()
      if (renormalizeError.value) {
        response.value = { error: renormalizeError.value }
      } else {
        response.value = { results: apiData.value.results }
      }
      loading.value = false
    } catch (e) {
      loading.value = false
      response.value = { error: e }
    }
  }

  return { response, loading, sendRequest }
}
