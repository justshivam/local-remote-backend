from winsdk.windows.media.control import GlobalSystemMediaTransportControlsSessionManager as MediaManager
import winsdk.windows.media.control as wmc
from pynput.keyboard import KeyCode, Controller
import asyncio
import os

keyboard = Controller()
PLAY_PAUSE_MUSIC_KEY_CODE = 0xB3
VOLUME_UP_KEY_CODE = 0xAF
VOLUME_DOWN_KEY_CODE = 0xAE
VOLUME_MUTE_KEY_CODE = 0xAD
NEXT_TRACK_KEY = 0xB0
PREVIOUS_TRACK_KEY = 0xB1

def sleep_windows():
    os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

def play_pause_music():
    keyboard.press(KeyCode.from_vk(PLAY_PAUSE_MUSIC_KEY_CODE))

def volume_up():
    keyboard.press(KeyCode.from_vk(VOLUME_UP_KEY_CODE))

def volume_down():
    keyboard.press(KeyCode.from_vk(VOLUME_DOWN_KEY_CODE))

def volume_mute():
    keyboard.press(KeyCode.from_vk(VOLUME_MUTE_KEY_CODE))

def next_track():
    keyboard.press(KeyCode.from_vk(NEXT_TRACK_KEY))

def previous_track():
    keyboard.press(KeyCode.from_vk(PREVIOUS_TRACK_KEY))

async def get_media_info():
    sessions = await MediaManager.request_async()

    current_session = sessions.get_current_session()
    if current_session:
        info = await current_session.try_get_media_properties_async()

        info_dict = {song_attr: info.__getattribute__(song_attr) for song_attr in dir(info) if song_attr[0] != '_'}

        info_dict['genres'] = list(info_dict['genres'])

        return info_dict
    return None

async def getMediaSession():
    sessions = await wmc.GlobalSystemMediaTransportControlsSessionManager.request_async()
    session = sessions.get_current_session()
    return session

def mediaIs(state="PLAYING"):
    session = asyncio.run(getMediaSession())
    details = asyncio.run(get_media_info())
    if session == None:
        return False
    return int(wmc.GlobalSystemMediaTransportControlsSessionPlaybackStatus[state]) == session.get_playback_info().playback_status, details


if __name__ == '__main__':
    current_media_info = asyncio.run(get_media_info())
    print(current_media_info)
    print(mediaIs("PLAYING"))