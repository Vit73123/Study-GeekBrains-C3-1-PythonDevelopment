# Выведите в консоль таблицу умножения от 2х2 до 9х10 как на школьной тетрадке.

for i in [2, 6]:
    for j in range(2, 11):
        for k in range(0, 4):
            print(f'{i + k:>2} x {j:>2} = {(i + k) * j:>2}', end='\t')
        print()
    print()
