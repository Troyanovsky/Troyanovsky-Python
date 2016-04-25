#TTS test
import subprocess
from urllib.request import urlopen
import time
from gtts import gTTS

def play(audio_file_path):
    subprocess.call(["afplay", audio_file_path])
foo = """
No Cellphones allowed in the library.





"""
tts = gTTS(text=foo, lang='en')
tts.save("test.mp3")
play("test.mp3")

