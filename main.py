from pprint import pprint

with open('recipes.txt', 'rt', encoding='utf-8') as file:
    cookbook = {}
    for line in file:
        dish_name = line.strip()
        ingredients_count = int(file.readline().strip())
        recipe = []
        for _ in range(ingredients_count):
            ingredient_name, quantity, measure = file.readline().strip().split('|')
            recipe.append({
                'ingredient_name': ingredient_name,
                'quantity': int(quantity),
                'measure':  measure

            })
        file.readline()
        cookbook[dish_name] = recipe




def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
        for ingredient in cookbook[dish]:
            new_shop_list_item = dict(ingredient)
            new_shop_list_item['quantity'] *= person_count
            if new_shop_list_item['ingredient_name'] not in shop_list:
                shop_list[new_shop_list_item['ingredient_name']] = new_shop_list_item
            else:
                shop_list[new_shop_list_item['ingredient_name']]['quantity'] +=\
                new_shop_list_item['quantity']
    return shop_list

print(get_shop_list_by_dishes(['Омлет'], 3))










