import psycopg2
 
# Connect to your postgres DB
conn = psycopg2.connect("dbname=dbtest user=postgres port=5432 password=FcLiverpool8")
 
# Open a cursor to perform database operations
cur = conn.cursor()
 
# Execute a query
cur.execute("SELECT * FROM test")
 
# Retrieve query results
records = cur.fetchall()

print(records)