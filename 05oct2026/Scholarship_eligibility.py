percentage = int(input("enter percentage:"))
attendance = int(input("enter attendance:"))

if percentage >= 85 and attendance >= 75:
    print("eligible for scholarship")
else:
    print("not eligible for scholarship")