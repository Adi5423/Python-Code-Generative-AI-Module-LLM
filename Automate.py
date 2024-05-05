import pyttsx3
import comtypes.client

# Creat a SAPI Voice 
cp = comtypes.client.CreateObject("SAPI.SpVoice")

# Speak some text
cp.Speak("Hello , It's Aistie Your Personal AI Assistant!!")

# create a SAPI voice
engine = pyttsx3.init('sapi5')

#Use a specific voice (requiers voice name as shown)
def speak(audio):
    engine.SetProperty('voice','Microsoft Zira Desktop')
    
    # Speak some text
    engine.say(audio)
    print(audio)
    
    engine.runAndWait()
