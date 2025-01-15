import sqlite3

# اتصال به پایگاه داده
db_path = r'C:\Users\Jabar\Desktop\rock_types.db'  # مسیر فایل پایگاه داده
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# خواندن تمام داده‌ها از جدول
cursor.execute("SELECT * FROM RockTypes")
rows = cursor.fetchall()

# نمایش داده‌ها
print("ID | Rock Type | Category | Minerals")
print("-" * 100)
for row in rows:
    print(f"{row[0]} | {row[1]} | {row[2]} | {row[3]}")

# بستن اتصال
conn.close()
