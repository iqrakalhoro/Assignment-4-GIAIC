def is_odd(value: int):
    remainder = value % 2
    return remainder == 1

def main():
    for i in range(10, 20):
        if is_odd(i):
            print(i, "odd 🔴")
        else:
            print(i, "even 🟢")

if __name__ == '__main__':
    main()
