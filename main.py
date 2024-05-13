import pyttsx3

# Initialize the text-to-speech engine
engine = pyttsx3.init()

if __name__ == '__main__':
    print("Welcome to RoboSpeaker 1.1. Created by Aditya")

    while True:
        x = input("Enter what you want to pronounce : ")
        if x.lower() == "q":
            engine.say('bye bye friend, take care')
            engine.runAndWait()
            break

        # Say the input text
        engine.say(x)
        engine.runAndWait()
