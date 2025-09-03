import sqlite3

try:
    # Connect to (or create) database
    conn = sqlite3.connect('fintech.db')
    cursor = conn.cursor()

    # Create Users table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        Name TEXT NOT NULL,
        Email TEXT UNIQUE,
        Balance REAL DEFAULT 0.00,
        JoinDate TEXT
    )
    ''')

    conn.commit()
    print("Table 'Users' created successfully in fintech.db")

    # Verify table creation
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='Users'")
    if cursor.fetchone():
        print("Confirmed: 'Users' table exists")
    else:
        print("Error: 'Users' table not found")

except sqlite3.Error as e:
    print(f"Error creating table: {e}")
finally:
    conn.close()