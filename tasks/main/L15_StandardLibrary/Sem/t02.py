# 📌 На семинаре про декораторы был создан логирующий декоратор. Он сохранял аргументы функции и результат её
# работы в файл.
# 📌 Напишите аналогичный декоратор, но внутри используйте модуль logging.
import logging

logging.basicConfig(filename=f"task2.log",
                    filemode="a",
                    level=logging.DEBUG)


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
