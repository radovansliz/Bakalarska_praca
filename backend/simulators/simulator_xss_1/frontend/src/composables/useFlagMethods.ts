import { ref } from "vue"
import { useApiFetch } from "@/composables/useApi"

export default function useFlagMethods() {
  const result = ref<string | null>(null)
  const flagFound = ref(false)
  const flag = ref('')

  // API Method to get Flag
  async function sendRequest() {
    flagFound.value = false
    // call api
    try {
      const { data: apiData, error: renormalizeError } = await useApiFetch(
        'flag'
      )
        .get()
        .json()
      if (renormalizeError.value) {
        flag.value = renormalizeError.value
      } else {
        flagFound.value = true
        flag.value = apiData.value.detail[0][0]
      }
    } catch (e) {
      flag.value = 'Error'
    }
  }

  // Global function getFlag
  async function getFlag() {
    await sendRequest()
  }

  // Assign global function to window
  window.flag = {
    getFlag
  }

  return { result, flagFound, flag, getFlag }
}
