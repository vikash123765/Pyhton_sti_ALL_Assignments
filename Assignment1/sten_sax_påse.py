import random 

class RockPaperScissorGame:
    
    
    def win_or_loose(user_choise,computer_string):
        if user_choise == computer_string:
            print(f"useres choise was: {user_choise} and computers choise was : {computer_string}, result is even")

        elif user_choise=="rock" and computer_string =="paper":
            print(f"useres choise was: {user_choise} and computers choise was : {computer_string}, rock loses aginst paper computer wins")
    
        elif user_choise=="rock" and computer_string=="scissor":
            print(f"useres choise was: {user_choise} and computers choise was : {computer_string}, rock beats scissor  computer loses ")
      
        elif user_choise=="scissor" and computer_string =="rock":
            print(f"useres choise was: {user_choise} and computers choise was : {computer_string}, scissor loses against rock  computer wins ")
    
        elif user_choise=="scissor" and computer_string=="paper":
            print(f"useres choise was: {user_choise} and computers choise was : {computer_string}, scissor beats paper  computer loses ")
    
        elif user_choise=="paper" and computer_string =="rock":
            print(f"useres choise was: {user_choise} and computers choise was : {computer_string}, paper beats rock  computer loses ")
    
        elif user_choise =="paper" and computer_string =="scissor":
            print(f"useres choise was: {user_choise} and computers choise was : {computer_string}, paper loses against scissor computer wins ")
def main():
        
    while True:
        user_choise= input(("pplease enter rock, paper, or scissor,  press q to end game"))
        if  user_choise.lower() =="q":
            break
        if not user_choise =="rock" and not user_choise =="paper" and not user_choise =="scissor":
            print("not valid input pleasde enter any of the given options")
            continue
        computer = random.randint(1,3)
  
        if computer == 1:
            computer_string="rock"
        elif computer == 2:
            computer_string="paper"
        elif computer == 3:
            computer_string="scissor"
        
        RockPaperScissorGame.win_or_loose(user_choise,computer_string)
main()         
        

"""    ## setting up realtinship between user and computer choise where win or loose should be placed         
        win_or_loose = {
        "rock": {"scissor":"wins","bag":"loses"},
        "scissor": {"bag": "wins", "rock": "loses"},
        "bag": {"rock": "wins", "scissor": "loses"}

        } 
    if user_choise == computer_string:
       print(f"useres choise was: {user_choise} and computers choise was : {computer_string}, result is even")
       break
    else:
        ## will return a win or lose value by us oassing the keys the relationship of win or lose is setup in win_or_loose dict
        result=win_or_loose[user_choise][computer_string]
        if result == "wins":
             print(f"useres choise was: {user_choise} and computers choise was : {computer_string} user wins")
        else:
            print(f"useres choise was: {user_choise} and computers choise was : {computer_string} user loses")
"""
 
    