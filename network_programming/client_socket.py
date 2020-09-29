import socket

HOST = 'localhost'    # The remote host
PORT = 5000              # The same port as used by the server
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    data = b''
    while data != b'Connected':
        req = input("Enter password to connect: ")
        s.sendall(bytes(req, encoding='utf-8'))
        data = s.recv(1024)
        print(data)
        if data == b"You failed to connect, too many attempts":
            break

