# CustomSocketProject

A basic client-server communication project with a C server and a Python client.

## Files:

- `server.c`: Handles incoming connections, messages, and uses threading for concurrency.
- `client.py`: Connects to the C server, sends messages, and allows clean disconnection.

## Usage:

1. Compile `server.c` on your terminal using a C compiler (e.g., `gcc -o server server.c -lpthread`).
2. Run `./server` to start the C server.
3. Run `python client.py` to start the Python client.
4. Enter messages in the client to send them to the C server and other connected clients.

## Instructions:

- The C server is multithreaded, allowing multiple client connections.
- Modify the server's code to include additional features or configurations.
- Use command-line arguments in the client to specify server address, port, etc.
