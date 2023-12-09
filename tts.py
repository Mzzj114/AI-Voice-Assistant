import pyttsx3
# import gTTS , which is tts service from Google

engine = pyttsx3.init()

def say(text, rate = 200, volume = 1.0):
    engine.setProperty('rate', rate)  # 设定语速 默认200
    engine.setProperty('volume', volume)  # 设定音量 默认1.0


    engine.say(text)

    engine.runAndWait()
    
