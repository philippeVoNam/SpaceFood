import yaml

description = "awesome description of the dish"
ingredients = []

lobster = {
    'ingredient': 'lobster',
    'quantity': 1
}

steak = {
    'ingredient': 'steak',
    'quantity': 1
}

ingredients.append(lobster)
ingredients.append(steak)

dish = {
    'description': description,
    'ingredients': ingredients
}

print(yaml.dump(dish))
