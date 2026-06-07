from RNG import random_num
from taking_input import get_input
from Visualization import visualization
def main():
    i = 0
    iterations = []
    guesses = []
    print("A number has been guessed from 1-100 try to guess it in 10 tries.")
    num_to_guess = random_num()
    while True:
        i+=1
        iterations.append(i)
        print("-"*75)
        guess = get_input()
        print("-"*75)
        guesses.append(guess)
        if guess == num_to_guess:
            print(f"You have succesfully Guessed the number is {i} times!")
            print(f"All of your guesses were: {guesses}")
            visualization(iterations,guesses,num_to_guess)
            break
        elif guess > num_to_guess:
            print("Go lower!")
        else:
            print("Go higher!")
        
        print("-"*75)
        print(f"Your previous guesses are: {guesses}")
        if i == 10:
            print(f"You have failed to guess the number {num_to_guess}")
            break

if __name__ == "__main__" : main()

    
    
    
