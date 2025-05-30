def make_sentence(word, part_of_speech):
    if part_of_speech == 0:
        print(f"My favorite book has a magical {word} in it!")
    elif part_of_speech == 1:
        print(f"Every morning, I like to {word} before breakfast!")
    elif part_of_speech == 2:
        print(f"The painting on the wall is incredibly {word}!")
    else:
        print("Invalid part of speech. Please enter 0 for noun, 1 for verb, or 2 for adjective.")

word = input("Please type a noun, verb, or adjective: ")
part = int(input("Is this a noun, verb, or adjective? Type 0 for noun, 1 for verb, 2 for adjective: "))
make_sentence(word, part)
