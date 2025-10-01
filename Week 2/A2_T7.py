print("Program starting.")
Fah = float(input("Insert fahrenheits: "))
Cel = (Fah - 32) / 1.8
Cel = round(Cel, 1)
print(f"{Fah}°F is {Cel}°C")
print("Program ending.")