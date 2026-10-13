age = int(input("Enter age: "))
price = 200

if age < 12:
    price = price * 50 / 100
elif age >= 60:
    price = price * 70 / 100

print("Ticket price = Rs.", price)