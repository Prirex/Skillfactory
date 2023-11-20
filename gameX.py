pole_size = 3 #колечество клеток

pole = [1,2,3,4,5,6,7,8,9] #игровое поле

def go():#вывод игрового поля
    print("_" * 4 * pole_size)
    for i in range (pole_size):
        print((" " * 3 + "|")*3)
        print("", pole[i * 3], "|", pole[1 + i *3], "|", pole[2 + i *3], "|")
        print(("_" * 3 + "|")*3)

    pass
def hod(index, char): #выполняем ход
    if (index >= 10 or index < 1 or pole[index - 1] in ("X", "x", "O", "o" "о", "О", "Х", "х")):
        return False

    pole[index - 1] = char
    return True
def check_win(): # проверка на победу
    win = False
    win_c = ((0,1,2), (3,4,5), (6,7,8), (0,4,8), (2,4,6), (0,3,6), (1,4,7), (2,5,8))
    for pos in win_c:
        if (pole[pos[0]] == pole[pos[1]] and pole[pos[1]] == pole[pos[2]]):
            win = pole[pos[0]]

    return win

def start():
    one_player = "X" #текущий игрок
    player = "Крестики"
    player_win = "Нолики"

    step = 1 #номер шага
    go()

    while (step <= 9) and (check_win() == False):
        index =input("\nХодят " + player + "\nВведите номер поля: ")

        if (hod(int(index), one_player)):
            print("Удачный ход!")

            if (one_player == "X"):
                one_player = "O"
                player = "Нолики"
                player_win = "Крестики"

            else:
                one_player = "X"
                player = "Крестики"
                player_win = "Нолики"

            go()
            step += 1
        else:
            print("Неверный номер, повторите!")

    if (step == 10):
        print("Ничья!, такое бывает")
        print("Спасибо за игру")


    else:
        print("С победой, " + player_win + "!\n",player, "не переживай, в следующий раз победа будет за тобой!")
        print("Спасибо за игру")



print("PriRex studio представляет:")
print("      Крестики-нолики")
#Проверяем знания игры и начием игру

rules_a = int(input("\n \n Напомнить правила ? \n" " 1 - дa, 2 -нет \n" "Ввод: "))

if rules_a != 1:
    print("Пора начинать! ")
    start()
else:
    print("Правила:\nИгроки по очереди ставят на свободные клетки поля 3×3 знаки (один всегда крестики, другой всегда нолики).\nПервый, выстроивший в ряд 3 своих фигуры по вертикали, горизонтали или большой диагонали, выигрывает.")
    print("\nПора начинать!")
    start()