import sqlite3

# Создание или подключение к базе данных
conn = sqlite3.connect('database.db')

# Создание курсора
c = conn.cursor()

# Создание таблицы Content
c.execute('''CREATE TABLE IF NOT EXISTS content (
             id INTEGER PRIMARY KEY AUTOINCREMENT,
             text TEXT,
             keywords TEXT,
             tag TEXT,
             timestampdata DATETIME)''')

# Закрытие соединения с базой данных
conn.close()