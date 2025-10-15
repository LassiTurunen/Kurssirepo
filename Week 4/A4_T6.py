# Tee muuttuja, joka laskee kierrokset
# Muuta annettu arvo integeriksi
# Arvo muuttuu loopin aikana
# Tee while =loop, joka looppaa niin kauan, kuin arvo ei ole 1
    # Printtaa alkuperäinen arvo ja lisää loppuun ->
    # Testaa onko arvo parillinen
        #Jaa arvo kahdella
    # Muussa tapauksessa
        # Kerro arvo kolmella ja lisää yksi

    # Lisää kierroksiin +1

# Printtaa kierrokset

print("Program starting.")

number = int(input("Insert a positive integer: "))
steps = 0

print(number, end="")

while number != 1:
    print(" -> ", end="")
    if number % 2 == 0:
        number = number // 2
    else:
        number = number * 3 + 1
    print(number, end="")
    steps += 1
print("")
print("Sequence had", steps, "total steps.")
print("")
print("Program ending.")