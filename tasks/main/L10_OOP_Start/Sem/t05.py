# 📌 Создайте три (или более) отдельных классов животных. Например рыбы, птицы и т.п.
# 📌 У каждого класса должны быть как общие свойства, например имя, так и специфичные для класса.
# 📌 Для каждого класса создайте метод, выводящий информацию специфичную для данного класса.
class Animal:
    def __init__(self, name: str):
        self.name = name


class Mammal(Animal):
    def __init__(self, name: str, weight: float):
        self.weight = weight
        super().__init__(name)

    def category(self) -> str:
        return "Малявка" if self.weight <= 1 else "Обычный" if self.weight <= 200 else "Гигант"


class Bird(Animal):
    def __init__(self, name: str, wing_span: float):
        self.wing_span = wing_span
        super().__init__(name)

    def wing_length(self):
        return self.wing_span / 2


class Fish(Animal):
    def __init__(self, name: str, max_depth: float):
        self.max_depth = max_depth
        super().__init__(name)

    def depth(self):
        return "Мелководная" if self.max_depth <= 1 else "Средневодная" if self.max_depth <= 100 else "Глубоководная"


if __name__ == '__main__':
    mammal1 = Mammal('Mammal1', 1)
    mammal2 = Mammal('Mammal2', 10)
    mammal3 = Mammal('Mammal3', 300)
    fish1 = Fish('Fish1', 1)
    fish2 = Fish('Fish2', 10)
    fish3 = Fish('Fish3', 200)
    bird = Bird('Bird', 0.5)
    print(f'{mammal1.name}\tweight\t= {mammal1.weight}\tcategory\t= {mammal1.category()}')
    print(f'{mammal2.name}\tweight\t= {mammal2.weight}\tcategory\t= {mammal2.category()}')
    print(f'{mammal3.name}\tweight\t= {mammal3.weight}\tcategory\t= {mammal3.category()}')
    print(f'{fish1.name}\tmax_depth\t= {fish1.max_depth}\tdepth\t= {fish1.depth()}')
    print(f'{fish2.name}\tmax_depth\t= {fish2.max_depth}\tdepth\t= {fish2.depth()}')
    print(f'{fish3.name}\tmax_depth\t= {fish3.max_depth}\tdepth\t= {fish3.depth()}')
