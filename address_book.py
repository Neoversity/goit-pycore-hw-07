from datetime import datetime, timedelta
from collections import UserDict
from record import Record

# Оголосіть декоратор input_error
def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            return f"Error: {e}"
    return wrapper

@input_error
def add_birthday(args, book):
    if len(args) != 2:
        raise ValueError("Usage: add-birthday [name] [DD.MM.YYYY]")
    
    name, birthday = args
    record = book.find(name)
    if record:
        record.add_birthday(birthday)
        return f"Birthday added for {name}."
    else:
        return f"Contact '{name}' not found."

@input_error
def show_birthday(args, book):
    if len(args) != 1:
        raise ValueError("Usage: show-birthday [name]")
    
    name = args[0]
    record = book.find(name)
    if record and record.birthday:
        return f"{name}'s birthday: {record.birthday.value}"
    elif record:
        return f"{name} doesn't have a birthday set."
    else:
        return f"Contact '{name}' not found."


@input_error
def birthdays(args, book):
    upcoming_birthdays = book.get_upcoming_birthdays()
    if upcoming_birthdays:
        return "\n".join(str(record) for record in upcoming_birthdays)
    else:
        return "No upcoming birthdays in the next week."
    

@input_error
def change_phone(args, book):
    if len(args) != 2:
        raise ValueError("Usage: change [name] [new_phone]")
    
    name, new_phone = args
    record = book.find(name)
    if record:
        old_phone = str(record.phones[0])  # Припускаємо, що у кожного контакту є лише один номер телефону
        record.edit_phone(old_phone, new_phone)
        return f"Phone number for {name} changed from {old_phone} to {new_phone}."
    else:
        return f"Contact '{name}' not found."

@input_error
def show_phone(args, book):
    if len(args) != 1:
        raise ValueError("Usage: phone [name]")
    
    name = args[0]
    record = book.find(name)
    if record and record.phones:
        return f"{name}'s phone number: {record.phones[0]}"
    elif record:
        return f"{name} doesn't have a phone number set."
    else:
        return f"Contact '{name}' not found."

@input_error
def show_all(book):
    if book:
        return "\n".join(str(record) for record in book.values())
    else:
        return "Address book is empty."











class AddressBook(UserDict):
    def add_record(self, record):
        if not isinstance(record, Record):
            raise ValueError("Only Record objects can be added to AddressBook")
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name)

    def delete(self, name):
        if name in self.data:
            del self.data[name]

    def get_upcoming_birthdays(self):
        today = datetime.today().date()
        next_week = today + timedelta(days=7)
        upcoming_birthdays = []
        for record in self.data.values():
            if record.birthday:
                birthday_date = datetime.strptime(record.birthday.value, "%d.%m.%Y").date()
                birthday_this_year = birthday_date.replace(year=today.year)
                if birthday_this_year < today:
                    birthday_this_year = birthday_this_year.replace(year=today.year + 1)
                if today <= birthday_this_year <= next_week:
                    upcoming_birthdays.append(record)
        return upcoming_birthdays
