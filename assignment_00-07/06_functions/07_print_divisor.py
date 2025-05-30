import math

def print_divisors(num: int):
    print(f"🧮 Here are the divisors of {num} ➡️")
    divisors = set()
    for i in range(1, int(math.sqrt(num)) + 1):
        if num % i == 0:
            divisors.add(i)
            divisors.add(num // i)
    for d in sorted(divisors):
        print(f"✔️ {d}")

def main():
    num = int(input("🔢 Enter a number: "))
    print_divisors(num)

if __name__ == '__main__':
    main()
