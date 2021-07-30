import os, toml, sys, socket, argparse, threading, time

# TODO: Kanske borde flyttas till config file, men känns onödigt
# i nuläget
HOST = ''  # Standard loopback interface address (localhost)
PORT = 20001        # Port to listen on (non-privileged ports are > 1023)

# Global variable
speaker_list = []
speakers = {}
terminal_lock = threading.Semaphore()
speaker_lock = threading.Semaphore()


clear = lambda: os.system('clear')

def addSpeaker():
    with terminal_lock:
        while True:
            tag = input("Välj kort kommando för medlemen:")
            if tag in speakers:
                print("Tag används redan")
            else:
                break
        name = input("Namn på medlemen: ")
        speakers[tag] = [name,0]

def speakerFromFile(path):
    file_data = toml.load(path)
    with speaker_lock:
        for speaker in file_data["talar"]:
            speakers[speaker[0]] = [speaker[1],0]


def addSpeakerToList(tag, remote=False):
    if tag in speakers:
        with speaker_lock:
            if tag in speaker_list:
                return False
            speaker_list.append(tag)
            speaker_list.sort(key=lambda x: speakers[x][1])
            return True
    else:
        if not remote:
            with terminal_lock:
                print("Ingen sådan talare")
        return False

def nextSpeaker():
    with speaker_lock:
        global speaker_list
        speaker = speakers[speaker_list[0]]
        speaker[1] += 1
        speaker_list = speaker_list[1:]

def resetCount():
    with terminal_lock:
        if len(speaker_list) != 0:
            while True:
                sure = input("Talar listan är inte tom är du säker?(y/n)")
                if sure == "n":
                    return
                elif sure == "y":
                    break

        with speaker_lock:
            for speaker in speakers:
                speakers[speaker][1] = 0

def udpListner():
    # Letar efter för char i UDP medelande och lägger till i
    # talar listan.

    UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

    UDPServerSocket.bind((HOST, PORT))

    t = threading.currentThread()
    while getattr(t, "do_run", True):
        # TODO: Fixa v, block till den från input och
        # stänger därför inte ner som den ska.
        bytesAddressPair = UDPServerSocket.recvfrom(1024)

        message = bytesAddressPair[0]
        address = bytesAddressPair[1]

        tag = chr(message[0])

        if (addSpeakerToList(tag,True)):
            render()


def render():
    with terminal_lock:
        clear()
        print("Skuggstyret talarlista")
        print("----------------------")

        for speaker in speaker_list:
            print(speakers[speaker][0])

def main(argv):
    udp_lister =  threading.Thread(target=udpListner, daemon=True)
    udp_lister.start()
    if len(argv) != 0:
        speakerFromFile(argv[0])
    while True:
        render()
        command = input()
        if command == ":q":
            udp_lister.do_run = False
            exit()
        elif command == ":a":
            addSpeaker()
        elif command == ":n":
            nextSpeaker()
        elif command == ":r":
            resetCount()
        elif command == ":h":
            print("Hjälp Sidan")
            print("-----------")
            print(""":a Lägga till nu talare för detta möte.\n
:n Visar nästa talare, aka ta bort nuvarande.\n
:r Rensar alla talares streck\n
:q Stänger in programet.\n
:h Visar nu varande info.\n\n
Programmet kan även kör med en toml file som argument,\n
vilket tillåter använder allt ladda talare. Filen ska \n
vara formaterade enligt:
talare = [
    [<tag1>,<namn1>],
    [<tag2>,<namn2>],
    ...
    ]
            """)
            input("Press any button to continue")

        else:
            addSpeakerToList(command)

if __name__ == "__main__":
    main(sys.argv[1:])