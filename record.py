from datetime import datetime

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    def __init__(self, value):
        super().__init__(value)

class Phone(Field):
    def __init__(self, value):
        if not value:
            raise ValueError("Phone number cannot be empty")
        try:
            self.validate(value)
        except ValueError as e:
            print(e)
        super().__init__(value)

    @staticmethod
    def validate(value):
        if len(value) != 10 or not value.isdigit():
            raise ValueError("Phone number must be 10 digits and contain only digits")

class Birthday(Field):
    def __init__(self, value):
        if not value:
            raise ValueError("Birthday cannot be empty")
        try:
            self.value = datetime.strptime(value, "%d.%m.%Y").date()
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")
        super().__init__(value)

    @staticmethod
    def validate(value):
        try:
            datetime.strptime(value, "%d.%m.%Y")
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")
        

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None

    def add_phone(self, phone):
        try:
            Phone.validate(phone)
            self.phones.append(Phone(phone))
        except ValueError as e:
            print(e)

    def remove_phone(self, phone):
        self.phones = [p for p in self.phones if str(p) != phone]

    def edit_phone(self, old_phone, new_phone):
        try:
            Phone.validate(new_phone)
            for phone in self.phones:
                if str(phone) == old_phone:
                    phone.value = new_phone
                    return
            print(f"Phone number {old_phone} not found.")
        except ValueError as e:
            print(e)

    def find_phone(self, phone):
        for p in self.phones:
            if str(p) == phone:
                return p
        return None

    def add_birthday(self, birthday):
        if self.birthday:
            raise ValueError("Birthday already exists for this record")
        self.birthday = Birthday(birthday)

    def __str__(self):
        birthday_str = str(self.birthday) if self.birthday else "None"
        return f"Contact name: {self.name.value}, phones: {'; '.join(str(p) for p in self.phones)}, birthday: {birthday_str}"

