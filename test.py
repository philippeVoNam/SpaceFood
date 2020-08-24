from tools.dish_controller import DishController
from elements.enums import DishCategories, Healthiness

name = "surf-n-turf"

category = DishCategories.Dinner.value

description = "awesome"

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

calories = 100

healthiness = Healthiness.Fatenning.value

dishControl = DishController()
dishControl.create(name, category, description, ingredients, calories, healthiness, "img.jpg")
