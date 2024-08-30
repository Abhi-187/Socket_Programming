const http = require("http");

const server = http.createServer((req, res) => {
  console.log("Request received"); // Log that a request has been received
  res.write("Hello from server\n"); // Write a response to the client
  console.log(req.url); // Log the requested URL

  if (req.url === "/home") {
    return res.end("Welcome to the home page"); // Return a response with "Welcome to the home page" if the requested URL is "/home"
  } else {
    return res.end("Goodbye"); // Return a response with "Goodbye" for any other requested URL
  } // it is good practice to use "return" only res.end also works but it is good practice to use return
});

server.listen(8020, () => {
  console.log("Server started on port 8020"); // Log that the server has started on port 8020
});

//to connect to the server we can use the browser or the client.js file
//the brower will do a get request to the server and the server will respond with the response
//the client.js will do a get request to the server and the server will respond with the response
//the server will log the request and the requested url
