# Напишите функцию get_file_info, которая принимает на вход строку - абсолютный путь до файла.
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.
#
# Пример использования.
# На входе:
#
# file_path = "C:/Users/User/Documents/example.txt"
#
# На выходе:
#
# ('C:/Users/User/Documents/', 'example', '.txt')

def get_file_info(file_path: str) -> ():
    '''
    Принимает строку - абсолютный путь до файла.
    Возвращает кортеж из трёх элементов: путь, имя файла, расширение файла

    :param path:
    :return:
    '''

    # split('el')[-1] - Получение с помощью среза последнего элемента из разделённых split()
    file_name = file_path.split("/")[-1]
    file_extension = file_name.split(".")[-1]

    # [: -len(file_name)] - Получение с помощью среза всей части строки до последнего элемента из разделённых split()
    path = file_path[:-len(file_name)]
    return (path, file_name[:-len(file_extension) - 1], "." + file_extension)

# file_path = "C:/Users/User/Documents/example.txt"
# ('C:/Users/User/Documents/', 'example', '.txt')
file_path = "C:/Users/User/Documents/example.txt"
print(get_file_info(file_path))

# file_path =  '/home/user/data/file'
# ('/home/user/data/', '', '.file')
file_path = '/home/user/data/file'
print(get_file_info(file_path))

# file_path = 'D:/myfile.txt'
# ('D:/', 'myfile', '.txt')
file_path = 'D:/myfile.txt'
print(get_file_info(file_path))

# file_path = 'C:/Projects/project1/code/script.py'
# ('C:/Projects/project1/code/', 'script', '.py')
file_path = 'C:/Projects/project1/code/script.py'
print(get_file_info(file_path))

# file_path = '/home/user/docs/my.file.with.dots.txt'
# ('/home/user/docs/', 'my.file.with.dots', '.txt')
file_path = '/home/user/docs/my.file.with.dots.txt'
print(get_file_info(file_path))

# file_path = 'file_in_current_directory.txt'
# ('', 'file_in_current_directory', '.txt')
file_path = 'file_in_current_directory.txt'
print(get_file_info(file_path))
