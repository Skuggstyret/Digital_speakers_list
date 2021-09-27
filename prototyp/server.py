import os, toml, sys,threading, datetime
from flask import Flask, jsonify
from flask_api import status
import json

app = Flask(__name__)

# Global variable
speaker_list = []
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
    speakers[name[0]] = [name,0,0]



# list
@app.route("/list/add/<tag>", methods=['POST'])
def addSpeakerToList(tag):
    if tag in speakers:
        with speaker_lock:
            if tag in speaker_list:
                return '', status.HTTP_400_BAD_REQUEST
            speaker_list.append(tag)
            speaker_list.sort(key=lambda x: speakers[x][1])
            return '',status.HTTP_202_ACCEPTED
    else:
        return '', status.HTTP_400_BAD_REQUEST

@app.route("/list/remove/<tag>",methods=['POST'])
def removeSpeakerFromList(tag):
    if tag in speakers:
        with speaker_lock:
            if tag not in speaker_list:
                return '', status.HTTP_400_BAD_REQUEST
            speaker_list.remove(tag)
            return '', status.HTTP_200_OK
    else:
        return '', status.HTTP_400_BAD_REQUEST

@app.route("/list/get",methods=['GET'])
def getSpeakersOnList():
    return jsonify(list(map(lambda x:speakers[x], speaker_list))), status.HTTP_200_OK


@app.route("/list/next",methods=['POST'])
def nextSpeaker():
    with speaker_lock:
        global speaker_list
        speaker = speakers[speaker_list[0]]
        speaker[1] += 1
        speaker[2] += 1
        speaker_list = speaker_list[1:]
        return speaker[0], status.HTTP_202_ACCEPTED

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
            f.write("{} - {}\n".format(speakers[speaker][0], speakers[speaker][2]))




# Init stuff
if __name__ == "__main__":
    if len(sys.argv) > 1:
        file_data = toml.load(sys.argv[1])
        with speaker_lock:
            for speaker in file_data["talar"]:
                speakers[speaker[0]] = [speaker[1],0,0]
    app.run(debug=True, use_reloader=False)
