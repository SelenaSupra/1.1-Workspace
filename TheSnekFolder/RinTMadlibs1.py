#Fill in the verbs and nouns, and run the python in terminal. Answer the prompt for a quick story!
verb1 = "drive"
verb2 = "punch"
verb3 = "kick"
noun1 = "car"
noun2 = "turkey"
noun3 = "baby"
































car = input("What kind of car do you drive?:").strip().lower()
if car == "supra":
    print ("No way, so do I!")
elif car == "toyota supra":
    print ("Small world, I've got a '95, myself!")
elif car == "toyota":
    print ("Oh, same here!")
else:
    print (f"Oh nice, so you drive a {car}.")





story = f"(\nOne day I was trying to {verb1} my {noun1} like I do every morning.\n \nBut I had to stop because a {noun2} decided to {verb2} it while I was in the middle of it!\n \nNow I like to {verb3} a {noun3} as much as the next person, but that was ridiculous.\n)"

print (story)