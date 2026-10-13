departments = ["CSE", "ECE", "IT", "EEE"]

dept = input("Enter department: ")

if dept in departments:
    print("Department available")
else:
    print("Department not available")