import random

# Asking user input
name = input("What's your name? ")
question = input("Give me question, " + name + ": ") # I don't use , because it will return args error.

# Random number generator
number = random.randint(1, 9)

# 8-Ball's Answers
if number == 1:
  answer = "Yes - definitely."
elif number == 2:
  answer = "It is decidely so."
elif number == 3:
  answer = "Without a doubt."
elif number == 4:
  answer = "Reply hazy, try again."
elif number == 5:
  answer = "Ask again later."
elif number == 6:
  answer = "Better not tell you now."
elif number == 7:
  answer = "My sources say no."
elif number == 8:
  answer = "Outlook not so good."
elif number == 9:
  answer = "Very doubtful."
else:
  answer = "Error!"

# User didn't give name and question
if name == "" and question == "": 
    print("Reality defabricated.")
# User didn't give question
elif question == "":
    print("You need to give me a question, idiot.")
# User didn't give name
elif name == "":
    print("Question:", question)
    print("Magic 8-Ball's answer:", answer)
# User give name and question
else:                             
    print(name, "asks, " + '"' + question + '"')
    print("Magic 8-Ball's answer:", answer)
