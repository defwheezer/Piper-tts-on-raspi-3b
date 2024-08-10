import numpy as np
import time
import sounddevice as sd
from piper.voice import PiperVoice
import psutil #cpu info
import httplib2
from gpiozero import CPUTemperature

cpu = CPUTemperature()
print("cpu.temperature: ",cpu.temperature)

model =  "en_US-kusal-medium.onnx"
print ("model =  en_US-kusal-medium.onnx")

import sounddevice as sd
from piper.voice import PiperVoice

voicedir = "/home/pi/pipertts/lib/python3.11/site-packages/piper/" #Where onnx model files are stored on my machine
model = voicedir+"en_US-kusal-medium.onnx"
voice = PiperVoice.load(model)
print ("voice loaded")

print ("psutil.getloadavg()",psutil.getloadavg())
h = httplib2.Http(".cache")
(resp_headers, content) = h.request("https://plurimediagroup.com/get_json_data_newsapi.php", "GET")
content = content.decode("utf-8")
#print (content)
# Create an empty Array
arr_str = []

arr_str = content.split('<p>')

#print (arr_str[0])

#api_url = "https://plurimediagroup.com/get_json_data_newsapi.php"


#text = "This is an example of text-to-speech using Piper TTS."

text = ["What to read this week: An astronaut’s journey  and queer horror that bites back at cliché.", "hahaha", "The witch is back in Agatha All Along’s first trailer.", "hah hah hah!", "Updates From the Rosemary’s Baby Prequel, and More.", "what the actual fuck, man?"]

print ("set up stream")
# Setup a sounddevice OutputStream with appropriate parameters
# The sample rate and channels should match the properties of the PCM data
stream = sd.OutputStream(samplerate=voice.config.sample_rate, channels=1, dtype='int16')
print ("done setting up stream")

# for title in text:
    # stream.start()
    # print("speaking")
    # for audio_bytes in voice.synthesize_stream_raw(title):
        # int_data = np.frombuffer(audio_bytes, dtype=np.int16)
        # stream.write(int_data)
    # stream.stop()
    # time.sleep(1)    

for title in arr_str:
    print("speaking titles: ", title)
    stream.start()
    try:
        for audio_bytes in voice.synthesize_stream_raw(title):
            int_data = np.frombuffer(audio_bytes, dtype=np.int16)
            stream.write(int_data)
    except:
        print("Something else went wrong")
        stream.stop()
        stream.close()
        stream = sd.OutputStream(samplerate=voice.config.sample_rate, channels=1, dtype='int16')
    stream.stop()
    #print ("psutil.getloadavg(): ",psutil.getloadavg())
    #print ("mem = psutil.virtual_memory(): ",psutil.virtual_memory())
    cpu = CPUTemperature()
    print("cpu.temperature: ",cpu.temperature)
    time.sleep(10)
    #print ("psutil.getloadavg()",psutil.getloadavg())
    #print ("mem = psutil.virtual_memory(): ",psutil.virtual_memory())

stream.close()