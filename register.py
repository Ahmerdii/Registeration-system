import json

# Load database
try:
    with open("users.json", "r") as file:
        users = json.load(file)
    print("Database loaded!")
except:
    users = {"ahmed": "1234"}
    print("New database created!")

def login(username, password):
    return username in users and users[username] == password

def register(username, password):
    if username in users:
        print("User already exists!")
        return False
    users[username] = password
    with open("users.json", "w") as file:
        json.dump(users, file)
    print(f"Account {username} saved to file!")
    return True

# Menu
while True:
    print("\n1. Login | 2. Register | 3. Exit")
    choice = input("Choose: ")

    if choice == "1":
        u = input("Username: ")
        p = input("Password: ")
        if login(u, p):
            print(f"Welcome {u}!")
            break
        else:
            print("Wrong login")

    elif choice == "2":
        u = input("New username: ")
        p = input("New password: ")
        register(u, p)

    elif choice == "3":
        break