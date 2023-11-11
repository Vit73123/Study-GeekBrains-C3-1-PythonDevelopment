from sem_package.date_validation import is_date_valid
from sem_package.guess_num_game import guess_num_game
from sem_package.enigma_game import show_results, enigma_game

print(is_date_valid('29.02.2024'))
print(is_date_valid('22.04.1999'))
print(guess_num_game(1, 10, 3))
enigma_game('Висит груша нельзя скушать', {'лампочка'}, 3)
enigma_game('Чем больше убираешь, тем больше становится', {'яма'}, 3)
enigma_game('Зимой и летом одним цветом', {'ель', 'ёлка', 'сосна'}, 3)
show_results()