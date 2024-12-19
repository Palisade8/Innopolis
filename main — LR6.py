print("Добрый день")
print("Лабораторная работа 6")

from flask import Flask, render_template
import sqlite3
import os

# Создаем приложение Flask
app = Flask(__name__)

# Функция для инициализации базы данных
def init_db():
    conn = sqlite3.connect('gifts.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS gifts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        gift TEXT,
        price REAL,
        status TEXT
    )''')

    # Добавляем данные, если таблица пустая
    cursor.execute("SELECT COUNT(*) FROM gifts")
    if cursor.fetchone()[0] == 0:
        gifts = [
            ('Иван Иванович', 'Санки', 2000, 'не куплен'),
            ('Ирина Сергеевна', 'Цветы', 3000, 'куплен'),
            ('Семен Семенович', 'Глобус', 2500, 'не куплен'),

        ]
        cursor.executemany("INSERT INTO gifts (name, gift, price, status) VALUES (?, ?, ?, ?)", gifts)
    conn.commit()
    conn.close()

@app.route('/')
def index():
    conn = sqlite3.connect('gifts.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM gifts")
    gifts = cursor.fetchall()
    conn.close()
    return render_template('index.html', gifts=gifts)

# Запускаем базу данных и приложение
if __name__ == '__main__':
    init_db()
    app.run(debug=True)

# Определяем путь к папке templates
folder_path = 'templates'
file_name = 'index.html'
file_path = os.path.join(folder_path, file_name)

# Создание папки, если она не существует
os.makedirs(folder_path, exist_ok=True)

# Заполняем HTML файл

html_content = '''<!DOCTYPE html>
<html lang="ru">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="styles.css">

    <title>Список подарков</title>
</head>
<body>
    <h1>Подарки на Новый Год</h1>
    <table>
        <tr>
            <th>ФИО</th>
            <th>Подарок</th>
            <th>Стоимость</th>
            <th>Статус</th>
        </tr>
        {% for gift in gifts %}
        <tr>
            <td>{{ gift[1] }}</td>
            <td>{{ gift[2] }}</td>
            <td>{{ gift[3] }}</td>
            <td>{{ gift[4] }}</td>
        </tr>
        {% endfor %}
    </table>
</body>
</html>
'''

# Запись содержимого в файл
with open(file_path, 'w', encoding='utf-8') as file:
    file.write(html_content)

print(f'Файл {file_name} успешно создан в папке {folder_path}.')