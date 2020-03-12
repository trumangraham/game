
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
    main()

def main():
    print("1: Go to sleep")
    print("2: Explore")
    print("3: Ask questions")
    answer3 = input("What would you like to do? ")
    if(answer3 == "1"):
        print()
        print("*You wake up tied down to a chair in a dark room*")
        ending()
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
                    print("Unknown: What do you think you are doing? ")
                    print("1: I was looking for the bathroom")
                    print("2: Just looking around")
                    print("3: Nothing")
                    answer7 = input("What would you like to say?")
                    print("*You briefly feel something hit you on the head and everything goes black*")
                    print("*****************************************")
                    print("*****************************************")
                    print("*****************************************")
                    print("*You wake up tied down to a chair in a dark room*")
                    ending()
                if(answer6 == "2"):
                    print("*You tackle the man down the stairs*")
                    print("*You look at your leg an notice a knife is in it*")
                    print("***Things are starting to get fuzzy***")
                    print("*****************************************")
                    print("*****************************************")
                    print("*****************************************")
                    print("*You wake up tied down to a chair in a dark room*")
                    ending()
                if(answer6 == "3"):
                    print("*You land smoothly and take off running*")
                    print("*Congratulations!!! You successfully escaped*")
                    credit()
            if(answer5 == "2"):
                print()
                print("*You wake up tied down to a chair in a dark room*")
                ending()
        if(answer4 == "2"):
            print("*You walk downstairs and discover an empty room with a chair sitting in the center*")
            print("*It looks like the chair was used to tie somebody down*")
            print("1: Run")
            print("2: Confront man")
            print("3: Ignore and go to sleep")
            answer7 = input("What would you like to do? ")
            if(answer7 == "1"):
                print("*While running up the stairs somebody steps out infront of you*")
                print("*They push you before you can react*")
                print("*You fall down the stairs and hit your head*")
                print("*****************************************")
                print("*****************************************")
                print("*****************************************")
                print("*You wake up tied down to a chair in a dark room*")
                ending()
            if(answer7 == "2"):
                print("*You walk into the room where you last saw him*")
                print("*It is empty*")
                print("*You fell something slam against your head*")
                print("*****************************************")
                print("*****************************************")
                print("*****************************************")
                print("*You wake up tied down to a chair in a dark room*")
                ending()
            if(answer7 == "3"):
                print("*You wake up tied down to a chair in a dark room*")
                ending()
        if(answer4 == "3"):
            print("*You walk outside and an alarm sounds as soon as you get out*")
            print("1: Run")
            print("2: Wait for alarm to stop")
            print("3: Investigate")
            answer8 = input("What would like to do? ")
            if(answer8 == "1"):
                print("*You take off running like a stallion*")
                print("*Congratulations!!! You successfully escaped*")
                credit()
            if(answer8 == "2"):
                print("*The unknown man from earlier is running at you*")
                print("*He injects you with a needle before you can do anything*")
                print("***Things are starting to get fuzzy***")
                print("*****************************************")
                print("*****************************************")
                print("*****************************************")
                print("*You wake up tied down to a chair in a dark room*")
                ending()
            if(answer8 == "3"):
                print("*The unknown man from earlier is running at you while you are checking the alarm*")
                print("*He injects you with a needle before you can do anything*")
                print("***Things are starting to get fuzzy***")
                print("*****************************************")
                print("*****************************************")
                print("*****************************************")
                print("*You wake up tied down to a chair in a dark room*")
                ending()
    if(answer3 == "3"):
        print("*You ask who he is who you are and where we are*")
        print("Unknown: Honestly I do not know who you are I just hit you over the head and brought you out to my cabin")
        print("Unknown: You aren't the first person I have done this to. You won't be the last either")
        print("Unknown: Now that you know that I am afraid I am can let you leave")
        print("*You fell something slam against your head*")
        print("*****************************************")
        print("*****************************************")
        print("*****************************************")
        print("*You wake up tied down to a chair in a dark room*")
        ending()
        

def ending():
    print("*Out of the corner of your eye you see the unknown man fiddeling with a blade*")
    print("1: Try to break out of chair")
    print("2: Reason with him")
    print("3: Wait")
    answer10 = input("What would you like to do? ")
    if(answer10 == "1"):
        print("*You keep attempting to break free*")
        print("*The rope is too tight*")
        print("*The man walks over and begins to cut you up")
        print("You died :(")
        credit()
    if(answer10 == "2"):
        print("*You being to tell him that he does not have to do this*")
        print("*You say you won't tell anybody*")
        print("*You tell him about your family and your life*")
        print("*He does not seem to care*")
        print("*The man walks over and begins to cut you up")
        print("You died :(")
        credit() 
    if(answer10 == "3"):
        print("*You sit quietly sit tight*")
        print("*He gets closer to you*")
        print("*You spit in his face, he drops the knife, you kick him in the balls, you grab the knife and cut yourself free*")
        print("*You successfully defeated him*")
        print("*Congratulations!!! You successfully escaped*")
        credit()
        
        
        
def credit():
    print()
    print("Coded by Truman Graham")
    print()
    print("Written by Truman Graham")
    print()
    print("Given 100% by Mr. Clark")
    print()
    print()
    fin = input("Would you like to play again? ")
    if(fin == "yes"):
        print("Enjoy")
        print()
        print()
        intro()
    if(fin == "no"):
        print("Thanks for playing have a good day")
        
    
          
            
            
                
                
        
intro()    
