price = 1000
quantity = 2
member = True
coupon = True

total = price * quantity

if member:
    total -= total * 10 / 100

if coupon:
    total -= total * 5 / 100

print("Final payable amount =", total)