
win_kombinations = [[0, 1, 2],
                    [3, 4, 5],
                    [6, 7, 8],
                    [0, 3, 6],
                    [1, 4, 7],
                    [2, 5, 8],
                    [0, 4, 8],
                    [2, 4, 6]]

# функция отображения текущего состояния поля
def showCurrent(*rows):
    print(50*'_')
    print('   0    1    2')
    print(f'0  {rows[0]}    {rows[1]}   {rows[2]}')
    print(f'1  {rows[3]}    {rows[4]}   {rows[5]}')
    print(f'2  {rows[6]}    {rows[7]}   {rows[8]}')


# проверка победила ли данная фигура
def isWin(fig, *rows):
    for komb in win_kombinations:
        if rows[komb[0]]==fig and rows[komb[1]]==fig and rows[komb[2]]==fig:
            return True
    return False





# функция проверяет можно ли выиграть, поставив  ход, в данном ряду
def calcRow(fig, i1, i2, i3, *rows):
    if rows[i1]==fig and rows[i2]==fig and rows[i3]=='-':
        return i3
    elif rows[i1]==fig and rows[i3]==fig and rows[i2]=='-':
        return i2
    elif rows[i2]==fig and rows[i3]==fig and rows[i1]=='-':
        return i1
    else:
        return -1

# Функция ищет комбинации, когда достаточно сделать ход чтоб выиграть
def findStepForWin(fig, *rows):
    for komb in win_kombinations:
        res = calcRow(fig, komb[0], komb[1], komb[2], *rows)
        if res >= 0:
            return res
    return -1



# 0 1 2
# 3 4 5
# 6 7 8




while True:
    print('Выберите тип фигур: ' )
    print('Для выхода из игры нажмите q')
    user_figure = input()
    if user_figure == 'q':
        break
    if user_figure not in ('o', 'x'):
        print('Неверный тип фигур.')
        continue

    rows =list('-' for i in range(0, 9))

    if user_figure == 'o':
        my_figure = 'x'
        rows[4] = 'x'
    else:
        my_figure = 'o'

    game_over = False
    while not game_over:
        # 1. обработка хода пользователя
        showCurrent(*rows)
        print('Ваш ход(введите строку и столбец через пробел): ')
        try:
            row, col = tuple(map(int, input().split(' ')))
            # print(row, col)
            if (0<=row<=2) and (0<=col<=2):
                current_index = col + row * 3
                if rows[current_index] != '-':
                    print('Этот ход не возможен, поле занято')
                    continue
                else:
                    rows[current_index] = user_figure
            else:
                print('Этот ход не возможен, поле вне диапазона')
                continue
        except:
            print('!!! Неправильные строка и столбец поля.')
            continue

        # 2. проверяем не победил ли противник
        if isWin(user_figure, *rows):
            game_over = True
            showCurrent(*rows)
            print('Мои поздравления! Вы победили!')
            continue



        # 3. если противник в шаге от победы, блокируем его ход
        user_index = findStepForWin(user_figure, *rows)
        if user_index >=0:
            rows[user_index] = my_figure

        else:
            # 4. если я в шаге от победы, то побеждаю
            user_index = findStepForWin(my_figure, *rows)
            if user_index >=0:
                rows[user_index] = my_figure
                game_over = True
                showCurrent(*rows)
                print(' Вы проиграли!')
                continue

            else:
            # 5. Если свободна центральная ячейка
                if rows[4] == '-':
                    rows[4] = my_figure
                    showCurrent(*rows)
                    continue

            # 6. Иначе делаем случайный шаг
                user_index = -1
                for i in range(0, 9):
                    if rows[i] == '-':
                        user_index = i
                        break
                if user_index <0:
                    game_over = True
                    showCurrent(*rows)
                    print(' Ничья!')
                    continue
                else:
                    rows[user_index] = my_figure
                    showCurrent(*rows)
