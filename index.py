import speech_recognition as sr
import webbrowser

r = sr.Recognizer()

while(True):
    with sr.Microphone() as source:
        print("Diga alguma coisa...")
        audio = r.listen(source)

    try:
        text = r.recognize_google(audio,language='pt-BR')
        print("Você disse: " + text)

        if "navegador" in text:
            webbrowser.open_new_tab('https://www.google.com')
        elif "YouTube" in text:
            webbrowser.open_new_tab('https://www.youtube.com')

    except sr.UnknownValueError:
        print("Não entendi")