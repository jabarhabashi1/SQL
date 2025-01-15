from docx import Document
import sqlite3

# Step 1: Read the Word document
doc_path = r"C:\Users\your data.docx"  # Replace with your file path
doc = Document(doc_path)

# Step 2: Parse the document and organize data
rock_data = []

current_category = None
for paragraph in doc.paragraphs:
    text = paragraph.text.strip()
    if not text:
        continue  # Skip empty lines
    if ":" not in text:
        current_category = text  # It's a category title
    else:
        rock_type, minerals = text.split(":", 1)
        minerals = [mineral.strip() for mineral in minerals.split(",")]
        rock_data.append((rock_type.strip(), current_category, ", ".join(minerals)))

# Step 3: Create SQLite database and table
db_path = r'C:\Users\Jabar\Desktop\rock_types.db'  # Output SQLite database file
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS RockTypes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    RockType TEXT,
    Category TEXT,
    Minerals TEXT
)
""")

# Step 4: Insert data into the table
cursor.executemany("""
INSERT INTO RockTypes (RockType, Category, Minerals) VALUES (?, ?, ?)
""", rock_data)

conn.commit()
conn.close()

print(f"Database created successfully at {db_path}")
