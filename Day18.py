class PasswordManager:
    def __init__(self):
        self.passwords = {}

    def add_password(self, website, username, password):
        self.passwords[website] = {"username": username, "password": password}

    def remove_password(self, website):
        if website in self.passwords:
            del self.passwords[website]
        else:
            print("Website not found.")

    def get_password(self, website):
        if website in self.passwords:
            username = self.passwords[website]["username"]
            password = self.passwords[website]["password"]
            return f"Website: {website}\nUsername: {username}\nPassword: {password}"
        else:
            return "Website not found."


def main():
    password_manager = PasswordManager()

    while True:
        print("\n===== Password Manager =====")
        print("1. Add Password")
        print("2. Remove Password")
        print("3. Get Password")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            website = input("Enter website: ")
            username = input("Enter username: ")
            password = input("Enter password: ")
            password_manager.add_password(website, username, password)
            print("Password added successfully.")
        elif choice == "2":
            website = input("Enter website to remove password: ")
            password_manager.remove_password(website)
            print("Password removed successfully.")
        elif choice == "3":
            website = input("Enter website to get password: ")
            password_info = password_manager.get_password(website)
            print(password_info)
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
