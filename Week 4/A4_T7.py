# Pyydä arvo ja muuta se integeriksi
# Alusta muuttuja, joka laskee kierroksia
# Tee While loop, joka looppaa niin kauan kuin arvo ei ole nolla
    # Testaa, onko arvo pienempi kuin 10 > break 
    # Muuta arvo integeriksi, jotta saamme yksittäiset numerot esiin
    # Tee for loop, joka käy läpi jokaisen luvun 
        # Testaa, onko numero viimeinen
        # Tee laskutoimitus 
    # Printtaa kertolaskun tulos
    # Muuta arvoksi edellisen kierroksen kertolaskun tulos
    # Jos arvo on nolla, printtaa No more steps
    # Lisää kierroslaskuriin +1

# Printtaa kierrokset ja program ending. 

print("Program starting.")
print("")
print("Check multiplicative persistence.")
value = int(input("Insert an integer: "))
rounds = 0

while value != 0:
    if value < 10:
        break

    value_str = str(value)
    product = 1

    for i in range(len(value_str)):
        print(value_str[i], end="")
        if i != len(value_str) - 1:
            print(" * ", end="")

    print(" = ", end="")

    for i in range(len(value_str)):
        product *= int(value_str[i])

    print(product)
    value = product
    rounds += 1

print("No more steps.")
print("")
print("This program took", rounds, "step(s)")
print("")
print("Program ending.")
