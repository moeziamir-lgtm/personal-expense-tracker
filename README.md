# Personal Expense Tracker

A command-line expense tracking application built with Python to practice clean code, data validation, and file persistence.

## Features

- Add and view expenses
- Search expenses by category
- Delete expenses
- Calculate total spending
- Summarize expenses by category
- Validate user input
- Automatically save and load expenses using JSON
- Organize code into separate Python modules
- Use type hints and `TypedDict` for clearer data structures

## Technologies

- Python
- JSON
- `pathlib`
- Git and GitHub

## Project Structure

```text
personal-expense-tracker/
├── main.py
├── expense_manager.py
├── save_expense/
│   └── expenses.json
├── .gitignore
└── README.md
```

## How to Run

1. Install Python 3.10 or later.
2. Clone this repository:

   ```bash
   git clone https://github.com/moeziamir-lgtm/personal-expense-tracker.git
   ```

3. Enter the project directory:

   ```bash
   cd personal-expense-tracker
   ```

4. Run the application:

   ```bash
   python main.py
   ```

## What I Learned

- Structuring a Python application using modules and functions
- Working with lists and dictionaries
- Validating user input and handling exceptions
- Reading and writing JSON files
- Using type hints and `TypedDict`
- Managing project versions with Git

## Future Improvements

- Add automated unit tests
- Improve validation of loaded JSON data
- Add monthly spending reports

---

**Status:** Learning project and ongoing development.
