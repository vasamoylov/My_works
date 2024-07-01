import time
class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = password
        self.age = age

class Video:
    def __init__(self, title, duration):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = False

class UrTube:
    def __init__(self):
        self.users = {}
        self.videos = []
        self.current_user = None

    def register(self, nickname, password, age):
        if self.users.get(nickname):
            print('Пользователь ', nickname, ' уже существует')
        else:
            p = hash(password)
            self.users[nickname] = [p, age]
            self.current_user = nickname
    def log_in(self, login, password):
        if self.users.get(login):
            p = hash(password)
            if p == self.users[login][0]:
                self.current_user = login
                print(self.current_user)
    def log_out(self):
        self.current_user = None
    def add(self,name):
        if name.title not in self.videos:
            self.videos.append(name.title)

    def get_videos(self, search):
        search_videos = []
        for i in self.videos:
            if str(search).lower() in str(i).lower():
                search_videos.append(i)
        print(search_videos)
    def watch_video(self, title_video):
        from time import sleep
        if self.current_user != None:
            if self.users[self.current_user][1] >= 18:
                for j in self.videos:
                    if j == title_video:
                        for i in range(1, 11):
                            print(i, end=' ')
                            sleep(1)
                        print('Конец видео')
            else:
                print('Вам нет 18 лет, пожалуйста покиньте страницу')
        else:
            print('Войдите в аккаунт, чтобы смотреть видео')

ur = UrTube()

v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10)
# Добавление видео
ur.add(v1)
ur.add(v2)
# Проверка поиска
ur.get_videos('лучший')
ur.get_videos('ПРОГ')
# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')
# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)
# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')