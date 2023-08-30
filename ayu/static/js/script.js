window.onload = function () {
	var app = new Vue({
	  delimiters: ['[[', ']]'],
	  el: '#app',
	  data: {
		messages: [],
		input: '',
		send_blank: false,
		placeholder: 'Send a message to the chatbot...',
	  },
	  created: function () {},
	  methods: {
		add_message: function () {
		  if (this.input.length > 0) {
			var message = {
			  text: this.input,
			  user: true,
			  chat_bot: false,
			};
			this.messages.push(message);
			this.input = '';
  
			//just in case
			this.send_blank = false;
			this.placeholder = 'Send a message to the chatbot...';
  
			fetch('/get-response/', {
			  body: JSON.stringify({ message: message['text'] }),
			  cache: 'no-cache',
			  credentials: 'same-origin',
			  headers: {
				'user-agent': 'Mozilla/4.0 MDN Example',
				'content-type': 'application/json',
			  },
			  method: 'POST',
			  mode: 'cors',
			  redirect: 'follow',
			  referrer: 'no-referrer',
			})
			  .then((response) => response.json())
			  .then((json) => {
				console.log(json);
				if (json.status === 'ok') {
				  var message = {
					text: json.response,
					user: false,
					chat_bot: true,
				  };
				  this.messages.push(message);
				  // Autoscroll to bottom
				  this.$refs.chatContainer.scrollTop = this.$refs.chatContainer.scrollHeight;
				} else {
				  alert('Error: ' + json.error_message);
				}
			  })
			  .catch((error) => {
				console.error('Error:', error);
			  });
		  } else {
			this.send_blank = true;
			this.placeholder = 'Please enter a message.';
		  }
		},
	  },
	});
  };
  