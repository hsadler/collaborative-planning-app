
import io from 'socket.io-client'

class SocketService {
  io (url, options) {
    return io(url, options)
  }
}

export default new SocketService()
