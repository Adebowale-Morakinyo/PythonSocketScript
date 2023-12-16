# PythonSocketScript

A simple client-server communication script using Python sockets.

## Files:

- `server.py`: Handles incoming connections and broadcasts messages to all connected clients.
- `client.py`: Connects to the server, sends messages, and allows the user to disconnect.

## Usage:

1. Run `server.py` to start the server.
2. Run multiple instances of `client.py` to connect to the server.
3. Enter messages in the client instances to send them to the server and other connected clients.

## Instructions:

- The server listens on a specified port (default: 5050).
- Clients connect to the server's IP address and port.
- Type `!DISCONNECT` to disconnect a client.
- Type `'q'` in the client to quit and disconnect.

## Notes:

- Threading is used to handle multiple client connections simultaneously.
- The communication is based on a fixed message header length.
