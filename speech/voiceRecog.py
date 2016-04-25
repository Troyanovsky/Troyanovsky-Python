#!/usr/bin/env python3

import speech_recognition as sr
# installed by "pip3 install SpeechRecognition"
# install dependency by "brew install portaudio && sudo brew link portaudio"
# "pip install pyaudio"
# install flac by "brew install flac"

def voiceRecognition():
    result = ""
    r = sr.Recognizer()
    while True:
        with sr.Microphone() as source:
            audio = r.listen(source)
        try:
            temp = (parseRaw(r.recognize_google(audio),result))
            if temp != None:
                result = temp
            else:
                break
            print(result)
        except LookupError:
            print("Could not understand audio")
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio.")
        except sr.RequestError:
            print("Could not request results.")
    print(result)

def parseRaw(raw,result):
    raw = raw.lower()
    print(raw)
    parsed = [i for i in raw.split(" ")]
    return writeCode(parsed,result)

def writeCode(parsed,result):
    if len(parsed) >= 4 and parsed[0] == "define" and parsed[2] == "parameter":
        return defineResult(parsed,result)
    elif len(parsed) >= 2 and parsed[0] == "if":
        return ifResult(parsed,result)
    elif len(parsed) >= 3 and parsed[:2] == ["else","if"]:
        return elifResult(parsed,result)
    elif len(parsed) == 1 and parsed[0] == "else":
        return result + "else:\n\t"
    elif len(parsed) == 1 and parsed[0] == "back" and result[-1] == "\t":
        return result[:-1]
    elif len(parsed) == 1 and parsed[0] == "end":
        return None
    else:
        return otherResult(parsed,result) + "\n"

def defineResult(parsed,result):
    result = result + "def " + parsed[1] + "(%s)" % ",".join(parsed[3:])
    result = result + ":\n\t"
    return result

def ifResult(parsed,result):
    rest = parsed[1:]
    result = result + "if " + other(rest,result) + ":\n\t"
    return result

def elifResult(parsed,result):
    rest = parsed[2:]
    result = result + "elif " + other(rest,result) + ":\n\t"
    return result

def otherResult(parsed,result):
    for word in parsed:
        if word == "equal": result += "="
        elif word == "plus": result += "+"
        elif word == "minus": result += '-'
        elif word == "multiply": result += "*"
        elif word == "devide": result += "/"
        else: result += word
    return result

voiceRecognition()