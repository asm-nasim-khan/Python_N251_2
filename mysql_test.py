import mysql.connector

# Establish a connection
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345",
    database="fashion_db"
)

# Create a cursor
cursor = conn.cursor()

# Execute a query
cursor.execute("SELECT * FROM brands")

# Fetch results
results = cursor.fetchall()
for row in results:
    print(row)

# Close the connection
cursor.close()
conn.close()
