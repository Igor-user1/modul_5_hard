class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = password
        self.age = age


class Video:
    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode


class UrTube:
    users = []
    videos = []
    current_user = None

    def log_in(self, nickname, password):
        password = hash(password)
        for i in range(len(self.users)):
            if nickname in self.users[i]:
                if password in self.users[i]:
                    self.current_user = nickname
                    return self.current_user

    def register(self, nickname, password, age):
        password = hash(password)
        for i in self.users:
            if nickname in i:
                return print(f'Пользователь {nickname} уже существует')
        else:
            self.users.append((nickname, password, age))
            self.current_user = nickname
            return self

    def log_out(self):
        self.current_user = None
        return self

    def add(self, *args):
        for j in args:
            if isinstance(j, Video):
                if j not in self.videos:
                    self.videos.append(j)
        return self.videos

    def get_videos(self, search_word):
        list_1 = []
        for i in self.videos:
            if str(search_word).lower() in str(i.title).lower():
                list_1.append(i.title)
        return list_1

    def watch_video(self, name_of_film):
        if self.current_user is not None:
            for i in self.videos:
                if name_of_film == i.title:
                    for j in self.users:
                        if self.current_user in j:
                            if i.adult_mode is True and j[2] >= 18:
                                for k in range(i.duration):
                                    k += 1
                                    print(k, end=" ")
                                print('Конец видео')
                            else:
                                return print('Вам нет 18, пожалуйста покиньте страницу')
                i.time_now = 0
        else:
            return print('Войдите в аккаунт чтобы смотреть видео')


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

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
