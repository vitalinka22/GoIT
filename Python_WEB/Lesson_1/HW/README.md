# Contact Management System

## Overview

This project is a simple contact management system implemented in Python. It allows users to add, update, and manage contact details including phone numbers and birthdays. The data is stored in a binary file using Python's `pickle` module.

## Features

- **Add Contacts:** Add new contacts with names and phone numbers.
- **Change Contacts:** Update existing contact details.
- **Show Phones:** Display phone numbers associated with a contact.
- **Show All Contacts:** List all contacts in the address book.
- **Add Birthdays:** Add birthday information to contacts.
- **Show Birthdays:** Display birthday information for a contact.
- **Upcoming Birthdays:** List upcoming birthdays within a specified number of days.

## Project Structure

- `Field`: Base class for different types of data fields.
- `Name`: Represents the contact's name.
- `Phone`: Represents the contact's phone number.
- `Birthday`: Represents the contact's birthday.
- `Record`: Represents a contact with associated phone numbers and birthday.
- `AddressBook`: Manages the collection of `Record` objects, including adding, finding, deleting, and getting upcoming birthdays.
- `Command`: Abstract base class for commands, with subclasses for specific operations.
- `ConsoleUI`: Command-line interface for user interaction.

## Installation

Clone the repository to your local machine:

```sh
git clone https://github.com/vitalinka22/GoIT.git
cd repository
```

## Usage

Run the program using Python:

```sh
python main.py
```

The program will prompt you to enter commands. Here are some example commands you can use:

- `add <name> <phone>`: Add a new contact with a phone number.
- `change <name> <old_phone> <new_phone>`: Update an existing contact's phone number.
- `phone <name>`: Show all phone numbers for a contact.
- `all`: Show all contacts.
- `add-birthday <name> <date>`: Add a birthday to a contact (format: DD.MM.YYYY).
- `show-birthday <name>`: Show the birthday for a contact.
- `birthdays`: List upcoming birthdays within the next 7 days.

### Example Commands

```sh
add John 1234567890
change John 1234567890 0987654321
phone John
add-birthday John 15.09.1990
show-birthday John
birthdays
```

## Code Structure

- **Classes:**
  - `Field`: Base class for defining various types of fields.
  - `Name`, `Phone`, `Birthday`: Inherit from `Field` and add specific validations.
  - `Record`: Represents a contact record.
  - `AddressBook`: Manages all contacts and provides functionality to interact with them.
  - `ConsoleUI`, `Command`: Provide a command-line interface and command execution framework.

- **Functions:**
  - `input_error`: Decorator to handle common input errors.
  - `parse_input`: Helper function to parse user input.
  - `load_data`: Load address book data from a file.

## Contributing

Feel free to fork the repository and submit pull requests. Ensure that you follow the coding conventions and include tests for new features or bug fixes.

## Contact

For any questions or feedback, please open an issue or contact [vitalinka.alipova2002@gmail.com].


