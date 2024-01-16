# 📌 Создайте класс Моя Строка, где:
# 📌 будут доступны все возможности str
# 📌 дополнительно хранятся имя автора строки и время создания
# (time.time)
import datetime


class MyStr(str):
    def __new__(cls, value, author):
        instance = super().__new__(cls, value)
        instance.author = author
        instance.time = datetime.datetime.now()
        return instance

    # def __str__(self):
    #     return f'{self.author = } {self.time = }'

if __name__ == '__main__':
    ms1 = MyStr('text', 'Vladislav')
    ms2 = MyStr('new_text', 'Max')
    print(ms1, ms1.author, ms1.time)
    print(ms2, ms2.author, ms2.time)