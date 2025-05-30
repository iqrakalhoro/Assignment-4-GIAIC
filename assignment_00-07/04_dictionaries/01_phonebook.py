def read_phone_numbers():
    """
    Ask the user for names and numbers to store in a phonebook (dictionary).
    Stops when the user inputs a blank name.
    Returns the phonebook dictionary.
    """
    phonebook = {}  

    while True:
        name = input("Name: ")
        if name == "":
            break
        number = input("Number: ")
        phonebook[name] = number

    return phonebook

def print_phonebook(phonebook):
    """
    Prints all the names and their corresponding phone numbers.
    """
    print("\n📖 Phonebook Entries:")
    for name in phonebook:
        print(f"📱 {name} -> {phonebook[name]}")

def lookup_numbers(phonebook):
    """
    Allow the user to lookup phone numbers by entering a name.
    Stops when the user inputs a blank name.
    """
    while True:
        name = input("\nEnter name to lookup: ")
        if name == "":
            break
        if name not in phonebook:
            print(f"❌ {name} is not in the phonebook.")
        else:
            print(f"📞 Number for {name}: {phonebook[name]}")


def main():
    phonebook = read_phone_numbers()
    print_phonebook(phonebook)
    lookup_numbers(phonebook)
    print("\n✅ End of program 👋")

if __name__ == '__main__':
    main()
