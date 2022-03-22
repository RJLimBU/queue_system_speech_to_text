#https://cloud.google.com/speech-to-text/docs/reference/rest/v1/RecognitionConfig
import os
from google.cloud import speech

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'ec530healthapp-d83318772040.json'
speech_client = speech.SpeechClient()

speechfile = 'i-said-how-do-you-do-how-do-you-do-what.mp3'  

with open(speechfile, 'rb') as f1:
	byte_data_mp3 = f1.read()
audiofile = speech.RecognitionAudio(content=byte_data_mp3)

configmp3=speech.RecognitionConfig(
	#encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
    sample_rate_hertz=44100,
    language_code="en-US",
    enable_automatic_punctuation=True
)

respondoutput = speech_client.recognize(
	config=configmp3,
	audio=audiofile
)

print(respondoutput)
