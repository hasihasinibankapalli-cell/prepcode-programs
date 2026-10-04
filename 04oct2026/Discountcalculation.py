price = int(input("enter the price:"))
discount = int(input("enter the discount:"))

discount_amount = (discount/100)*price

print(f"discount amount:{discount_amount}")
print(f"final price: {price-discount_amount}")