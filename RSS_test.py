import sqlite3
# this function prints all the recipes in the database
def database_test():
    conn = sqlite3.connect('foodDatabase.db')
    cursor = conn.cursor()
    print("Recipes Table:")
    cursor.execute("SELECT * FROM Recipes;")
    print(cursor.fetchall())
    conn.close()
# testing the database is populated
database_test()