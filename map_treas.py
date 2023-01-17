row1 = ["◻", "◻", "◻"]
row2 = ["◻", "◻", "◻"]
row3 = ["◻", "◻", "◻"]
map = [row1, row2, row3]
game_field = f"    1    2    3\n1 {map[0]}\n2 {map[1]}\n3 {map[2]}"
print(game_field)
position = input("Где сокровище?(первая цифра - строка, вторая - столбец)")

if position == '11':
    map[0][0] = 'x'
elif position == '12':
    map[0][1] = 'x'
elif position == '13':
    map[0][2] = 'x'
elif position == '21':
    map[1][0] = 'x'
elif position == '22':
    map[1][1] = 'x'
elif position == '23':
    map[1][2] = 'x'
    print('      YOU WIN')
elif position == '31':
    map[2][0] = 'x'
elif position == '32':
    map[2][1] = 'x'
elif position == '33':
    map[2][2] = 'x'

new_game_field = f"    1    2    3\n1 {map[0]}\n2 {map[1]}\n3 {map[2]}"
print(new_game_field)