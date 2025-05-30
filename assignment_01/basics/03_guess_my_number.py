import random

def main():
    secret = random.randint(0, 99)
    
    guess = int(input("I am thinking of a number between 0 and 99... Enter a guess: "))

    while guess != secret:
        if guess > secret:
            print("Your guess is too high")
        else:
            print("Your guess is too low")
        
        guess = int(input("Enter a new number: "))
    
    print(f"Congrats! The number was: {secret}")

if __name__ == "__main__":
    main()
