const net = require("net");

// Create a TCP server
const socket_server = net.createServer((socket) => {
  console.log("Client connected");

  // Event listener for receiving data from the client
  socket.on("data", (data) => {
    console.log(data.toString());
    socket.write("Hello from server");
  });
});

// Start the server and listen on port 8020
socket_server.listen(8020, () => {
  console.log("Server started on port 8020");
});
