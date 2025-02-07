# RPS.py
# Name: Mason Rodgers
# Date: 2/7/25
# Assignment: RPS

import random 

def main():
    wins = 0
    ties = 0
    losses = 0

    print("Welcome to Rock, Paper, Scissors!")  
    print("Type R for Rock, P for Paper, or S for Scissors.")  

    play_again = "Y"

    while play_again.upper() == "Y":  
        computer_choice = random.choice(['R', 'P', 'S'])  

        user_choice = input("Your choice: ")  
        user_choice = user_choice.upper()  

        if user_choice not in ['R', 'P', 'S']:
            print("Oops, invalid input. Please use R, P, or S.")  
            continue  
        print("You chose:", user_choice)
        print("Computer chose:", computer_choice)

        
        if user_choice == computer_choice:
            print("It is a tie!")
            ties = ties + 1  
        elif (user_choice == 'R' and computer_choice == 'S') or \
             (user_choice == 'P' and computer_choice == 'R') or \
             (user_choice == 'S' and computer_choice == 'P'):
            print("Awesome! You Win!")
            wins = wins + 1  
        else:
            print("Darn! You Lost.")
            losses = losses + 1  

      
        play_again = input("Wanna play again? (Y/N): ")  

    
    print("\nFinal Stats:")
    print("Wins:", wins, "Ties:", ties, "Losses:", losses)
    print("Thanks for Playing!")  

if __name__ == '__main__':
    main()
