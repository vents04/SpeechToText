import speech_recognition as sr

r = sr.Recognizer()
print("You have 5 seconds for your speech. Listening...")
with sr.Microphone() as source:
    audio_data = r.record(source, duration=5)
    print("Recognizing your speech...")
    try:
        text = r.recognize_google(audio_data)
        print(text)
    except sr.UnknownValueError as error:
        print("Speech could not be recognized")
