# print() # funktiokutsu
# print("Hello") # "Hello" on funktion parametri
# len()



# while True:
#     print("I can do this forever")

# Voidaan tehdä itse funktioita, aiemmin ollaan vaan käytetty niitä.
# Ensin funktiot, sitten muut

# def greet(name):
#     print(f"Hello {name}")

# print("Here I am")
# name = "Lassi"
# greet(name) 

# def greet(name):
#     return f"Hello, {name}"

# print(greet("Lassi"))

# def greeting_airport(person, age):
#     print(f"How do you do {person}")
#     if age >= 18:
#         print("Welcome to your flight")
#     else:
#         print(f"You need to wait for {18-age} years to fly solo.")

# greeting_airport("Lassi", 30)

#Primary number = Luku joka on suurempi kuin 1, eli siis alkuluku, sillä on kaksi positiivista jakajaa, Esimerkkejä alkuluvuista:
# 2, 3, 5, 7, 11, 13, 17, 19, 23…

# Tee ohjelma, joka kysyy käyttäjältä kokonaislukua. Testaa funktiolla, onko se alkuluku (prime number) vai ei. 
# Kysy uutta lukua, kunnes käyttäjä pyytää lopettamaan kysymyksen. 



def onko_alkuluku(luku):
    if luku < 2:
        return False
    for i in range(2, int(luku ** 0.5) + 1):
        if luku % i == 0:
            return False
    return True

while True:
    user_input = input("Anna kokonaisluku (tai kirjoita 'lopeta' lopettaaksesi): ")

    if user_input.lower() == "lopeta":
        print("Ohjelma lopetetaan.")
        break

    if not user_input.isdigit() and not (user_input.startswith("-") and user_input[1:].isdigit()):
        print("Anna kelvollinen kokonaisluku!")
        continue

    luku = int(user_input)

    if onko_alkuluku(luku):
        print(f"{luku} on alkuluku.")
    else:
        print(f"{luku} ei ole alkuluku.")


