import random
winning_number=random.randint(1,100)
guess=1
number=int(input("enter the number"))
game_over=False
while not game_over:
    if number==winning_number:
        print(f"you won and won in {guess} times")
        game_over=True
    else:
        if winning_number>number:
            print("too low")
            guess+=1
            number=int(input("guess again"))
        else:
            print("too high")
            guess+=1
            number=int(input("guess again"))
        

     
