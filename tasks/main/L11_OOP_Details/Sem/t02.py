# � Создайте класс Архив, который хранит пару свойств.
# Например, число и строку.
# 📌 При новом экземпляре класса, старые данные из ранее созданных экземпляров сохраняются в пару
# списков-архивов
# 📌 list-архивы также являются свойствами экземпляра

class Archive:
    instance = None

    def __new__(cls, text, number):
        if cls.instance is None:
            cls.instance = super().__new__(cls)
            cls.instance.old_text = []
            cls.instance.old_num = []
        else:
            cls.instance.old_text.append(cls.instance.text)
            cls.instance.old_num.append(cls.instance.number)
        return cls.instance

    def __init__(self, text, number):
        self.text = text
        self.number = number

if __name__ == '__main__':
    a1 = Archive('fakfkaf', 12)
    print(a1.old_text, a1.old_num)
    a2 = Archive('jagnagj', 111)
    print(a2.old_text, a2.old_num)
    print(a1.old_text, a1.old_num)
