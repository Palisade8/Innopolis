# ****** Аттестационное  Задание2

import requests
from bs4 import BeautifulSoup

# URL страницы с новостями
url = 'https://www.company.rt.ru/ir/news_calendar/'

# Запрос к веб-странице
response = requests.get(url)
response.encoding = 'windows-1251'  # Установка кодировки ...

# Проверка доступности
if response.status_code == 200:
    # Парсинг HTML-кода страницы
    soup = BeautifulSoup(response.text, 'html.parser')

    # Список для хранения новостей
    news_list = []

    # Поиск блоков новостей
    news_items = soup.find_all('div', class_='news_item')  # класс новостей

    for item in news_items[:20]:  # Ограничение 20 новостей
        date = item.find('div', class_='item_date').text.strip()  # дата
        title = item.find('div', class_='item_text').text.strip()  # заголовок
        link = item.find('a')['href']  # Ссылка на новость

        # Создание словаря для каждой новости
        news_list.append({
            'date': date,
            'title': title,
            'link': link
        })

    # Вывод списка
    print(news_list)
else:
    print(f'Ошибка при запросе: {response.status_code}')