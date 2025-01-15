import sqlite3

# Connect to the database
db_path = r'C:\Users\your data.db'  # Database file path
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Read all data from the table
cursor.execute("SELECT * FROM RockTypes")
rows = cursor.fetchall()

# Display data
print("ID | Rock Type | Category | Minerals")
print("-" * 100)
for row in rows:
    print(f"{row[0]} | {row[1]} | {row[2]} | {row[3]}")

# Close connection
conn.close()
