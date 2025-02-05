import random
import string

adjectives = ["Bold","Clever","Swift","Fearless","Mighty","Vivid","Fierce","Jolly","Noble","Radiant","Stealthy","Witty","Lively","Brave","Zesty"]
nouns = ["Falcon","Panther","Titan","Shadow","Phoenix","Warrior","Thunder","Knight","Dragon","Wolf","Cyclone","Gladiator","Vortex","Maverick","Specter"]

def generate_username(add_numbers=False, add_special_chars=False):
    adj = random.choice(adjectives)
    noun = random.choice(nouns)
    username = adj + noun
    
    if add_numbers:
        username += str(random.randint(10, 99))
    if add_special_chars:
        username += random.choice("!@#$%&*")
    
    return username

def save_to_file(username):
    with open("usernames.txt", "a") as file:
        file.write(username + "\n")

print("Welcome to the Random Username Generator!")

again = "yes"
while again == "yes":
    add_numbers = input("Include numbers? (yes/no): ").strip().lower() == "yes"
    add_special_chars = input("Include special characters? (yes/no): ").strip().lower() == "yes"

    username = generate_username(add_numbers, add_special_chars)
    print(f"Generated Username: {username}")

    save_to_file(username)
    print("Username saved to 'usernames.txt'.")

    again = input("Would you like to generate another username? (yes/no): ").strip().lower()

print("Thank you for using the username generator.")
