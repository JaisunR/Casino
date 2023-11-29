import socket
import threading


def client(message_callback):
    server_address = '127.0.0.1'
    server_port = 12000

    try:
        socket_instance = socket.socket()
        socket_instance.connect((server_address, server_port))
        threading.Thread(target=handle_messages, args=[socket_instance, message_callback]).start()
    except Exception as e:
        print(f'Error connecting to server socket {e}')
        socket_instance.close()
        return None

    return socket_instance

def handle_messages(connection, message_callback):
    while True:
        try:
            msg = connection.recv(1024)
            if msg:
                decoded_msg = msg.decode()
                message_callback(decoded_msg)
            else:
                connection.close()
                break
        except Exception as e:
            print(f'Error handling message from server: {e}')
            connection.close()
            break
