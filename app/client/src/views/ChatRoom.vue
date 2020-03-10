<template>
	<div class="chat-room-container">

		<h1>Chat Room</h1>

		<ul class="messages">
			<li v-for="(message, index) in messages" :key="index">{{ message }}</li>
		</ul>
		
		<form @submit.prevent="handleSubmit">
			<input 
				autocomplete="off" 
				v-model="newMessage" 
			/><button type="submit">Send</button>
		</form>

	</div>
</template>

<script>
import services from '@/services'

export default {
	name: 'ChatRoom',
	props: {},
	data () {
		return {
			httpService: services.use('httpService'),
			socketService: services.use('socketService'),
			socket: null,
			newMessage: "",
			messages: []
		}
	},
	methods: {
		handleSubmit () {
			this.socket.emit('chat message', this.newMessage);
			this.newMessage = '';
		}
	},
	created () {
		this.socket = this.socketService.io()
		this.socket.on('chat message', (msg) => {
			this.messages.push(msg)
		});
	}
}
</script>

<style scoped lang="scss">
	div.chat-room-container {

		* { margin: 0; padding: 0; box-sizing: border-box; }
		form { background: #000; padding: 3px; 
			position: fixed; bottom: 0; width: 100%; }
		form input { border: 0; padding: 10px; 
			width: 90%; margin-right: .5%; }
		form button { width: 9%; background: rgb(130, 224, 255); 
			border: none; padding: 10px; }

		ul.messages {
			list-style-type: none; 
			margin: 0; 
			padding: 0;
			margin-bottom: 40px;
			li { 
				padding: 5px 10px;
				:nth-child(odd) { 
					background: #eee; 
				}
			}
		}

	}
</style>
