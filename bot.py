#question:answer

# import time

# now = time.ctime()

qna = {
    "Hi" : "Hey!",
    "How are you?" : "I am fine...How may I help you?",
    "What is your name?" : "My name is Subway",
    "How old are you?" : "I'm 20!",
    # "What time is it?" : now,
}

while True:
    qs = input()
    if(qs == "quit"):
        break
    else:
        print(qna[qs])