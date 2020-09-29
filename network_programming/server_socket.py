import socket

HOST = 'localhost'                 # Symbolic name meaning all available interfaces
PORT = 5000              # Arbitrary non-privileged port
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    numb_of_attempts = 5
    s.bind((HOST, PORT))
    s.listen(1)
    print("Listenting on " + HOST + "\\" + str(PORT))
    conn, addr = s.accept()
    with conn:
        print('Trying to connect with ', addr)
        received_password = 0
        while received_password != 12345 and numb_of_attempts > 0:
            received_password = int(conn.recv(1024))
            if received_password != 12345:
                numb_of_attempts-=1
                if(numb_of_attempts > 0):
                    conn.sendall(b"Wrong password")
                else:
                    conn.sendall(b"You failed to connect, too many attempts")
                print("They tried to connect and failed with psw: " + str(received_password))
            else:
                conn.sendall(b"Connected")
        print("They failed to connect, connection lost")