const net = require("net");

// Create a new socket object
const socket = new net.Socket();

// Connect to the server
socket.connect(8020, "localhost", () => {
  console.log("Connected to server");

  // Send a message to the server
  socket.write("Hello from client");

  // Listen for data received from the server
  socket.on("data", (data) => {
    console.log(data.toString());
  });
});
