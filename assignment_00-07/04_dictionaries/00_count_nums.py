def get_user_numbers():
    """
    Ask the user to enter numbers repeatedly.
    Stops when user inputs a blank line.
    Returns a list of entered numbers.
    """
    user_numbers = []
    while True:
        user_input = input("➡️ Enter a number: ")
        if user_input == "":
            break
        num = int(user_input)
        user_numbers.append(num)
    return user_numbers

def count_nums(num_lst):
    """
    Takes a list of numbers.
    Returns a dictionary with number frequencies.
    """
    num_dict = {}
    for num in num_lst:
        if num not in num_dict:
            num_dict[num] = 1
        else:
            num_dict[num] += 1
    return num_dict

# -------------------------------------
# 🖨️ 3. Function to print the frequency results
# -------------------------------------
def print_counts(num_dict):
    """
    Prints each number and how many times it appears.
    """
    for num in num_dict:
        print(f"🔢 {num} appears {num_dict[num]} times.")

# -------------------------------------
# ▶️ 4. Main program execution starts here
# -------------------------------------
def main():
    user_numbers = get_user_numbers()
    num_dict = count_nums(user_numbers)
    print("\n📊 Number counts:")
    print_counts(num_dict)
    print("\n✅ End of program 👋")

if __name__ == '__main__':
    main()
