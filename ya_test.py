from tools.dish_controller import DishController
from elements.dish import Dish
from elements.enums import DishCategories, Healthiness

name = "l-s"
category = DishCategories.Dinner.value
description = "wonderful food"
ingredients = ["lobster", "steak"]
calories = 100
healthiness = Healthiness.Fatenning.value
dishImgPath = "img.jpg"

dish = Dish(name, category, description, ingredients, calories, healthiness, dishImgPath)

dishControl = DishController()

dishControl.create(dish)

dish1 = dishControl.read("data/dishes/dinner/surf-n-turf")

print(dish1)
