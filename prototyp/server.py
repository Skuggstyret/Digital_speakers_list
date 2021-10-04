import os, toml, sys,threading, datetime
from flask import Flask, jsonify
from flask_api import status
from flask_cors import CORS
import json
from functools import reduce

app = Flask(__name__)
CORS(app)

# Global variable
speaker_lists = [[]]
curr_list = len(speaker_lists) - 1
speakers = []
speaker_lock = threading.Semaphore()


# Class handling information about a speaker
class Speaker:
    def __init__(self, name, number):
        if number.isdigit():
            self.name = name.strip()
            self.number = number
            self.tot_spoken = 0
            self.list_spoken = [0] * (curr_list + 1)
        else:
            raise ValueError("Invalid name or number")

    def isVal(self, v):
        if self.name.lower() == v.lower() or self.number == v:
            return True
        return False

    def raiseHand(self):
        add_to_list(self)

    def lowerHand(self):
        remove_from_list(self)

    def spoken(self):
        remove_from_list(self)
        self.tot_spoken += 1
        self.list_spoken[curr_list] += 1

    def toJSON(self):
        return "{\"name\":\"" + self.name + "\",\"number\":\"" + self.number + "\"}"

# Global helper functions
def speaker_sort_key(s):
    return s.list_spoken


def add_to_list(speaker):
    with speaker_lock:
        if len(list(filter(lambda s: s.isVal(speaker.number), speaker_lists[curr_list]))) == 0:
            speaker_lists[curr_list].append(speaker)
            speaker_lists[curr_list].sort(key=speaker_sort_key)


def remove_from_list(speaker):
    with speaker_lock:
        speaker_lists[curr_list] = [s for s in speaker_lists[curr_list] if not s.isVal(speaker.number)]
    

def getValidSpeaker(name):
    valid_speakers = list(filter(lambda s: s.isVal(name), speakers))
    if len(valid_speakers) == 1:
        return valid_speakers[0]

# Speaker
@app.route("/speaker/get",methods=['GET'])
def getSpeakers():
    return json.dumps(speakers), status.HTTP_200_OK

## adds user to this session, is not presistent
@app.route("/speaker/add/<json_str>", methods=['POST'])
def addSpeaker(json_str):
    d = json.loads(json_str)  

    matching_speakers = list(filter(lambda s: s.number == d['number'], speakers))

    if len(list(matching_speakers)) == 1:
        matching_speakers[0].name = d['name']
        return '', status.HTTP_202_ACCEPTED
    else:
        try:
            speakers.append(Speaker(d['name'], d['number']))
            return '', status.HTTP_201_CREATED
        except ValueError: 
            return '', status.HTTP_400_BAD_REQUEST

# list
@app.route("/list/add/<name>", methods=['POST'])
def addSpeakerToList(name):
    speaker = getValidSpeaker(name)

    if speaker:
        speaker.raiseHand()
        return '', status.HTTP_200_OK
    else:
        try:
            new_speaker = Speaker('', name)
            speakers.append(new_speaker)
            new_speaker.raiseHand()
            return '', status.HTTP_201_CREATED
        except ValueError: 
            return '', status.HTTP_400_BAD_REQUEST


@app.route("/list/remove/<name>",methods=['POST'])
def removeSpeakerFromList(name):
    speaker = getValidSpeaker(name)

    if speaker:
        speaker.lowerHand()
        return '', status.HTTP_200_OK
    else:
        return 'No such speaker', status.HTTP_400_BAD_REQUEST

@app.route("/list",methods=['GET'])
def getSpeakersOnList():
    speaker_list_strings = []

    for sl in speaker_lists:
        speaker_list_strings.append("[" + ','.join(map(lambda s: s.toJSON(), sl)) + "]")

    output = "[" + ",".join(speaker_list_strings) + "]"

    print(output)
    return output, status.HTTP_200_OK


@app.route("/list/next",methods=['POST'])
def nextSpeaker():
    speaker_lists[curr_list][0].spoken()
    return '', status.HTTP_202_ACCEPTED

@app.route("/list/reset", methods=['POST'])
def resetCount():
    speaker_lists[curr_list] = []
    for speaker in speakers:
        speaker.list_spoken = 0

    return '', status.HTTP_200_OK

@app.route("/list/push", methods=['POST'])
def addNextLevelOfList():
    with speaker_lock:
        speaker_lists.append([])

        for s in speakers:
            s.list_spoken.append(0)
        
        global curr_list
        curr_list = len(speaker_lists) - 1
    
    return '', status.HTTP_200_OK

@app.route("/list/pop", methods=['POST'])
def removeCurrLevelOfList():
    with speaker_lock:
        speaker_lists.pop()

        for s in speakers:
            s.list_spoken.pop()

        global curr_list
        curr_list = len(speaker_lists) - 1

    return '', status.HTTP_200_OK

@app.route("/list/leaderboard", methods=['GET'])
def getLeaderboard():
    output = list(map(lambda s: {'name': s.name, 'number': s.number, 'spoken': s.tot_spoken}, 
                sorted(speakers, key=lambda s: s.tot_spoken, reverse=True)))

    return jsonify(output), status.HTTP_200_OK

# meeting
@app.route("/meeting/export/<name>", methods=['POST'])
def export(name = ""):
    if name == "":
        date = datetime.date.today()
        name = date.strftime("%Y-%m-%d")

    with open(name, "x") as f:
        for speaker in speakers:
            f.write("{} - {}\n".format(speaker, speakers[speaker][2]))




# Init stuff
if __name__ == "__main__":
    if len(sys.argv) > 1:
        file_data = toml.load(sys.argv[1])
        with speaker_lock:
            for speaker in file_data["speakers"]:
                speakers[speaker] = [0,0]
    app.run(debug=True, use_reloader=False)
