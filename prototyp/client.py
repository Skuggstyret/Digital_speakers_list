import socket, sys, os

if len(sys.argv) < 2:
    ip = input("Ip: ")
    port = int(input("Port: "))
else:
    ip = sys.argv[1]
    port = int(sys.argv[2])

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
while True:
    os.system('clear')
    message = input("Short command: ")
    sock.sendto(bytes(message,"utf-8"), (ip, port))
