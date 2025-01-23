const chatContainer = document.getElementById('chat-container');
const inputField = document.getElementById('input-field');
const sendButton = document.getElementById('send-button');

sendButton.addEventListener('click', sendMessage);

function sendMessage() {
    const userMessage = inputField.value;
    if (userMessage.trim() === '') return;

    displayMessage(userMessage, 'user');
    inputField.value = '';

    fetch('/api/chat', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ message: userMessage }),
    })
    .then(response => response.json())
    .then(data => {
        displayMessage(data.reply, 'bot');
    })
    .catch(error => {
        console.error('Error:', error);
    });
}

function displayMessage(message, sender) {
    const messageElement = document.createElement('div');
    messageElement.className = sender === 'user' ? 'user-message' : 'bot-message';
    messageElement.textContent = message;
    chatContainer.appendChild(messageElement);
}