def main():
    weight = float(input("Enter your weight on Earth: "))
    planet = input("Enter the name of a planet (e.g., Mars): ")

    # Relative gravity values compared to Earth
    gravity = {
        "Mercury": 0.38,
        "Venus": 0.91,
        "Mars": 0.38,
        "Jupiter": 2.34,
        "Saturn": 1.06,
        "Uranus": 0.92,
        "Neptune": 1.19,
        "Pluto": 0.06
    }

    if planet in gravity:
        new_weight = weight * gravity[planet]
        print(f"Your weight on {planet} would be: {new_weight:.2f}")
    else:
        print("Unknown planet. Please enter a valid planet name with the first letter capitalized.")

if __name__ == "__main__":
    main()
