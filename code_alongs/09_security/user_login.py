from connect_postgres import connect_postgres
from sqlalchemy import text

username = input("Enter your username:    ")
password = input("Enter your password:    ")

with connect_postgres().connect() as conn:
    result = conn.execute(
        text(
            f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
        )
    ).fetchall()
    
    if result:
        print("Login successful")
        print("Eat all ice cream")
    else:
        print("Anotha failure")