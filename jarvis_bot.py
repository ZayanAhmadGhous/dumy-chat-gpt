import speech_recognition as sr
import pyttsx3
import openai

openai.api_key="your-api-key"


def SpeakText(text):
    engine=pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


r=sr.Recognizer()

def record_text():
    while(1):
        try:
            with sr.Microphone() as source2:
                r.adjust_for_ambient_noise(source2,duration=0.2)

                print("I'm listening")

                audio2=r.listen(source2)

                mytext=r.recognize_google(audio2)

                return mytext
        except sr.RequestError as e:
            print(f"Couldn't request result: {0}")

        except sr.UnknownValueError:
            print("Unknown Error Occured")


def send_to_gpt(messages):

    response =openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=messages,
        temperature=0.5,
        max_tokens=100,
        n=1,
        stop=None
        )

    message=response['choices'][0]['message']['content']

    return message

messages=[]

greating="Hello! " #You can add your name against hello if you want
SpeakText(greating)

while(1):
    text=record_text()
    messages.append({"role":"user","content": text})
    responce=send_to_gpt(messages)
    SpeakText(responce)

    print(responce)



