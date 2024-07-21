print('В команде Мастера кода участников: %(team1_num)s ! ' % {'team1_num': 5})
print('Итого сегодня в командах участников: %(team1_num)s и %(team2_num)s !' % {'team1_num': 5, 'team2_num': 6})

print('Команда Волшебники данных решила задач: {score_2} !'.format(score_2='42'))
print('Волшебники данных решили задачи за {team1_time} с !'.format(team1_time='18015.2'))

score_1 = 40
score_2 = 42
team1_time = 1552.512
team2_time = 2153.31451
tasks_total = 82
time_avg = round((team1_time + team2_time) / tasks_total, 2)

print(f'Команды решили {score_1} и {score_2} задач.')

if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
    challenge_result = 'Победа команды Мастера кода!'
elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
    challenge_result = 'Победа команды Волшебники Данных!'
else:
    challenge_result = 'Ничья!'
print(f'{challenge_result}')

print(f'Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!')

