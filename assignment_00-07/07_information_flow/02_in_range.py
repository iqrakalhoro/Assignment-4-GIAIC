def in_range(n, low, high):
    if low <= n <= high:
        return True
    return False

def main():
    print("🔎 Testing in_range function:")
    print("Is 5 in range 1 to 10? ➡️", in_range(5, 1, 10))
    print("Is 0 in range 1 to 10? ➡️", in_range(0, 1, 10))
    print("Is 10 in range 10 to 20? ➡️", in_range(10, 10, 20))
    print("Is 21 in range 10 to 20? ➡️", in_range(21, 10, 20))

if __name__ == '__main__':
    main()
