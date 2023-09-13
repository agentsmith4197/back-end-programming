from random import randint

def play_game():
    computer_number = randint(1, 10)
    attempts = 0
    
    while attempts < 3:
        user_number = int(input('Guess the Number: '))
        
        if user_number == computer_number:
            print('Congratulations! You guessed the correct number.')
            return
        elif user_number < computer_number:
            print('The number you enter is small try a higher number.')
        else:
            print(' The number you enter is too big Try a lower number.')
        
        attempts += 1
    print(f'Sorry, you couldn\'t guess the number. The correct number was {computer_number}.')

play_game()
