food_price = 250
quantity = 2
delivary_charge = 50
discount_percentage = 10

subtotal = food_price * quantity
discount = subtotal * discount_percentage / 100
final_bill = subtotal + delivary_charge - discount

print("final bill:", final_bill)