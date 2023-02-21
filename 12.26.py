def prepare(f, export_list = []):
    lines = f.readlines()
    for line in lines:
        export_list.append(line.split())
    return export_list

def export(export_list, amount = 0, countries = []):
    product = input('Ввести назву товару: ')
    for list in export_list:
        if product.title() in list:
            countries.append(list[1])
            amount += int(list[2])
    if amount == 0:
        print('Товар не знайдено')
        export(export_list)
    else:
        product_info = {'countries': countries, 'amount': amount}
        print(product_info)

f = open("hw/12.26.txt")
export_list = prepare(f)
export(export_list)