print("Program starting.")
print("Welcome to the unit converter program!")
print("Follow the menu instructions below.\n")

print("Options:")
print("1 - Length")
print("2 - Weight")
print("0 - Exit")
Choice = int(input("Your choice: "))

if Choice == 1:
    print("\nLength options:")
    print("1 - Meters to kilometers")
    print("2 - Kilometers to meters")
    print("0 - Exit")
    Choice2 = int(input("Your choice: "))

    if Choice2 == 1:
        Meters = float(input("Insert meters: "))
        Kilometers = Meters / 1000
        print(f"{Meters:.1f} m is {Kilometers:.1f} km")
    elif Choice2 == 2:
        Kilometers = float(input("Insert kilometers: "))
        Meters = Kilometers * 1000
        print(f"{Kilometers:.1f} km is {Meters:.1f} m")
    elif Choice2 == 0:
        print("Exiting...")
    else:
        print("Unknown option.")

elif Choice == 2:
    print("\nWeight options:")
    print("1 - Grams to pounds")
    print("2 - Pounds to grams")
    print("0 - Exit")
    Choice2 = int(input("Your choice: "))

    if Choice2 == 1:
        Grams = float(input("Insert grams: "))
        Pounds = Grams / 453.59237
        print(f"{Grams:.1f} g is {Pounds:.1f} lb")
    elif Choice2 == 2:
        Pounds = float(input("Insert pounds: "))
        Grams = Pounds * 453.59237
        print(f"{Pounds:.1f} lb is {Grams:.1f} g")
    elif Choice2 == 0:
        print("Exiting...")
    else:
        print("Unknown option.")

elif Choice == 0:
    print("Exiting...")
else:
    print("Unknown option.")

print("\nProgram ending.")
