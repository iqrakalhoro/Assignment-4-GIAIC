def main():
    curr_value = int(input("Enter a number: "))

    while curr_value < 100:
        curr_value = curr_value * 2
        print(f"Doubled value: {curr_value}")

    print("Done! The value has reached 100 or more!")

if __name__ == '__main__':
    main()
