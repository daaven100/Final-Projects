print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10%, 12%, or 15%? "))
people = int(input("How many people to split the bill? "))

first = bill * (1 + tip / 100)
second = first / people

# Another way to get the final code
#433.76final = round(second, 2)
final = "{:.2f}".format(second)

print(f"Each person should pay: ${final}")

#separationnnnnn

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

bill = 0

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age < 12:
        bill = 5
        print("Child tickets are $5.")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7.")
    elif 45 <= age <= 55:
        print("You enter for free")
    else:
        bill = 12
        print("Adult tickets are $12.")

    wants_photo = input("Do you want a photo taken? yes or no? ")
    if wants_photo == "yes":
        bill += 3

    print(f"Your final bill is {bill}.")

else:
    print("Sorry, you have to grow taller before you can ride.")