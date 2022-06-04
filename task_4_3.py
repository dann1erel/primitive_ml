from task_1 import *


def reinforcement():
    board = [[2, -3],
             [-1, 2]]
    a_win_result = 0
    a_win_result_m = [0] * 100
    move = [0] * 100
    sum = 0
    a_balls = [0] * 10 + [1] * 10
    b_balls = [0] * 10 + [1] * 10
    for i in range(100):
        a_move = random.choice(a_balls)
        b_move = random.choice(b_balls)
        move[i] = [a_move, b_move]
        a_win_result_m[i] = board[a_move][b_move]
        a_win_result += board[a_move][b_move]
        if board[a_move][b_move] > 0:
            for i in range(2):
                a_balls.append(a_move)
        else:
            for i in range(abs(board[a_move][b_move])):
                b_balls.append(b_move)
    p1 = a_balls.count(0) / len(a_balls)
    p2 = b_balls.count(0) / len(b_balls)
    a_result_avg = a_win_result / 100
    mat_waiting = 2 * p1 * p2 - 3 * p1 * (1 - p2) - 1 * (1 - p1) * p2 + 2 * (1 - p1) * (1 - p2)
    for i in range(100):
        sum += (a_win_result_m[i] - a_result_avg) ** 2
    sko = (sum / 99) ** 0.5
    disp = p1 * p2 * (2 - mat_waiting) ** 2 + \
           p1 * (1 - p2) * (-3 - mat_waiting) ** 2 + \
           (1 - p1) * p2 * (-1 - mat_waiting) ** 2 + \
           (1 - p1) * (1 - p2) * (2 - mat_waiting) ** 2
    tsko = disp ** 0.5
    print("Вероятность игрока А:", p1)
    print("Вероятность игрока В:", p2)
    print("Среднее значение выигрыша/проигрыша игрока А:", a_result_avg)
    print("Математическое ожидание игрока A:", mat_waiting)
    print("Среднее квадратичное отклонение от экспериментального среднего:", sko)
    print("Дисперсия:", disp)
    print("Теоретическое среднее квадратичное отклонение для данных вероятностей", tsko)


reinforcement()