#!/usr/bin/env python3
#SST
import time
import speech_recognition as sr

while True:
    r = sr.Recognizer()
    with sr.Microphone() as source:                # use the default microphone as the audio source
        audio = r.listen(source)                   # listen for the first phrase and extract it into audio data
    start = time.time()
    # recognize speech using Google Speech Recognition
    try:
        # for testing purposes, we're just using the default API key
        # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY", show_all=True)`
        # instead of `r.recognize_google(audio, show_all=True)`
        from pprint import pprint
        print("Google Speech Recognition results:")
        result = r.recognize_google(audio)
        if result == "stop":
            break
        pprint(result) # pretty-print the recognition result
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
    print(time.time()-start)

    start = time.time()
    # recognize speech using Wit.ai
    WIT_AI_KEY = "ITIPFVIXEBFCZ76SIT3ILDK3H4BOAYAM" # Wit.ai keys are 32-character uppercase alphanumeric strings
    try:
        from pprint import pprint
        print("Wit.ai recognition results:")
        result = r.recognize_wit(audio, key=WIT_AI_KEY)
        if result == "stop":
            break
        pprint(result) # pretty-print the recognition result
    except sr.UnknownValueError:
        print("Wit.ai could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Wit.ai service; {0}".format(e))
    print(time.time()-start)
# # recognize speech using Microsoft Bing Voice Recognition
# BING_KEY = "84316c1ff9d64265bd44e3e44ac0a69e" # Microsoft Bing Voice Recognition API keys 32-character lowercase hexadecimal strings
# try:
#     print("Microsoft Bing Voice Recognition thinks you said " + r.recognize_bing(audio, key=BING_KEY, show_all=True))
# except sr.UnknownValueError:
#     print("Microsoft Bing Voice Recognition could not understand audio")
# except sr.RequestError as e:
#     print("Could not request results from Microsoft Bing Voice Recognition service; {0}".format(e))

