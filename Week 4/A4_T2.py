print("Program starting.")
print("")

start = int(input("Insert starting value: "))
stop = int(input("Insert stopping value: "))
print("")

print("Starting for-loop:")
for i in range(start, stop + 1):
    if i != stop:
        print(i, end=" ")
    else:
        print(i)
print("")

print("Program ending.")