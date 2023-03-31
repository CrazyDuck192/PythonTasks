# Завдання 12.23
from collections import defaultdict

def phone_number(filename, name):
    f = open(filename)
    names = f.readlines()
    name = name.split()
    name = f'{name[0].title()} {name[1].title()}.'
    for row in names:
        if f'{row.split()[0]} {row.split()[1]}' == name:
            return name, row.split()[2]
    f.close()

    return 'співробітника не знайдено'

filename = 'exercises/12.23.txt'  
name = input("Введіть ім'я: ")     
print(f'Телефон співробітника {phone_number(filename, name)[0]}: {phone_number(filename, name)[1]}')

# Завдання 12.24

def cubes_by_colours(filename):
    f = open(filename)
    rows = f.readlines()
    colours_dict = defaultdict(int)
    areas_dict = defaultdict(int)
    cubes_dict = defaultdict(tuple)

    for cube in rows:
        colours_dict[cube.split()[1]] += 1
    for cube in rows:
        areas_dict[cube.split()[1]] += int(cube.split()[0])**3
    for colour in areas_dict.keys():
        cubes_dict[colour] = (f'Кількість кубиків: {colours_dict[colour]}',
            f"Сумарний об'єм: {areas_dict[colour]}")
    f.close()

    return cubes_dict

def cubes_by_materials(filename):
    f = open(filename)
    rows = f.readlines()
    wood_cubes = 0
    iron_cubes = 0

    for cube in rows:
        if cube.split()[2] == 'wood' and int(cube.split()[0]) == 3:
            wood_cubes += 1
        if cube.split()[2] == 'iron' and int(cube.split()[0]) > 5:
            iron_cubes += 1

    return wood_cubes, iron_cubes


filename = 'exercises/12.24.txt'
for cube_colour, info in cubes_by_colours(filename).items():
    print(f"{cube_colour}: {info}")

cubes = cubes_by_materials(filename)
print(f"\nКількість дерев'яних кубиків із ребром 3: {cubes[0]}")
print(f"Кількість металевих кубиків із ребром більшим за 5: {cubes[1]}")

        