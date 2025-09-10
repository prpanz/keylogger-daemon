import sqlite3

def create_db(path_to_db: str, table_name: str) -> bool:
    with sqlite3.connect(path_to_db) as connection:
        cursor = connection.cursor()
        try:
            cursor.execute(
                f'''CREATE TABLE IF NOT EXISTS {table_name}(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                symbol TEXT,
                date TEXT
                )'''
            )
            connection.commit()
            return True
        except sqlite3.Error as err:
            print(err)
            return False

def insert_db(path_to_db: str, table_name: str, data: list) -> bool:
    
    with sqlite3.connect(path_to_db) as connection:
        cursor = connection.cursor()
        try:
            cursor.executemany(
                    f'''INSERT INTO {table_name} (symbol, date) VALUES (?, ?)''', data
                )
            connection.commit()
            return True
        except sqlite3.Error as err:
            print(err)
            connection.rollback()
            return False
        
def show_db(path_to_db: str, table_name: str):
    with sqlite3.connect(path_to_db) as connection:
        cursor = connection.cursor()
        cursor.execute(f'SELECT * FROM {table_name}')
        return cursor.fetchall()