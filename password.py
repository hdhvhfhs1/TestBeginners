correct_password = "open123"
attempts = 0
max_attempts = 3

while attempts < max_attempts:
    password = input("Enter Password: ")
    if password == correct_password:
        print("Correct Password")
        break
    else:
        attempts += 1

if attempts == max_attempts:
    print("Locked")
