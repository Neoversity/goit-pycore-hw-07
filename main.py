from record import Record, Name, Birthday, parse_input, hello, close
from address_book import AddressBook, add_birthday, show_birthday, birthdays, change_phone, show_phone, show_all



def main():
    book = AddressBook()
    while True:
        print("add", "change", "phone", "all", "add-birthday", "show-birthday", "birthdays", "hello","close", "exit")
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command == "add":
            if len(args) != 2:
                print("Usage: add [name] [phone]")
            else:
                name, phone = args
                record = book.find(name)
                if record:
                    record.add_phone(phone)
                    print(f"Phone number added to existing contact '{name}'.")
                else:
                    new_record = Record(name)
                    new_record.add_phone(phone)
                    book.add_record(new_record)
                    print(f"New contact '{name}' added with phone number '{phone}'.")

        elif command == "change":
            if len(args) != 3:
                print("Usage: change [name] [old_phone] [new_phone]")
            else:
                name, old_phone, new_phone = args
                record = book.find(name)
                if record:
                    record.edit_phone(old_phone, new_phone)
                else:
                    print(f"Contact '{name}' not found.")

        elif command == "phone":
            if len(args) != 1:
                print("Usage: phone [name]")
            else:
                name = args[0]
                record = book.find(name)
                if record:
                    print(f"{name}'s phone numbers: {', '.join(str(p) for p in record.phones)}")
                else:
                    print(f"Contact '{name}' not found.")

        elif command == "all":
            print(show_all(book))
            
        elif command == "add-birthday":
            if len(args) != 2:
                print("Usage: add-birthday [name] [DD.MM.YYYY]")
            else:
                name, birthday = args
                print(add_birthday([name, birthday], book))

        elif command == "show-birthday":
            if len(args) != 1:
                print("Usage: show-birthday [name]")
            else:
                name = args[0]
                print(show_birthday([name], book))

        elif command == "birthdays":
            upcoming_birthdays = book.get_upcoming_birthdays()
            if upcoming_birthdays:
                print("\n".join(str(record) for record in upcoming_birthdays))
            else:
                print("No upcoming birthdays in the next week.")


        elif command == "hello":
            print(hello())


        elif command in ["close", "exit"]:
            print(close())
            break
        else:
            print("Invalid command. Please try again.")
            


if __name__ == "__main__":
    main()

