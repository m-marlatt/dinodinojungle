import random
#dino dino jungle
# 45% Chance of mushroom; with 6 boxes and 6 shortcuts.
# Average time to complete between 3:00 & 3:30 mins
# S = shortcut M = Mushoom
# S1 = -5s needs M6 or M5
# S2 = -20s needs M6 or M1
# S3 = -5s needs M1 or M2
# S4 = -25s needs M2 or M3
# S5 = -10s needs M4 or M3
# S6 = -2s needs M4 or M5
# Optimal time Lap1 = -27s Lap2 = -32s Lap3 = -32s



x = 0
y = 330
Mushroom = x
laps = 0
finalTime = y
S1 = False
S2 = False
S3 = False
S4 = False
S5 = False
S6 = False
for laps in range(1,4):


 #Shortcuts

        if laps >= 2:
            if Mushroom >=1:
                print(Mushroom)
                userInput = input("Would you like to use a mushroom for Shortcut 1? Y(0) or N(1)?: \n")
                if userInput ==0: 
                    finalTime = y-5
                    Mushroom = x-1
                else: 
                    pass
            else: 
                pass

        
            
        M1 = random.randint(1,100)

        if M1 <= 45:
            Mushroom = x+1
            print("You got a mushroom!")
        else:
                print("Did not get a Mushroom")
                

        if Mushroom >= 1:
            print(Mushroom)
            userInput = input("Would you like to use a mushroom for Shortcut 2? Y(0) or N(1)?: \n")
            if userInput ==0: 
                finalTime = y-20
                Mushroom = x-1
                S2 =True
            
            else: 
                pass
        else:
            print("Cannot take shortcut 2 because there is no available Mushroom.")
            


        M2 = random.randint(1,100)

        if M2 <= 45:
            Mushroom = x+1
            print("You got a mushroom!")
        else:
                print("Did not get a Mushroom")
                

        if Mushroom >= 1:
            if S2 == False:
                print(Mushroom)
                userInput = input("Would you like to use a mushroom for Shortcut 3? Y(0) or N(1)?: \n")
                if userInput ==0: 
                        finalTime = y-5
                        Mushroom = x-1
                        S3 = True
                else: 
                    pass
                
        else:
            print("Cannot take shortcut 3 because there is no available Mushroom.")
            



        M3 = random.randint(1,100)

        if M3 <= 45:
            Mushroom = x+1
            print("You got a mushroom!")
        else:
                print("Did not get a Mushroom")
                

        if Mushroom >= 1 and S2 == False or S3 ==False:
            print(Mushroom)
            userInput = input("Would you like to use a mushroom for Shortcut 4? 0(Y) or 1(N)?: \n")
            if userInput ==0: 
                finalTime = y-25
                Mushroom = x-1
                S4 =True
            else: 
                    pass
        else:
            print("Cannot take shortcut 4 because there is no available Mushroom.")
            

        M4 = random.randint(1,100)

        if M4 <= 45:
            Mushroom = x+1
            print("You got a mushroom!")
        else:
                print("Did not get a Mushroom")
                

        if Mushroom >= 1:
            if S4 == False:
                print(Mushroom)
                userInput = input("Would you like to use a mushroom for Shortcut 5? Y(0) or N(1)?: \n")
                
                if userInput ==0: 
                    finalTime = y-10
                    Mushroom = x-1
                else: 
                    pass
        else:
            print("Cannot take shortcut  because there is no available Mushroom."
           

    M5 = random.randint(1,100)

        if M5 <= 45:
            Mushroom = x+1
            
        else:
                print("Did not get a Mushroom")
                

        if Mushroom >= 1:
            userInput = input("Would you like to use a mushroom for Shortcut 6? Y(0) or N(1)?: \n")
            print(Mushroom)
            if userInput ==0: 
                finalTime = y-2
                Mushroom = x-1
            else: 
                    pass
        else:
            print("No available Mushroom")
           

        M6 = random.randint(1,100)

        if M6 <= 45:
            Mushroom = x+1
            print("You got a mushroom!")
        else:
                print("Did not get a Mushroom")
                
else:
     print("Your final time is: \n") 
     print(finalTime)

#Doesn't stack the subtractions from the final time and a weird syntax error on line 141.