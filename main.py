import csv
import json
import math
import os
import random
from os import listdir
from typing import Callable

def new_csv_file(file_name: str = 'gen_nums'):
    file_name = file_name + '.csv'
    with open(file_name, 'w', encoding='UTF-8') as file_write:
        file_writer = csv.writer(file_write, delimiter=",", lineterminator="\r")
        lines_count = random.randint(1, 10)
        for _ in range(lines_count):
            file_writer.writerow([random.randint(-1000, 1000),
                                 random.randint(-1000, 1000),
                                 random.randint(-1000, 1000)])

new_csv_file()

def decor(func: Callable):

    def wrapper(*args):
        for (path, dirs, files) in os.walk(os.getcwd()):
            for file in files:
                if file.endswith('.csv'):
                    file_name = file
        with (
            open(file_name, 'r', encoding='UTF-8') as file_read,
            open('result.json', 'w', encoding='UTF-8') as file_write
        ):
            res_dict = {}
            file_reader = csv.reader(file_read, delimiter = ",")
            for row in file_reader:
                res = func(int(row[0]), int(row[1]), int(row[2]))
                res_dict[f'{row[0]},{row[1]},{row[2]}'] = res
            json.dump(res_dict, file_write, indent=4, ensure_ascii=False)
    return wrapper

@decor
def root_quadratic_equation(a: int, b: int, c: int):
    d = b**2 - (4 * a * c)
    if d > 0:
        x1 = (-b + math.sqrt(d)) / (2 * a)
        x2 = (-b - math.sqrt(d)) / (2 * a)
        return f'{x1 = }, {x2 = }'
    elif d == 0:
        x1 = -b / (2 * a)
        return f'{x1 = }'
    else:
        return f'нет корней'

root_quadratic_equation(1, 12, 4)