 # * author : Philippe Vo 
 # * date : Aug-22-2020 15:33:52
 
# * Imports
import enum
# 3rd Party Imports
# User Imports

# * Code
class DishCategories(enum.Enum):
    Breakfast = "breakfast"
    Lunch = "lunch"
    Dinner = "dinner"
    Snacks = "snacks"

class Healthiness(enum.Enum):
    Fatenning = "fatenning"
    Neutral = "neutral"
    Healthy = "healthy"

class DishModes(enum.Enum):
    Editable = "editable"
    Show = "show"

class SizeType(enum.Enum):
    Unit = "unit"
    Per100g = "per100g"
