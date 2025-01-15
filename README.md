# SQL
SQL Reader and Maker is a lightweight and user-friendly tool designed to simplify database operations. It allows users to read, execute, and generate SQL queries with ease, making it ideal for both beginners and advanced users.

This project consists of two Python scripts that work together to process rock type data, store it in an SQLite database, and retrieve it for display.

## Files
1. **SQL.py**:
   - Reads and parses data from a Word document.
   - Organizes the data into categories, rock types, and associated minerals.
   - Stores the structured data into an SQLite database.

2. **SQL_Reader.py**:
   - Connects to the SQLite database created by `SQL.py`.
   - Retrieves and displays all the data from the database in a tabular format.

---

## How to Use

### Prerequisites
- Python 3.x installed on your system.
- Required libraries:
  - `python-docx`: For reading Word documents.
  - `sqlite3`: For database operations (included with Python).

Install `python-docx` if not already installed:
```bash
pip install python-docx
```

### Step 1: Create the Database
1. Update the `doc_path` variable in `SQL.py` with the path to your Word document containing rock type data.
2. Update the `db_path` variable with the desired output path for the SQLite database file.
3. Run `SQL.py`:
   ```bash
   python SQL.py
   ```
4. A database named `rock_types.db` (or your specified name) will be created with the parsed data.

### Step 2: Read the Data
1. Update the `db_path` variable in `SQL_Reader.py` with the path to the created SQLite database.
2. Run `SQL_Reader.py`:
   ```bash
   python SQL_Reader.py
   ```
3. The script will fetch and display the data from the database.

---

## Example Output

### SQL Reader Output:
```
ID | Rock Type | Category | Minerals
-------------------------------------------------
1  | Basalt    | Igneous  | Feldspar, Pyroxene
2  | Limestone | Sedimentary | Calcite, Quartz
```

---

## License
This project is licensed under the MIT License. You are free to use, modify, and distribute this code.

