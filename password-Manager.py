import pyperclip

FILE_NAME = "PASSWORDS.txt"


def save_password():
    website = input("Enter the website: ")
    password = input("Enter the password: ")

    with open(FILE_NAME, "a") as file:
        file.write(f"{website}<||>{password}\n")

    print("Password saved successfully!")


def get_password():
    website = input("Enter the website: ")

    try:
        with open(FILE_NAME, "r") as file:

            for line in file:
                line = line.strip()

                if "<||>" in line:
                    saved_website, password = line.split("<||>", 1)

                    if saved_website == website:
                        pyperclip.copy(password)

                        print("Password copied to clipboard!")
                        return

            print("Website not found.")

    except FileNotFoundError:
        print("No passwords have been saved yet.")


def main():
    while True:

        print("\n===== PASSWORD MANAGER =====")
        print("1. Save a password")
        print("2. Get a password")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            save_password()

        elif choice == "2":
            get_password()

        elif choice == "3":
            print("Exiting Password Manager...")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()