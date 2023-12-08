import socket

HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = '!DISCONNECT'
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)


def connect():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(ADDR)
    return client


def send(client, msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))

    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))


def start():
    response = input('Would you like to connect (yes/no)? ')
    if response.lower() != 'yes':
        return

    connection = connect()
    while True:
        msg = input('Message(q for quit): ')

        if msg.lower() == 'q':
            break

        send(connection, msg)

    send(connection, DISCONNECT_MESSAGE)


start()
