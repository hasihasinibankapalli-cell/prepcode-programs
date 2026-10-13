blocked = ["admin", "guest", "root"]

username = input("Enter username: ")

if username not in blocked:
    print("Username available")
else:
    print("Username blocked")