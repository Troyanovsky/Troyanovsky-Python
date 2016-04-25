#TTS test
from gtts import gTTS
import subprocess
from urllib.request import urlopen
import time

def play(audio_file_path):
    subprocess.call(["afplay", audio_file_path])

def getTemp(raw):
    tempIndex = (raw.find("<temp_c>")+len("<temp_c>")
            ,raw.find("</temp_c>"))
    temperature = raw[tempIndex[0]:tempIndex[1]] + " degrees Celsius"
    if "." in temperature:
        temperature = temperature.replace("."," point ")
    return temperature

def getHum(raw):
    humIndex = (raw.find("<relative_humidity>")+len("<relative_humidity>")
            ,raw.find("</relative_humidity>"))
    humidity = raw[humIndex[0]:humIndex[1]] + " percent"
    return humidity

def getDescription(raw, nowHour):
    try:
        if raw.find("Forecast for Today") != -1:
            raw = raw[raw.find("Forecast for Today"):]
            when = "Today: "
        elif (raw.find("Forecast for Tonight") != -1):
            raw = raw[raw.find("Forecast for Tonight"):]
            when = "Tonight: "
        elif (raw.find("Forecast for Rest Of Tonight") != -1):
            raw = raw[raw.find("Forecast for Rest Of Tonight"):]
            when = "Rest Of Tonight: "
        elif (raw.find("Forecast for Overnight") != -1):
            raw = raw[raw.find("Forecast for Overnight"):]
            when = "Overnight: "
        desIndex = (raw.find("<description>")+len("<description>")
            ,raw.find("</description>"))
        description = when + raw[desIndex[0]:desIndex[1]]
        return description
    except:
        return ""

raw = urlopen("http://w1.weather.gov/xml/current_obs/KAGC.xml")
raw = raw.read().decode("utf-8")
raw1 = urlopen("http://www.rssweather.com/zipcode/15289/rss.php")
raw1 = raw1.read().decode("utf-8")
nowHour = time.localtime().tm_hour
nowMinute = time.localtime().tm_min
description = getDescription(raw1,nowHour)
now = "The time is {0}:{1}. ".format(nowHour,nowMinute)
forecast = (now + "Weather in Pittsburgh. " + "The temperature is " + 
    getTemp(raw) + ". The humidity is " + getHum(raw) + '. ' + description)
tts = gTTS(text=forecast, lang='en')
tts.save("weather.mp3")
print(forecast)
play("weather.mp3")