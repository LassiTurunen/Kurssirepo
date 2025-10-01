# # print("Welcome to the temp app!")
# # Temp = int(input("What is the temperature of CPU? "))

# # if(Temp > 80):
# #     print("Warning, temperature too high!")
# # else:
# #     print("All cool, keep on going!")

# # Tee ohjelma, joka testaa, onko annettu numero parillinen vai pariton.

# # num = int(input("Insert number: "))

# # Answer = num % 2
# # if Answer == 0:

# # if num % 2 == 0:
# #     print("Parillinen")
# # else:
# #     print("Pariton")

# Temp = int(input("Temperature: "))

# if(Temp > 80):
#     if(Temp > 90):
#         print("You are toast")
#     else:
#         print("Warning")
# else:
#     print("You are ok")

# #if(Temp > 90):
#    # print("You are toast")
# #elif(Temp > 80):
#    # print("Warning!")
# #else:
#    # print("You are ok")

# # Tee ohjelma, joka kysyy kahta nimeä. Testaa kumpi nimistä on pidempi vai onko ne saman mittaisia. Vinkki: len()

# nimi1 = input("Anna ensimmäinen nimi: ")
# nimi2 = input("Anna toinen nimi:")

# pituus1 = len(nimi1)
# pituus2 = len(nimi2)

# if pituus1 > pituus2:
#     print(f"Nimi {nimi1} on pidempi kuin {nimi2}.")
# elif pituus2 > pituus1: 
#     print(f"Nimi {nimi2} on pidempi kuin {nimi1}.")
# else:
#     print("Nimet ovat samanpituisia.")

# Town = "Lahti"
# Street = "Mukkulankatu"
# Building = 19

# if(Town == "Lahti" and Street == "Mukkulankatu" and Building == 19):
#     print("You are at LAB")
# elif(Town == "Lahti" and (Street != "Mukkulankatu" or Building != 19)):
#     print("You are in the correct town, but check the street address again")
# elif not(Town == "Lahti" and Street == "Mukkulankatu" and Building == 19):
#     print("You are lost...")

# #1. ehto: True JA 2. ehto False 

#import random

#print (random.random())
#print(random.randint(1, 6))

# Tee yksinkertainen kivi, sakset, paperi peli random metodia käyttäen.

import random

print("Valitse: 1 = kivi, 2 = sakset, 3 = paperi")
pelaaja = int(input("Anna numerosi: "))

vastustaja = random.randint(1, 3)
print("Vastustaja valitsi:", vastustaja)

if pelaaja == vastustaja:
    print("tasapeli")
elif (
    (pelaaja == 1 and vastustaja == 2) or
    (pelaaja == 2 and vastustaja == 3) or
    (pelaaja == 3 and vastustaja == 1)
):
    print("voitit pelin")
else:
    print("hävisit pelin")

