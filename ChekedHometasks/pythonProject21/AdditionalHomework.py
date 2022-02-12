class Kingdom:
    """Класс царство описывает царство из которого происходит животное"""
    def description(self):
        """Информация о царстве"""
        print("Animals")


class Group(Kingdom):
    """Класс отряд наследуется от класса царство уменьшая выборку до парнокопытных"""
    def description(self):
        """Переопределение метода, добавление информации  об отряде"""
        super().description()
        print("Artiodactyls")


class Kind(Group):
    """Класс вид наследуется от класса группа, который в свою очередь уже содержит в себе информацию от царства
    уменьшая выборку до свиней"""

    def description(self):
        """Переопределение метода, добавление информации  о виде"""
        super().description()
        print("Pigs")


class Pig(Kind):
    """Обращение к конкретной свинке, от которой мы создаем экзепляры, которая будет содержать информацию
     о царстве, отряде и виде"""
    def pepa(self):
        print("Pepa pig")


pepa_pig = Pig()
pepa_pig.description()
pepa_pig.pepa()
