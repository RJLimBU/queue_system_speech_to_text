import os
from google.cloud import speech
import threading, queue

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'ec530healthapp-d83318772040.json'
speech_client = speech.SpeechClient()

q = queue.Queue()

def s2t():
	speechfile = q.get()
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
	#return respondoutput
	q.task_done()




speechfile = ['i-said-how-do-you-do-how-do-you-do-what.mp3',
'a-fine-bunch-of-water-lilies-you-turned-out-to-be.mp3','jiminy-crickets!.mp3']

# turn-on the s2t thread
threading.Thread(target=s2t, daemon=True).start()

for item in speechfile:
    q.put(item)
print('All task requests sent\n', end='')

q.join()
print('All work completed')

# response = s2t(speechfile)

# print(response)

# for i in range(len(response['results'])):
# 	regText = response['results'][i]['alternatives'][0]['transcript']
