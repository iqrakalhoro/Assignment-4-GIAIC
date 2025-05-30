ADULT_AGE: int = 18

def is_adult(age: int):
    if age >= ADULT_AGE:
        return True
    return False

def main():
    age = int(input("🧓 How old is this person?: "))
    result = is_adult(age)
    print(f"✅ Is adult? {result}")

if __name__ == '__main__':
    main()
