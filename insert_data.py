import sqlite3

try:
    conn = sqlite3.connect('fintech.db')
    cursor = conn.cursor()
    cursor.execute("INSERT OR IGNORE INTO Users (Name, Email, Balance, JoinDate) VALUES ('John Doe', 'john@example.com', 100.50, '2025-09-03')")
    cursor.execute("INSERT OR IGNORE INTO Users (Name, Email, Balance, JoinDate) VALUES ('Jane Smith', 'jane@example.com', 200.00, '2025-09-04')")
    conn.commit()
    print("Data inserted successfully")
    cursor.execute("SELECT * FROM Users")
    for row in cursor.fetchall():
        print(row)
except sqlite3.Error as e:
    print(f"Error: {e}")
finally:
    conn.close()