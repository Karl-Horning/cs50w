document.addEventListener('DOMContentLoaded', () => {
    // Connect to WebSocket
    var socket = io.connect(location.protocol + '//' + document.domain + ':' + location.port);

    // Configure buttons when connected
    socket.on('connect', () => {
        // Each button should emit a 'submit vote' event
        document.querySelectorAll('button').forEach(button => {
            button.onclick = () => {
                const selection = button.dataset.vote;
                socket.emit('submit vote', {'selection': selection});
            };
        });
    });

    // Add new vote to unordered list when announced
    socket.on('announce vote', data => {
        const li = document.createElement('li');
        li.innerHTML = `Vote Recorded: ${data.selection}`;
        document.querySelector('#votes').append(li);
    });
});