import numpy as np

count = 0  # счетчик попыток
number = np.random.randint(1, 101)  # загадали число
print("Загадано число от 1 до 100")


def game_core_v2(number):
    '''Уменьшаем или увеличиваем число в зависимости от того, больше оно или меньше нужного.
       Число меняется на среднее арифметическое значение между нашим числом и нужным'''
    count = 1
    predict = np.random.randint(1, 101)  # эмулятор введенного числа без человека
    while number != predict:
        count+=1
        lower_bound = 0
        upper_bound = 100
        if number > predict:
            print(f"Угадываемое число больше {predict} ")
            lower_bound = predict
            predict = (lower_bound+upper_bound)//2
        elif number < predict:
            print(f"Угадываемое число меньше {predict} ")
            upper_bound = predict
            predict = (lower_bound+upper_bound)//2
    print(f"Вы угадали число {number} за {count} попыток.") # выход из цикла, если угадали

def score_game(game_core_v2):
    '''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы эксперимент был воспроизводим!
    random_array = np.random.randint(1,101, size=(1000))
    for number in random_array:
        count_ls.append(game_core_v2(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return(score)

# Проверяем
score_game(game_core_v2)