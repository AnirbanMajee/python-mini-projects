SECURE = (("s", "$"), ("f", "5"), ("O", "7"), ("y", "5"), ("j", "4"),
          ("t", "$"), ("x", "00"), ("v", "$#"), ("w", "$%"),)

def securePassword(password):
    for a,b in SECURE:
        password = password.replace(a, b)
        return password
    
if __name__ == "__main__":
    password = input("Enter a password \n")
    password = securePassword(password)
    print(f"Your secure password is : {password}")
