#hangman_game
from words import words
from logo import logo
import random

print(logo)
stages=[
''' 
 +--+
 |  |
 O  |
\\|/ |
/ \\ |
=====
''',
'''
 +--+
 |  |
 O  |
\\|/ |
/   |
=====
''',
'''
 +--+
 |  |
 O  |
\|/ |
    |
=====
''',
'''
 +--+
 |  |
 O  |
\\|  |
    |
=====
''',
'''
 +--+
 |  |
 O  |
 |  |
    |
=====
''',
'''
 +--+
 |  |
 O  |
    |
    |
=====
''',
'''
 +--+
 |  |
    |
    |
    |
=====
'''
]

def display_man(wrong_guesses):
        print(stages[wrong_guesses]) 

def display_hint(hint):
    print(" ".join(hint))

def display_answer(answer):
    print(f"The word was: {answer}")


def main():
    answer=random.choice(words)
    hint=["_"]*len(answer)
    wrong_guesses=0          
    guessed_letters=[]
    is_running=True
    
    
    while is_running:
        display_man(wrong_guesses)
        display_hint(hint)
        guess=input("Guess a letter: ").lower()
        
        
        if len(guess)!=1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue
       
       
        if guess in guessed_letters:
            print("You already guessed that letter. Try again.")
            continue
        guessed_letters.append(guess)
       
       
        if guess in answer:
            for i in range(len(answer)):
                if answer[i]==guess:
                    hint[i]=guess
        
        
        else:
            wrong_guesses+=1        


        if "_" not in hint:
            display_man(wrong_guesses)
            display_answer(answer)
            print("Congratulations! You guessed the word.")
            is_running=False

        if wrong_guesses>=len(stages):
            print("Game Over! You ran out of guesses.")
            display_answer(answer)
            is_running=False

if __name__ == "__main__":
    main()
