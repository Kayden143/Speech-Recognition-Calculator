import speech_recognition as sr
print(sr.__version__)

r = sr.Recognizer()

def add(*args):
   return sum(args)

def multiply(*args):
    return product(args)

def subtract(*args):
    return sum(args) * -1

# def divide(*args):
#     return sum(args)

ops = {"+":add, "-":subtract, "*":multiply}
   
with sr.Microphone() as s:
    print("Adjusting...")
    #r.adjust_for_ambient_noise()
    r.adjust_for_ambient_noise(s, duration = 0.2)
    print("Listening")
    said = ""
    test = []
    bre = False
    validInputs = {"Plus", "plus", "+", "-", "/", "*", "Time", "Times", "time", "times", "multiply", "Multiply", "Multiplied by", "X"}
    for i in range(100):
        try: 
            audio = r.listen(s, phrase_time_limit=1.2)
            said = r.recognize_google(audio)
            if said == "stop":
                bre = True
            elif said != "":
                print(said)
                test.append(said)
            said = ""
        except: said = ""
        if bre:
            break
    print(test)
    digits = said.split(" ")
    i = 0
    while i < len(test):
        if test[i] not in validInputs and not test[i].isdigit():
            test.pop(i)
        else:
            if test[i] == "Plus" or test[i] == "plus":
                test[i] = "+"
            elif test[i] == "time" or test[i] == "times" or test[i] == "X":
                test[i] = "*"
            i += 1
    print(test)

            
