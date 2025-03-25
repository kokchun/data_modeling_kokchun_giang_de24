from pathlib import Path

sql_path = Path(__file__).parent / "sql"

def read_sql_file(sql_filename):
    with open(sql_path / sql_filename, 'r') as sql_file:
        return sql_file.read()
    

if __name__ == '__main__':
    print(read_sql_file("create_user.sql"))