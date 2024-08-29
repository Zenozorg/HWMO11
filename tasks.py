import sqlite3

conn = sqlite3.connect('example.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS example_table (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER,
    email TEXT
)
''')
conn.commit()

def read_all_rows():
    cursor.execute("SELECT * FROM example_table")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

def read_one_row(row_id):
    cursor.execute("SELECT * FROM example_table WHERE id = ?", (row_id,))
    row = cursor.fetchone()
    if row:
        print(row)
    else:
        print(f"Row with ID {row_id} not found.")
    
def insert_row(name, age, email):
    cursor.execute("INSERT INTO example_table (name, age, email) VALUES (?, ?, ?)", (name, age, email))
    conn.commit()
    print("Row inserted.")


def delete_row(row_id):
    cursor.execute("DELETE FROM example_table WHERE id = ?", (row_id,))
    conn.commit()
    if cursor.rowcount > 0
        print(f"Row with ID {row_id} deleted.")
    else:
        if __name__ in "__main__":
            insert_row('Alice', 30, 'alice@example.com')
            insert_row('Bob', 25, 'bob@example.com')

            print("All rows:")
            read_all_rows()

            print("\nSingle row with ID 1:")
            read_one_row(1)

            print("\nDeleting row with ID 1:")
            delete_row(1)

            print("\nAll rows after deletion:")
            read_all_rows()

conn.close