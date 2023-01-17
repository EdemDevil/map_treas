row1 = ["◻", "◻", "◻"]
row2 = ["◻", "◻", "◻"]
row3 = ["◻", "◻", "◻"]
map = [row1, row2, row3]
game_field = f"    1    2    3\n1 {map[0]}\n2 {map[1]}\n3 {map[2]}"
print(game_field)

position = input("Where treasure?(first number - string, second - column)")

horizontal = int(position[0])
vertical = int(position[1])

selected_string = map[horizontal - 1]
selected_column = selected_string[vertical - 1] = 'X'

new_game_field = f"    1    2    3\n1 {map[0]}\n2 {map[1]}\n3 {map[2]}"
print(new_game_field)

if position == '23':
    print("      YOU WIN")
else:
    print("     GAME OVER")
