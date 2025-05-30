fruits = {
    'apple': 1.5,
    'durian': 50,
    'jackfruit': 80,
    'kiwi': 1,
    'rambutan': 1.5,
    'mango': 5
}


total_cost = 0

for fruit_name in fruits:
    price = fruits[fruit_name]
    quantity = int(input(f"🍉 How many ({fruit_name}) do you want?: "))
    total_cost += price * quantity


print(f"\n🧮 Your total is: ${total_cost}")

