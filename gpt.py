from openai import OpenAI
import speech_recognizer as sr
import pyttsx3





listener = sr.Recognizer()

engine = pyttsx3.init()

client = OpenAI(api_key="")


while True:
    with sr.Microphone() as source:
        print("Speak now ......")
        voice = listener.listen(source)
        data = listener.recognize_google(voice)
    response = client.chat.completions.create(model="gpt-3.5-turbo-instruct",
                                              messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": data} ])

    choice = int(input("Enter 1 to print the response (Or) Enter 2 for listen and see the response" ))



    if choice == 1:
        print(response.choices[0].message.content)
    else:
        print(response.choices[0].message.content)
        engine.say(response)
        engine.runAndWait()


    repeat = input("Do you want to ask more questions ? \n")
    if repeat in ["NO","no","No","nO"]:
        break








    if "exit" in data:
        break















