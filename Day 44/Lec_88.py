import pyttsx3

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Set properties (optional)
engine.setProperty('rate', 150)  # Speed of speech
engine.setProperty('volume', 0.5) # Volume (0.0 to 1.0)

shoutoutlist = ["Aman","Naman","Gaurav","Udit","Yash"]

for l in shoutoutlist:
    message = f"Shout Out To {l}"
    print(message)
    engine.say(message)
    engine.runAndWait()
