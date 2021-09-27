import os, toml, sys,threading, datetime
from flask import Flask, jsonify
from flask_api import status
import json
from functools import reduce

app = Flask(__name__)

# Global variable
speaker_lists = [[],[]]
speakers = {}
speaker_lock = threading.Semaphore()

# TODO: Byt till två talarlistor

# Speaker
@app.route("/speaker/get",methods=['GET'])
def getSpeakers():
    return json.dumps(speakers), status.HTTP_200_OK

## adds user to this session, is not presistent
@app.route("/speaker/add/<name>", methods=['POST'])
def addSpeaker(name):
    speakers[name] = [0,0]

# list
@app.route("/list/add/<name>", methods=['POST'])
def addSpeakerToList(name):
    if name in speakers:
        with speaker_lock:
            if name in speaker_lists[0] or name in speaker_lists[1]:
                return 'Speaker already on list', status.HTTP_400_BAD_REQUEST
            index = 0
            if speakers[name][0] > 0:
                temp = (reduce(lambda x,y: [x[0]+y[0], x[1]+y[1]], map(lambda x:(speakers[x][0],1) ,speakers), [0,0]))
                index = int(speakers[name][0] > (temp[0]/temp[1])/2)
            speaker_lists[index].append(name)
            return 'Speaker added',status.HTTP_202_ACCEPTED
    else:
        return 'No such speaker', status.HTTP_400_BAD_REQUEST

@app.route("/list/remove/<name>",methods=['POST'])
def removeSpeakerFromList(name):
    if name in speakers:
        with speaker_lock:
            index = 0
            if name not in speaker_lists[0]:
                index = 1
                if name not in speaker_lists[1]:
                    return 'No such speaker on list', status.HTTP_400_BAD_REQUEST
            speaker_lists[index].remove(name)
            return 'Speaker removed', status.HTTP_200_OK
    else:
        return 'No such speaker', status.HTTP_400_BAD_REQUEST

@app.route("/list/get",methods=['GET'])
def getSpeakersOnList():
    return jsonify(data=speaker_lists), status.HTTP_200_OK


@app.route("/list/next",methods=['POST'])
def nextSpeaker():
    with speaker_lock:
        global speaker_list
        index = 0
        if len(speaker_lists[0]) == 0:
            index = 1
        if len(speaker_lists[index]) == 0 :
            return 'Speakers list is empty', status.HTTP_410_GONE
        next_speaker = speaker_lists[index][0]
        speaker = speakers[next_speaker]
        speaker[0] += 1
        speaker[1] += 1
        speaker_lists[index] = speaker_lists[index][1:]
        return next_speaker, status.HTTP_202_ACCEPTED

@app.route("/list/reset", methods=['POST'])
def resetCount():
    with speaker_lock:
        for speaker in speakers:
            speakers[speaker][1] = 0

    return '', status.HTTP_202_ACCEPTED

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
