const chatBox = document.getElementById('chat-box');
const inputBox = document.getElementById('input-box');
const threadId = 'chat_' + Math.random().toString(36).substring(2, 15);

async function sendMessage() {
    const message = inputBox.value.trim();
    if (!message) return;

    const userMsg = document.createElement('div');
    userMsg.textContent = `You: ${message}`;
    chatBox.appendChild(userMsg);
    inputBox.value = '';

    try {
        const response = await axios.post('http://127.0.0.1:8000/chat', {
            message,
            thread_id: threadId
        });
        const botMsg = document.createElement('div');
        botMsg.textContent = `Bot: ${response.data.reply}`;
        chatBox.appendChild(botMsg);
    } catch (error) {
        console.error(error);
        const errMsg = document.createElement('div');
        errMsg.textContent = 'Bot: Error occurred';
        chatBox.appendChild(errMsg);
    }
    chatBox.scrollTop = chatBox.scrollHeight;
}

inputBox.addEventListener('keypress', (e) => {
    if (e.key === 'Enter') sendMessage();
});