import socket
import argparse

HEADER = 64
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = '!DISCONNECT'


def connect(server, port):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((server, port))
    return client


def send(client, msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))

    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))


def start(server, port):
    connection = connect(server, port)

    while True:
        msg = input('Message (type \'q\' to quit): ')

        if msg.lower() == 'q':
            break

        send(connection, msg)

    send(connection, DISCONNECT_MESSAGE)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Client for C_Python_Socket_Project')
    parser.add_argument('--server', default='localhost', help='Server address')
    parser.add_argument('--port', type=int, default=5050, help='Server port')
    args = parser.parse_args()

    start(args.server, args.port)
