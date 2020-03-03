print("Unknown: Ah, you are finally awake")
answer = input("Unknown: Do you remember anything?")
if(answer == "yes"):
    print("Unknown: Good, we need to get going then.")
if(answer == "no"):
    print("Unknown: Well, that makes sense. You got hit pretty hard. I will explain later put for now we need to keep moving.")

print("*You and the unknown chracter move through a forrest until coming upon a cabin*")
answer1 = input("Unknown: We should be safe here. Do you need anything?")
if(answer1 == "yes"):
    answer2 = input("Unknown: What do you need?")
    print("Unknown: We should be able to get " + answer2 + " in the morning. For now it is best if you rest up.")
if(answer1 == "no"):
    print("Unkown: Alright, if you do just let me know. You should go rest up for the time being")
