import speech_recognition as sr
import urllib.error
import urllib.parse
import urllib.request
import subprocess
import os

from urllib import request
from pathlib import Path
root = f'{str(Path(__file__).resolve().parent)}/ogg/'

class VkSint:

    def sint(url):
        destination = f'{root}test.ogg'
        dest_filename = f'{root}output.wav'

        urllib.request.urlretrieve(url, destination)
        process = subprocess.run(['ffmpeg', '-i', destination, dest_filename])
        if process.returncode != 0:
            return "Something went wrong"

        r = sr.Recognizer()
        harvard = sr.AudioFile('/home/utka/Python/VK/group bot/ogg/output.wav')
        with harvard as source:
            r.adjust_for_ambient_noise(source, duration=0.5)
            audio = r.record(source)

        try:
            AudioResult = r.recognize_google(
                audio, language='ru-RU')
        except:
            AudioResult = 'Неудалось распознать'

        for i in [destination, dest_filename]:
            path = os.path.join(os.path.abspath(os.path.dirname(__file__)), i)
            os.remove(path)
        os.system("clear")
        return AudioResult
