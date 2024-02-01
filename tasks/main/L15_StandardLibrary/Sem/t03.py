# 📌 Доработаем задачу 2.
# 📌 Сохраняйте в лог файл раздельно:
# ○ уровень логирования,
# ○ дату события,
# ○ имя функции (не декоратора),
# ○ аргументы вызова,
# ○ результат.
import logging

FORMAT = "%(asctime)s | %(levelname)s | %(message)s"

logging.basicConfig(filename=f"task3.log",
                    filemode="a",
                    level=logging.DEBUG,
                    format=FORMAT)


def logging_deco(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        logging.debug(f"Аргументы: {args} | {kwargs} | "
                      f"Результат: {result} | "
                      f"Функция: {func.__name__}")
        return result

    return wrapper


@logging_deco
def some_func(a: [int, float], b: [int, float]) -> [None, float]:
    try:
        return a / b
    except ZeroDivisionError as e:
        return None


if __name__ == "__main__":
    for i in range(0, 10):
        for j in range(0, 10):
            some_func(i, j)
