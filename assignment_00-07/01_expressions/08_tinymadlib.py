SENTENCE_START: str = "Learning Python is awesome. Today I built an "

def main():
    adjective: str = input("Please type an adjective and press enter. ")
    noun: str = input("Please type a noun and press enter. ")
    verb: str = input("Please type a verb and press enter. ")
    print(SENTENCE_START + adjective + " " + noun + " " + verb + "!")

if __name__ == '__main__':
    main()
