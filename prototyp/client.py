import socket, sys, os

default_command = ""

if len(sys.argv) < 3:
    ip = input("Ip: ")
    port = int(input("Port: "))
else:
    ip = sys.argv[1]
    port = int(sys.argv[2])

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
while True:
    os.system('clear')
    message = input("Short command: ")
    if message == "":
        message = default_command
    elif message.split()[0] == ":d":
        if len(message.split()) > 1:
            default_command = message.split()[1]
    elif message == ":h":
        input("HELP SCREEN TODO")

    sock.sendto(bytes(message,"utf-8"), (ip, port))
