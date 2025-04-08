import os
import requests
from dotenv import load_dotenv
import subprocess
import shutil
import time
from deepgram import Deepgram

load_dotenv()

DG_API_KEY = os.getenv("DEEPGRAM_API")
MODEL_NAME = "alpha-stella-en-v2"

def is_installed(lib_name: str) -> bool:
    lib = shutil.which(lib_name)
    return lib is not None

def play_stream(audio_stream, use_ffmpeg=True):
    player = "ffplay"
    if not is_installed(player):
        raise ValueError(f"{player} not found, necessary to stream audio.")
    
    player_command = ["ffplay", "-autoexit", "-", "-nodisp"]
    player_process = subprocess.Popen(
        player_command,
        stdin=subprocess.PIPE,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )

    for chunk in audio_stream:
        if chunk:
            player_process.stdin.write(chunk)  # type: ignore
            player_process.stdin.flush()  # type: ignore
    
    if player_process.stdin:
        player_process.stdin.close()
    player_process.wait()