from collections import UserDict
import re
from datetime import datetime, timedelta
import pickle

def save_data(book, filename="addressbook.pkl"):
    with open(filename, "wb") as f:
        pickle.dump(book, f)

def load_data(filename="addressbook.pkl"):
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return AddressBook()  # Повернення нової адресної книги, якщо файл не знайдено
class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    pass


class Phone(Field):
    def __init__(self, value):
        if self.validate(value):
            super().__init__(value)
        else:
            raise ValueError("Invalid phone number. It must contain exactly 10 digits.")

    def validate(self, value):
        return bool(re.fullmatch(r"\d{10}", value))


class Birthday(Field):
    def __init__(self, value):
        try:
            self.value = datetime.strptime(value, "%d.%m.%Y")
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def remove_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                self.phones.remove(p)
                break

    def edit_phone(self, phone_old, phone_new):
        for i, p in enumerate(self.phones):
            if p.value == phone_old:
                self.phones[i] = Phone(phone_new)
                break
        else:
            raise ValueError("Phone number not found.")

    def find_phone(self, phone_find):
        for p in self.phones:
            if p.value == phone_find:
                return p
        return None

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

    def add_birthday(self, birthday):
        self.birthday = Birthday(birthday)


class AddressBook(UserDict):
    def add_record(self, record: Record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name, None)

    def delete(self, name):
        self.data.pop(name, None)

    def __str__(self):
        return '\n'.join(str(record) for record in self.data.values())

    def get_upcoming_birthdays(self, days=7):
        upcoming_birthdays = []
        today = datetime.now().date()  # Ensure today is a date object

        for record in self.data.values():
            if record.birthday:
                # Convert birthday to date for comparison
                birthday_this_year = record.birthday.value.date().replace(year=today.year)

                if birthday_this_year < today:
                    birthday_this_year = record.birthday.value.date().replace(year=today.year + 1)

                if 0 <= (birthday_this_year - today).days <= days:
                    birthday_this_year = adjust_for_weekend(birthday_this_year)
                    upcoming_birthdays.append({
                        "name": record.name.value,
                        "congratulation_date": birthday_this_year.strftime("%d.%m.%Y")
                    })

        return upcoming_birthdays


def adjust_for_weekend(birthday):
    if birthday.weekday() >= 5:
        return find_next_weekday(birthday, 0)
    return birthday


def find_next_weekday(start_date, weekday):
    days_ahead = weekday - start_date.weekday()
    if days_ahead <= 0:
        days_ahead += 7
    return start_date + timedelta(days=days_ahead)


def input_error(func):
    def wrapper(args, book):
        try:
            return func(args, book)
        except (IndexError, KeyError, ValueError) as e:
            return str(e)

    return wrapper


@input_error
def add_birthday(args, book):
    name, birthday = args.split(maxsplit=1)
    record = book.find(name)
    if not record:
        return f"Contact {name} not found."
    record.add_birthday(birthday)
    return f"Birthday for {name} set to {birthday}."


@input_error
def show_birthday(args, book):
    name = args.strip()
    record = book.find(name)
    if not record:
        return f"Contact {name} not found."
    if record.birthday:
        return f"Birthday for {name} is {record.birthday.value.strftime('%d.%m.%Y')}."
    return f"No birthday set for {name}."


@input_error
def birthdays(args, book):
    days = int(args.strip()) if args else 7
    upcoming_birthdays = book.get_upcoming_birthdays(days)
    if not upcoming_birthdays:
        return "No upcoming birthdays."
    return "\n".join(f"{user['name']}: {user['congratulation_date']}" for user in upcoming_birthdays)


def parse_input(user_input):
    cmd, *args = user_input.split(maxsplit=1)
    cmd = cmd.strip().lower()
    return cmd, args[0] if args else ""


@input_error
def add_contact(args, book):
    name, phone = args.split(maxsplit=1)
    record = book.find(name)
    if record:
        record.add_phone(phone)
        return f"Phone number {phone} added to {name}."
    else:
        record = Record(name)
        record.add_phone(phone)
        book.add_record(record)
        return f"Contact {name} created with phone {phone}."


@input_error
def change_contact(args, book):
    name, phone_old, phone_new = args.split(maxsplit=2)
    record = book.find(name)
    if record:
        record.edit_phone(phone_old, phone_new)
        return f"Phone number for {name} changed from {phone_old} to {phone_new}."
    else:
        return f"Contact {name} not found."


@input_error
def phone_contact(args, book):
    name = args.strip()
    record = book.find(name)
    if record:
        phones = ', '.join(phone.value for phone in record.phones)
        return f"The phone numbers for {name} are: {phones}"
    else:
        return f"Contact {name} not found."


def all_contacts(book):
    return str(book)


def main():
    book = load_data()
    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Goodbye!")
            save_data(book)
            break

        elif command == "hello":
            print("How can I help you?")

        elif command == "add":
            print(add_contact(args, book))

        elif command == "change":
            print(change_contact(args, book))

        elif command == "phone":
            print(phone_contact(args, book))

        elif command == "all":
            print(all_contacts(book))

        elif command == "add-birthday":
            print(add_birthday(args, book))

        elif command == "show-birthday":
            print(show_birthday(args, book))

        elif command == "birthdays":
            print(birthdays(args, book))

        else:
            print("Invalid command.")






if __name__ == "__main__":
    main()

