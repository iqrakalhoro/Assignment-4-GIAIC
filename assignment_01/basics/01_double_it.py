def main():
    user_input = input("Enter a number: ")
    curr_value = int(user_input)

    while curr_value < 100:
        curr_value = curr_value * 2
        print(curr_value)

if __name__ == "__main__":
    main()
