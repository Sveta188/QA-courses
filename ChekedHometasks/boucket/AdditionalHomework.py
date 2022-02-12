# 1. Определить иерархию и создать несколько цветов.
# Собрать букет (можно использовать аксессуары) с определением его стоимости.
# 2. Определить время его увядания по среднему времени жизни всех цветов в букете.
# 3. Позволить сортировку цветов в букете на основе различных параметров (свежесть/цвет/длина стебля/стоимость...)
# 4. Реализовать поиск цветов в букете по определенным параметрам.
# 5. Узнать, есть ли цветок в букете.

class Flower:
    def __init__(self, name=None, color=None, stem_length=None, freshness=None, lifetime=None, price=None,
                 amounts_of_flowers=None):
        self.name = name
        self.color = color
        self.stem_length = stem_length
        self.fresheness = freshness
        self.lifetime = lifetime
        self.price = price
        self.amounts_of_flowers = amounts_of_flowers


class Rose(Flower):
    def __init__(self, *args):
        super().__init__(*args)

    def __repr__(self):
        return f"This {self.fresheness} {self.color} {self.name} has the length of the stem " \
               f"about {self.stem_length} cm.\n" \
               f"Lifetime of this flower is {self.lifetime} days.\n" \
               f"The price for {self.amounts_of_flowers} flower is {self.price} rubles."


class Iris(Flower):
    def __init__(self, *args):
        super().__init__(*args)

    def __repr__(self):
        return f"This {self.color} {self.name} that was cut {self.fresheness} has length of the stem " \
               f"about {self.stem_length} cm.\n" \
               f"Lifetime of this flower is {self.lifetime} days.\n" \
               f"The price for {self.amounts_of_flowers} flower is {self.price} rubles."


class Herbera(Flower):
    def __init__(self, *args):
        super().__init__(*args)

    def __repr__(self):
        return f"This {self.fresheness} {self.color} {self.name} has the length of the stem " \
               f"about {self.stem_length} cm.\n" \
               f"Lifetime of this flower is {self.lifetime} days.\n" \
               f"The price for {self.amounts_of_flowers} flower is {self.price} rubles."


class Chrysanthemum(Flower):
    def __init__(self, *args):
        super().__init__(*args)

    def __repr__(self):
        return f"This {self.fresheness} {self.color} {self.name} has the length of the stem " \
               f"about {self.stem_length} cm.\n" \
               f"Lifetime of this flower is {self.lifetime} days.\n" \
               f"The price for {self.amounts_of_flowers} flower is {self.price} rubles."


class Alstroemeria(Flower):
    def __init__(self, *args):
        super().__init__(*args)

    def __repr__(self):
        return f"This {self.fresheness} {self.color} {self.name} has the length of the stem " \
               f"about {self.stem_length} cm.\n" \
               f"Lifetime of this flower is {self.lifetime} days.\n" \
               f"The price for {self.amounts_of_flowers} flower is {self.price} rubles."


class Eustoma(Flower):
    def __init__(self, *args):
        super().__init__(*args)

    def __repr__(self):
        return f"This {self.fresheness} {self.color} {self.name} has the length of the stem " \
               f"about {self.stem_length} cm.\n" \
               f"Lifetime of this flower is {self.lifetime} days.\n" \
               f"The price for {self.amounts_of_flowers} flower is {self.price} rubles."


class Bouquet:
    def __init__(self, flowers):
        self.flowers = flowers


    def lifetime_of_bouquet(self):
        """several lifetime of the bouquet"""
        several_laifetime = 0
        for i in self.flowers:
            several_laifetime = (several_laifetime + i.lifetime) / len(self.flowers)
        return f"The several lifetime of this bouquet is {several_laifetime} days"


    def price_of_bouquet(self):
        """price of the bouquet"""
        total_price = 0
        for i in self.flowers:
            total_price = (total_price + i.price)
        return f"The price of this bouquet is {total_price} rubles"


    def bubble_sort_by_price(self):
        swapped = True
        while swapped:
            swapped = False
            for i in range(len(self.flowers) - 1):
                if self.flowers[i].price > self.flowers[i + 1].price:
                    self.flowers[i].price, self.flowers[i + 1].price = self.flowers[i + 1].price, self.flowers[i].price
                    swapped = True


    def selection_sort_by_stem_length(self):
        for i in range(len(self.flowers)):
            lowest_value_index = i
            for j in range(i + 1, len(self.flowers)):
                if self.flowers[j].stem_length < self.flowers[lowest_value_index].stem_length:
                    lowest_value_index = j
                self.flowers[i].stem_length, self.flowers[lowest_value_index].stem_length = self.flowers[lowest_value_index].stem_length, self.flowers[i].stem_length
        return self.flowers


    def search_by_lifetime(self, life_time):
        filtered_flowers = filter(lambda x: x.lifetime == life_time, self.flowers)
        for flower in self.flowers:
            print(flower)


    def if_flower_in_bouqet(self, flower):
        if flower in self.flowers:
            return f"The flower {flower.name} is in bouquet"
        return f"The flower {flower.name} is not in bouquet"








if __name__ == "__main__":
    rose = Rose('rose', 'red', 60, 'freshly cut', 30, 7, 1)  # Flower
    iris = Iris('iris', 'blue', 80, 'week ago', 10, 4, 1)  # Flower
    herbera = Herbera('herbera', 'yellow', 40, 'freshly cut', 20, 5, 1)  # Flower
    chrysanthemum = Chrysanthemum('chrysanthemum', 'white', 50, 'week ago', 15, 6, 1)  # Flower
    alstroemeria = Alstroemeria('alstroemeria', 'purple', 30, 'freshly cut', 21, 4, 1)  # Flower
    eustoma = Eustoma('eustoma', 'purple', 40, 'freshly cut', 45, 5, 1)  # Flower

    my_darling = Bouquet([rose, herbera, eustoma])  # Bouquet
    middle_summer = Bouquet([herbera, eustoma, chrysanthemum, alstroemeria])  # Bouquet
    only_for_you = Bouquet([iris, rose, alstroemeria])  # Bouquet

    # print(rose)
    # print(iris)
    # print(herbera)
    # print(chrysanthemum)
    # print(alstroemeria)
    # print(eustoma)
    # print(mydarling)

    several_lifetime = my_darling.lifetime_of_bouquet()  # several lifetime of the bouquet
    print(several_lifetime)

    several_lifetime = middle_summer.lifetime_of_bouquet()  # several lifetime of the bouquet
    print(several_lifetime)

    several_lifetime = only_for_you.lifetime_of_bouquet()  # several lifetime of the bouquet
    print(several_lifetime)

    total_price = my_darling.price_of_bouquet()  # price of the bouquet
    print(total_price)

    total_price = middle_summer.price_of_bouquet()  # price of the bouquet
    print(total_price)

    total_price = only_for_you.price_of_bouquet()  # price of the bouquet
    print(total_price)

    selection_sort_stem_length = middle_summer.selection_sort_by_stem_length()
    print(selection_sort_stem_length)

    bubble_sort_price = only_for_you.bubble_sort_by_price()
    print(bubble_sort_price)

    print(middle_summer.search_by_lifetime(30))

    print(middle_summer.if_flower_in_bouqet(rose))