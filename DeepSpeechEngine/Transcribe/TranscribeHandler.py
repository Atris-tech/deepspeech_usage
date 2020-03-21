from globals.config import ConfigDeepSpeech
import uuid
import os
import scipy.io.wavfile as wav
from .Services.SpeechToTextService import SpeechToTextService
transcribeObj = SpeechToTextService()
conf = ConfigDeepSpeech()
validFrequency = conf.get_config("frequency")
class TranscribeHandler:

    def transcribe(self, audio):

        self.uniqueFolder = conf.get_config("audio_folder") +"/"+ str(uuid.uuid4()) + "/"
        os.mkdir(self.uniqueFolder)
        uniqueFile = self.uniqueFolder + str(uuid.uuid4()) + ".wav"
        with open(uniqueFile, 'wb') as f:
            f.write(audio)
        frequency, newAudio = wav.read(uniqueFile)
        precheck = self.precheck(frequency)
        if(precheck):
            print("new aud")
            print(newAudio)
            text = transcribeObj.transcribe(audio = newAudio)
            resp = {
                "status" : "sucess",
                "data" : text
            }

            return resp
        else:
            error = {
                "frequency_of_audio": frequency,
                "frequency_required": validFrequency
            }
            resp = {
            "status": "error",
            "data" : error
            }
            return resp
    def precheck(self, fs):
        if int(fs) == int(validFrequency):
            status = True
            return status
        else:
            status = False
            return status