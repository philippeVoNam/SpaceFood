import yaml

class Dish:
    def __init__(self):
        self.name = "Philippe"
        self.id = 27759908

dish = Dish()

yaml.dump(dish, "data.yaml")
