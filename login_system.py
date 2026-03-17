import getpass

def login():
    password = "nala"
    attempt = 1

    while attempt <= 10: 
        print(f"Attempt {attempt} of 10")
        tentative = getpass.getpass("Enter your password: ")
        if tentative == "":
            print("Password cannot be empty!")
            continue
        elif tentative == password:
            print("Allowed access! Welcome back!")
            return
        else:
            print("Oh - this is not your password, try again!\n")   
            attempt += 1
    print("Too many failed attempts. Access blocked!")

if __name__ == "__main__":
    login()
