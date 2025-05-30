AFFIRMATION: str = "I am capable of doing anything I put my mind to."

def main():
    print("Please type the following affirmation exactly:")
    print(f'"{AFFIRMATION}"')

    user_input = input()

    while user_input != AFFIRMATION:
        print("That was not the affirmation.")
        print("Please type the following affirmation again:")
        print(f'"{AFFIRMATION}"')
        user_input = input()

    print("That's right! You're awesome! Keep believing in yourself.")

if __name__ == '__main__':
    main()
