# ****** Аттестационное  Задание
import pandas as pd
import fastavro
import io

# читаем файл
fil = pd.read_csv('Sheet1.csv')
#Уникальные значения в столбце Брэнд
uniq_brand = fil['Бренд'].unique()

#создание списка  для записи в AVRO файл
data = [{'номер строки': idx, 'имя бренда': brand} for idx, brand in enumerate(uniq_brand)]

#описание схемы AVRO файла
schema = {
    'type': 'record',
    'name': 'Brand',
    'fields': [
        {'name': 'номер строки', 'type': 'int'},
        {'name': 'имя бренда', 'type': 'string'}
    ]
}
#запись в файл
with io.BytesIO() as f:
    fastavro.writer(f, schema, data)
    f.seek(0)
    with open('brands.avro', 'wb') as avro_file:
        avro_file.write(f.read())