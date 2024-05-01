// This is a JavaScript comment
// Define a function to handle sending messages
function sendMessage() {
    var message = document.getElementById('message-input').value.trim();
    if (message === '') return;

    document.getElementById('chat-display').innerHTML += "<p>You: " + message + "</p>";

    // Send message to backend server
    fetch('/chatbot', {
        method: 'POST',
        body: JSON.stringify({ message: message }),
        headers: {
            'Content-Type': 'application/json'
        }
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('chat-display').innerHTML += "<p>Chatbot: " + data.response + "</p>";
    });

    document.getElementById('message-input').value = '';
}
