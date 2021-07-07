import os, toml, sys

speaker_list = []
speakers = {}

clear = lambda: os.system('clear')

def addSpeaker():
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
    for speaker in file_data["talar"]:
        speakers[speaker[0]] = [speaker[1],0]

def printSpeakerList():
    for speaker in speaker_list:
        print(speakers[speaker][0])

def addSpeakerToList(tag):
    if tag in speakers:
        speaker_list.append(tag)
        speaker_list.sort(key=lambda x: speakers[x][1])
    else:
        print("Ingen sådan talare")

def nextSpeaker():
    global speaker_list
    speaker = speakers[speaker_list[0]]
    speaker[1] += 1
    speaker_list = speaker_list[1:]

def resetCount():
    if len(speaker_list) != 0:
        while True:
            sure = input("Talar listan är inte tom är du säker?(y/n)")
            if sure == "n":
                return
            elif sure == "y":
                break

    for speaker in speakers:
        speakers[speaker][1] = 0

def main(argv):
    if len(argv) != 0:
        speakerFromFile(argv[0])
    while True:
        clear()
        print("Skuggstyret talarlista")
        print("----------------------")

        printSpeakerList()

        command = input()

        if command == ":q":
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
