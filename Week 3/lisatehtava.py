# #Tehtävä:
# Jos käyttäjätunnus = omaNimi ja ikä >= 18 ja käyttäjä on admin => avataan admin sivu
# Jos käyttäjätunnus = omaNimi ja ikä >= 18 => avataan käyttäjäsivu
# Jos ikä < 18 => kerrotaan käyttäjälle: Ikä ei riitä
# Jos käyttäjätunnus != omaNimi => Pääsy kielletty 

# Admin tunnuksilla valikko: 1. Lisää uusi käyttäjä, 2. tarkista laitteen toiminta, 3. exit
# Käyttäjäsivulla valikko: 1. Tarkista omat tiedot, 2. exit

print("Program starting.")
print("Welcome to the system.")

Username = input("Insert your username: ")
Age = int(input("Insert your age: "))
Admin = input("Are you an admin (yes/no): ")

if Username == "Lassi" and Age >= 18 and Admin == "yes":
    print("Accessing admin page...")
    print("Options:")
    print("1 - Add new user")
    print("2 - Check device functionality")
    print("0 - Exit")
    Choice = int(input("Your choice: "))

    if Choice == 1:
        NewUser = input("Insert new username: ")
        NewUserAge = int(input("Insert new user's age: "))
        NewUserAdmin = input("Is the new user an admin? (yes/no): ")
        print(f"New user {NewUser} added.")
        print("Program ending.")

    elif Choice == 2:
        print("All devices are functional.")
        print("Program ending.")

    elif Choice == 0:
        print("Exiting...")
        print("Program ending.")

    else:
        print("Unknown option.")
        print("Program ending.")

elif Username == "Lassi" and Age >= 18 and Admin != "yes":
    print("Accessing user page...")
    print("Options:")
    print("1 - Check my details")
    print("0 - Exit")
    Choice = int(input("Your choice: "))

    if Choice == 1:
        print(f"Username: {Username}, Age: {Age}")
        print("Program ending.")

    elif Choice == 0:
        print("Exiting...")
        print("Program ending.")

    else:
        print("Unknown option.")
        print("Program ending.")

elif Age < 18:
    print("Age is not sufficient.")
    print("Program ending.")

elif Username != "Lassi":
    print("Access denied.")
    print("Program ending.")

