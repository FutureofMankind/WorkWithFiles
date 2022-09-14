import os.path
from pprint import pprint


file_name = "CookBook.txt"


def cook_catalog(file_name):
    with open(file_name, encoding="utf-8") as file_obj:
        cook_book = {}
        for line in file_obj:
            dish_name = line.strip()
            cook_book[dish_name] = []
            for item in range(int(file_obj.readline())):
                ingredient = file_obj.readline().split(' | ')
                cook_book[dish_name].append({'ingredient_name': ingredient[0],
                                               'quantity': ingredient[1],
                                               'measure': ingredient[2].strip()})
            file_obj.readline()
        return cook_book


catalog = cook_catalog(file_name)
pprint(catalog)


def list_of_stores_with_ingredients(dishes, person_count, cook_book):
    order = {}
    for dish in dishes:
        if dish in cook_book:
            for ingredient in cook_book[dish]:
                if ingredient['ingredient_name'] in order:
                    order[ingredient['ingredient_name']]['quantity'] += ingredient['quantity'] * person_count
                else:
                    order[ingredient['ingredient_name']] = {'measure': ingredient['measure'],
                                                       'quantity': (ingredient['quantity'] * person_count)}
        else:
            print(f'Dishes {dish} not in the cook book')
    return order


def strings(file):
    with open(file, 'r', encoding="UTF-8") as x:
        return sum(1 for _ in x)


def catalog(writing_file, base_path, location):
    files = []
    for i in list(os.listdir(os.path.join(base_path, location))):
        x = [strings(os.path.join(base_path, location, i)), os.path.join(base_path, location, i), i]
        files.append(x)
    for list_file in sorted(files):
        opening_files = open(writing_file, 'a', encoding="UTF-8")
        opening_files.write(f'{list_file[2]}\n')
        opening_files.write(f'{list_file[0]}\n')
        with open(list_file[1], 'r', encoding="UTF-8") as file:
            check = 1
            for line in file:
                opening_files.write(f'line in № {check} in file {list_file[2]} : {line}')
                check += 1
        opening_files.write(f'\n')
        opening_files.close()
