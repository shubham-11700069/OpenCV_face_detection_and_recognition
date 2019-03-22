import random
import time

import speech_recognition as sr

    # create recognizer and mic instances
recognizer = sr.Recognizer()
microphone = sr.Microphone()
while True:
  print('Speak!')
    #guess = recognize_speech_from_mic(recognizer, microphone)    
    #print("You said: {}".format(guess["transcription"]))
  with microphone as source:
    recognizer.adjust_for_ambient_noise(source)
    audio = recognizer.listen(source)
    recog_audio=recognizer.recognize_google(audio)
  print("You said:",recog_audio)

  if(recog_audio=='stop'):
    break

        # determine if guess is correct and if any attempts remain
        