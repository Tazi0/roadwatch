const websocketUrl = `ws://${import.meta.env.VITE_PROD_URL}/socket`

export const websocket = new WebSocket(websocketUrl)

websocket.onopen = () => {
  console.log('WebSocket connection opened')
}

websocket.onmessage = (event) => {
  console.log('WebSocket message received:', event.data)
}

websocket.onclose = () => {
  console.log('WebSocket connection closed')
}

websocket.onerror = (error) => {
  console.error('WebSocket error:', error)
}
