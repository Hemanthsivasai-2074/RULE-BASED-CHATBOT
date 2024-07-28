const chatMessages = document.querySelector('.chat-messages');
const userInput = document.getElementById('user-input');

function sendMessage() {
    const userMessage = userInput.value;
    if (userMessage.trim() !== '') {
        const messageElement = document.createElement('div');
        messageElement.classList.add('chat-message', 'user-message');
        messageElement.textContent = userMessage;
        chatMessages.appendChild(messageElement);

        // Replace this with your chatbot logic
        const chatbotResponse = "This is a sample chatbot response.";

        const botMessageElement = document.createElement('div');
        botMessageElement.classList.add('chat-message');
        botMessageElement.textContent = chatbotResponse;
        chatMessages.appendChild(botMessageElement);

        userInput.value = '';
    }
}
