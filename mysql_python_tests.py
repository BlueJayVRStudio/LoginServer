## pip install mysql-connector-python


import mysql.connector

# Configure database connection parameters
db_config = {
    'host': 'localhost',
    'user': 'your_username',
    'password': 'your_password',
    'database': 'your_database_name'
}

# Establish a database connection
try:
    conn = mysql.connector.connect(**db_config)
    print("Connection established!")
except mysql.connector.Error as e:
    print(f"Error connecting to MySQL: {e}")

# Check if the connection was successful
if conn.is_connected():
    # Create a cursor from the connection
    cursor = conn.cursor()

    # Example query: Fetch data
    query = "SELECT * FROM your_table_name"
    cursor.execute(query)

    # Fetch and display the results
    for row in cursor.fetchall():
        print(row)

    # Close the cursor
    cursor.close()
else:
    print("Failed to connect!")

# Close the connection
conn.close()