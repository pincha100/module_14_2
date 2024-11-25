import sqlite3

connection = sqlite3.connect("babax.db")
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER,
    balance INTEGER NOT NULL
)
''')

cursor.execute("SELECT COUNT(*) FROM Users")
if cursor.fetchone()[0] == 0:
    users_data = [
        ("User1", "example1@gmail.com", 10, 1000),
        ("User2", "example2@gmail.com", 20, 1000),
        ("User3", "example3@gmail.com", 30, 1000),
        ("User4", "example4@gmail.com", 40, 1000),
        ("User5", "example5@gmail.com", 50, 1000),
        ("User6", "example6@gmail.com", 60, 1000),
        ("User7", "example7@gmail.com", 70, 1000),
        ("User8", "example8@gmail.com", 80, 1000),
        ("User9", "example9@gmail.com", 90, 1000),
        ("User10", "example10@gmail.com", 100, 1000),
    ]
    cursor.executemany("INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)", users_data)

# Обновление баланса у каждой второй записи, начиная с первой
cursor.execute("UPDATE Users SET balance = 500 WHERE id % 2 = 1")

# Удаление каждой третьей записи, начиная с первой
cursor.execute("DELETE FROM Users WHERE id % 3 = 0")

# Удаление записи с id = 6
cursor.execute("DELETE FROM Users WHERE id = ?", (6,))

# Подсчёт общего количества записей
total_users = cursor.execute("SELECT COUNT(*) FROM Users").fetchone()[0]

# Подсчёт суммы всех балансов
total_balance = cursor.execute("SELECT SUM(balance) FROM Users").fetchone()[0]

# Вычисление и вывод среднего баланса
if total_users > 0:  # Проверка на случай, если нет пользователей
    average_balance = total_balance / total_users
    print(f"Средний баланс всех пользователей: {average_balance:.2f}")
else:
    print("Нет данных о пользователях.")

connection.commit()
connection.close()
