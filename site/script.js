document.getElementById('send-button').addEventListener('click', function() {
    const userInput = document.getElementById('user-input');
    const chatOutput = document.getElementById('chat-output');
    
    // Create user message bubble
    const userMessage = document.createElement('div');
    userMessage.textContent = userInput.value;
    userMessage.classList.add('user-message');
    chatOutput.appendChild(userMessage);

    // Clear the input field
    userInput.value = '';

    // TODO: Here you would add the code to send the message to the backend and receive the response
});
