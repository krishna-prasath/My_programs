import speech_recognition as ne
a=ne.Recognizer()
with ne.Microphone() as source:
    print("speak now")
    audio=a.listen(source)
    try:
        text=a.recognize_google(audio)
        print("text is::",text())
    except:
        print("error")
