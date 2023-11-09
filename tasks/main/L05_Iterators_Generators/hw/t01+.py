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

    *path, name = file_path.split('/')
    if len(path) > 0:
        path = '/'.join(path) + '/'
    else:
        path = ''

    *name, ext = name.split('.')
    if len(name) > 0:
        name = '.'.join(name)
    else:
        name = ''
    ext = '.' + ext
    return path, name, ext


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
