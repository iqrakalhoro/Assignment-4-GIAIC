def subtract_seven(num):
    return num - 7

def main():
    print("🔢 Welcome to the Subtract Seven Program!")

    try:
        user_input = int(input("🔹 Please enter a number: "))
        result = subtract_seven(user_input)
        print("✅ After subtracting 7, the result is:", result)
    except ValueError:
        print("❌ Invalid input! Please enter a valid number.")

if __name__ == '__main__':
    main()
