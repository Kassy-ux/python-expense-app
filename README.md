# Python Expense App

A simple command-line application built with Python to help you track your income and expenses, manage your budget, and get a clear picture of your finances.

## Features

- Add income and expense entries with descriptions and amounts
- Categorize transactions (e.g., Food, Transport, Rent, Entertainment)
- View a summary of your total income, total expenses, and current balance
- List all recorded transactions
- Delete or edit existing entries

## Prerequisites

- Python 3.8 or higher

## Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/Kassy-ux/python-expense-app.git
   cd python-expense-app
   ```

2. **Create and activate a virtual environment** (recommended)

   ```bash
   python -m venv venv
   source venv/bin/activate      # macOS/Linux
   venv\Scripts\activate         # Windows
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the application from the project root:

```bash
python main.py
```

Follow the on-screen prompts to:

| Option | Action |
|--------|--------|
| `1` | Add a new transaction |
| `2` | View all transactions |
| `3` | View account summary |
| `4` | Delete a transaction |
| `5` | Exit |

### Example

```
Welcome to Python Expense App!

1. Add transaction
2. View transactions
3. View summary
4. Delete transaction
5. Exit

Enter your choice: 1
Enter type (income/expense): expense
Enter amount: 25.50
Enter category: Food
Enter description: Lunch at café

Transaction added successfully!
```

## Project Structure

```
python-expense-app/
├── main.py           # Application entry point
├── expenses.py       # Core logic for managing transactions
├── data/
│   └── transactions.json  # Stored transaction data
├── requirements.txt  # Python dependencies
└── README.md
```

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a new feature branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -m "Add your feature"`)
4. Push to your branch (`git push origin feature/your-feature`)
5. Open a Pull Request

## License

This project is licensed under the [MIT License](LICENSE).
