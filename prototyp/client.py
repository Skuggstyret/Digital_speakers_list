import socket, sys

if len(sys.argv) < 2:
    print("Ange ip och port som argument <ip> <port>")

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
while True:
    message = input("Short command: ")
    sock.sendto(bytes(message,"utf-8"), (sys.argv[1], int(sys.argv[2])))
