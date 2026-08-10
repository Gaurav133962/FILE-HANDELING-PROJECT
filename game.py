
import random
num = random.randint(1,1000)
print(num)

tries= 0
while True:


    guess = int(input( "GUESS YOUR NUMBER BTW 1 TO 1000 :- "))
    if num == guess:
        tries+=1
        print( f"YOUR GUESS IS RIGHT YOU ANSWER CORRECT IN {tries} TRIES")
        
              
    elif num < guess:
        tries += 1  
        print("you need to go lower")
    
    elif num > guess:
        tries += 1
        print("go little higher")
    
    elif num < guess:
        tries += 1  
        print("go little higher")

    else :
        tries += 1
        print(print("your answer is wrong"))