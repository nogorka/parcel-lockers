import csv
import numpy as np
import os
import csv
import pandas as pd

# Получение списка всех файлов в директории
def get_all_filenames(directory_path):
    filenames = []
    for filename in os.listdir(directory_path):
        if os.path.isfile(os.path.join(directory_path, filename)):
            filenames.append(filename)
    return filenames

# Чтение csv из файла
def load_csv(file_path):
    with open(file_path, 'r', encoding='utf-8') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        data = [row for row in csv_reader]
    return data

# Вытаскивание маршрута из файла
def get_route(dirname, filename):
    path = os.path.join('public', dirname, filename)
    df = load_csv(path)
    return np.array([row['id'] for row in df])

# Чтение точек и преобразование к формату работы { 'id': (lat, long), ....}
def read_csv_to_dict(file_path):
    data_dict = {}

    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            # Преобразуем значения широты и долготы в кортеж
            data_dict[row['id']] = (float(row['lat']), float(row['long']))

    return data_dict

# Чтение и преобразование к структурному массиву numpy [it, id, node, lat, long]
def read_csv_to_strct(file_path):
    dtype = [('it', '<i4'), ('id', 'i8'), ('node', 'i8'), ('lat', float), ('long', float)]
    data_list = []

    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for i, row in enumerate(reader):
            data_list.append((i, row['id'], 0, float(row['lat']), float(row['long'])))

    data_array = np.array(data_list, dtype=dtype)

    return data_array

# Сопоставлении ключей и переупорядочивания строк в DataFrame
def reorder_csv(input_csv, output_csv, keys, type='strct'):
    df = pd.read_csv(input_csv)
    if type == 'dict':
        df['id'] = df['id'].astype(str)
    df_selected = df[df['id'].isin(keys)]
    df_reordered = df_selected.set_index('id').loc[keys].reset_index()
    df_reordered.to_csv(output_csv, index=False)

if __name__ == "__main__":
    d = read_csv_to_strct('public/example_routes/10_ex_1.csv')
    print(d['lat'])