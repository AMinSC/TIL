import mariadb
import sys

# Configure your MariaDB connection
config = {
    'user': 'root',
    'password': '1218',
    'host': 'localhost',
    'port': 3306,
    'database': 'beme_test'
}

try:
    # Connect to MariaDB
    conn = mariadb.connect(**config)

    # Create a cursor object
    cur = conn.cursor()

    # Create a new table
    cur.execute("CREATE TABLE IF NOT EXISTS test_table (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(100), age INT)")

    # Insert data into the table
    cur.execute("INSERT INTO test_table (name, age) VALUES (?, ?)", ("Alice", 30))
    cur.execute("INSERT INTO test_table (name, age) VALUES (?, ?)", ("Bob", 25))

    # Commit the transaction
    conn.commit()

    print("Data inserted successfully.")

except mariadb.Error as e:
    print(f"Error connecting to MariaDB: {e}")
    sys.exit(1)

finally:
    # Close the connection
    if conn:
        conn.close()