# Завдання 12.21
print('Завдання 12.21')

def dates(filename):
    f = open(filename)
    d = f.readlines()
    d_list = []

    for x in d:
        d_list.append(x.strip().split('.'))
    f.close()
    
    return d_list

def task_a(d_list):
    years = []

    for date in d_list:
        years.append(int(date[2]))
    
    return min(years)
    
def task_b(d_list):
    spring_months = ['03', '04', '05']
    spring_dates = []

    for date in d_list:
        if date[1] in spring_months:
            spring_dates.append(date)
        
    return spring_dates

def task_c(d_list):
    year = max([int(x[2]) for x in d_list])
    d = []

    for date in d_list:
        if int(date[2]) == year:
            d.append(date)
    d_list = d
    if len(d_list) == 1:
        return d_list[0]
    
    month = max([int(x[1]) for x in d_list])
    d = []

    for date in d_list:
        if int(date[1]) == month:
            d.append(date)
    d_list = d
    if len(d_list) == 1:
        return d_list[0]
    
    day = max([int(x[0]) for x in d_list])
    d = []
    for date in d_list:
        if int(date[0]) == day:
            d.append(date)
    return d[0]

filename = 'exercises/12.21.txt'
d_list = dates(filename)

print(f'Найменший рік: {task_a(d_list)}\n')

print('Весняні дати: ')
for x in task_b(d_list):
    print('.'.join(x))

print(f'\nНайпізніша дата: {".".join(task_c(d_list))}')

# Завдання 12.29
print('\nЗавдання 12.29')

def search_rect(filename):
    f = open(filename)
    rects = f.readlines()
    rects_dict = {}
    area_dict = {}

    for rect in rects:
        rects_dict[int(rect.split()[0])] = ((int(rect.split()[3]), int( rect.split()[5])), 
            (int(rect.split()[8]), int(rect.split()[10])))

    for number, coords in rects_dict.items():
        area = abs(coords[0][0] - coords[1][0]) * abs(coords[0][1] - coords[1][1])
        area_dict[number] = area
    f.close()

    area = max(area_dict.values())
    for k, v in area_dict.items():
        if v == area:
            return (k, v)


filename = 'exercises/12.29.txt'
print(f'Прямокутник під номером {search_rect(filename)[0]} має площу {search_rect(filename)[1]}')