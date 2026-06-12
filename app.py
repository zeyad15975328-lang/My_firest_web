import string
import random

print("""──── ୨୧ ────
𝐖𝐄𝐋𝐂𝐎𝐌𝐄✿ ᭄⸙
──── ୨୧ ────""")


name = input("\nplease. Enter your quadruple name or more quadruple\n")

while len(name.split( )) < 4:
    print("please, Enter your quadruple name")
    name = input("\nplease. Enter your quadruple name or more quadruple\n")


age1 = int(input("\nplease, Enter your age \n"))

while age1 < 5:
    print("sorry. Age must be above 5 years.")
    age1 = int(input("\nplease, Enter your age\n "))

email1 = input("\nplease. Enter your email\n")


while "@gmail.com" not in email1:
    print("⚠️ you forgot ( @gmail.com )⚠️")
    email1 = input("please, rewrite your email.\n")

suggestion = input("\nDo you want to create a password for you (Yes / No)\n").capitalize()


 
letters = string.ascii_letters
numbers = string.digits
punctuations = string.punctuation
total1 = letters + numbers + punctuations

if suggestion == "Yes":
    password1_suggestion = random.choices(total1, k=8)
    finished_password = "".join(password1_suggestion)
    print(f"\nSuggested password is: {finished_password}\n")
else:
    print("\nOkay.\n")


if suggestion == "Yes":
    password1 = input("\nEnter the suggested password\n")
else:
    password1 = input("\nplease, Enter your password\n")

confirmed_password = input("\nplease, confirm the password\n")


while len(password1) < 8 or not any(c in total1 for c in password1) or password1 != confirmed_password:
    if len(password1) < 8:
        print("The length of the password must be at least 8")
    if password1 != confirmed_password:
        print("The password must match the confirmation password.")

    password1 = input("\nplease, rewrite your password\n")
    confirmed_password = input("\nplease, confirm the password\n")

user_info = {
    "username": name,
    "Age": age1,
    "email": email1,
    "password": password1
}

print("your account has been successfully created")

print(f'account is: {user_info["email"]}')
