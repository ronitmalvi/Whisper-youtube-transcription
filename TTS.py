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