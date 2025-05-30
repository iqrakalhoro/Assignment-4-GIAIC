MINIMUM_HEIGHT = 50 

def main():
 
    height = float(input("📏 How tall are you? "))
    if height >= MINIMUM_HEIGHT:
        print("🎢 You're tall enough to ride! 🎉")
    else:
        print("🚫 You're not tall enough to ride, but maybe next year! 🌱")

def tall_enough_extension():

    while True:
        user_input = input("📏 How tall are you? (Press Enter to stop) ")
        if user_input == "":
            print("👋 Goodbye! Stay safe!")
            break
        try:
            height = float(user_input)
            if height >= MINIMUM_HEIGHT:
                print("🎢 You're tall enough to ride! 🎉")
            else:
                print("🚫 You're not tall enough to ride, but maybe next year! 🌱")
        except ValueError:
            print("❌ Please enter a valid number!")

if __name__ == '__main__':
    tall_enough_extension()
