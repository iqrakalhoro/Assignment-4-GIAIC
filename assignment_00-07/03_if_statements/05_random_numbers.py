import random

N_NUMBERS = 10     
MIN_VALUE = 1     
MAX_VALUE = 100    

def main():
   
    for _ in range(N_NUMBERS):
        num = random.randint(MIN_VALUE, MAX_VALUE)
        print(f"🎲 {num}")

if __name__ == '__main__':
    main()
