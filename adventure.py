
def intro():
    print("Unknown: Ah, you are finally awake")
    answer = input("Unknown: Do you remember anything? ")
    if(answer == "yes"):
        print("Unknown: Good, we need to get going then.")
    if(answer == "no"):
        print("Unknown: Well, that makes sense. You got hit pretty hard. I will explain later but for now we need to keep moving.")
    woods()

def woods():
    print("*You and the unknown chracter move through a forest until coming upon a cabin*")
    answer1 = input("Unknown: We should be safe here. Do you need anything? ")
    if(answer1 == "yes"):
        answer2 = input("Unknown: What do you need ? ")
        print("Unknown: We should be able to get " + answer2 + " in the morning. For now it is best if you rest up.")  
    if(answer1 == "no"):
        print("Unknown: Alright, if you do just let me know. You should go rest up for the time being")
        print("*The unknown man walks into a bedroom and closes the door*")
    choice()

def choice():
    print("1: Go to sleep")
    print("2: Explore")
    print("3: Ask questions")
    answer3 = input("What would you like to do? ")
    if(answer3 == "1"):
        print()
        print("*You wake up with a headache and the sound of something upstairs*")
        if(answer3 == "2"):
            print("1: Upstairs")
            print("2: Basement")
            print("3: Outside")
            answer4 = input("Where would you like to go? ")
            if(answer4 == "1"):
                print()
                print("*You walk upstairs and discover acouple empty bedrooms and a locked door*")
                print("1: Attempt to pick lock")
                print("2: Go to sleep")
                answer5 = input("What would you like to do? ")
                if(answer5 == "1"):
                    print("*Attempt failed due to lack of lockpicks*")
                    print("*You hear hear somebody running up the stairs*")
                    print("1: Wait")
                    print("2: Charge person")
                    print("3: Jump out window")
                    answer6 = input("What would you like to do? ")
                    if(answer6 == "1"):
                        print("*You recognize the person as the same man from before*")
                        print("Unknown: What do you think you are doing?")
                        print("1: I was looking for the bathroom")
                        print("2: Just looking around")
                        print("3: Nothing")
                        answer7 = input("What would you like to say?")
                        print("*You briefly feel something hit you on the head and everything goes black*")
                        print("*****************************************")
                        print("*****************************************")
                        print("*****************************************")
                        print("*You wake up tied down to a chair in a dark room*")
                
                
                

intro()    
