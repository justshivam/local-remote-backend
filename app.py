from flask import Flask, request
from constants import (
    PLAY_PAUSE_MUSIC,
    VOLUME_UP,
    VOLUME_DOWN,
    VOLUME_MUTE,
    NEXT_TRACK,
    PREVIOUS_TRACK,
    SLEEP_WINDOWS,
)
from details_api import (
    volume_up,
    volume_down,
    volume_mute,
    next_track,
    play_pause_music,
    previous_track,
    sleep_windows,
)
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)


@app.route("/api/v1/")
def test_route():
    return {"message": "test"}


@app.route("/api/v1/action")
def action_route():
    requested_action = request.args.get("action")
    executed = False
    try:
        if requested_action == PLAY_PAUSE_MUSIC:
            play_pause_music()
            executed = True
        elif requested_action == VOLUME_UP:
            volume_up()
            executed = True
        elif requested_action == VOLUME_DOWN:
            volume_down()
            executed = True
        elif requested_action == VOLUME_MUTE:
            volume_mute()
            executed = True
        elif requested_action == NEXT_TRACK:
            next_track()
            executed = True
        elif requested_action == PREVIOUS_TRACK:
            previous_track()
            executed = True
        elif requested_action == SLEEP_WINDOWS:
            sleep_windows()
            executed = True
    except:
        return {"message": f"Failed To Execute Request: {requested_action}"}, 500
    if not executed:
        return {"message": f"Unknown Request: {requested_action}"}, 400
    return {"message": f"Executed Request: {requested_action}"}, 202


if __name__ == "__main__":
    app.run(debug=os.environ["DEBUG"].lower() == "true", port=os.environ["PORT"])
