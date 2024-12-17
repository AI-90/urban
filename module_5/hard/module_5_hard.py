from time import sleep

class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

    def __str__(self):
        return self.nickname

class Video:
    def __init__(self, title, duration, time_now = 0, adult_mode = False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

    def __str__(self):
        return self.title

class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self,nickname,password):
        h_password = hash(password)
        for user in self.users :
            if user.nickname == nickname and user.password == h_password:
                self.current_user = user
                return

    def register(self, nickname, password, age):
        for user in self.users:
            if user.nickname == nickname:
                print(f"Пользователь {nickname} уже существует")
                self.log_in(nickname,password)
                return
        user = User(nickname, password, age)
        self.users.append(user)
        self.log_in(nickname, password)

    def log_out(self):
        self.current_user = None

    def add(self, *new_videos:Video):
        for new_video in new_videos:
            add_vidio = True
            for old_video in self.videos:
                if old_video.title == new_video.title:
                    add_vidio = False
                    break
            if add_vidio:
                self.videos.append(new_video)

    def get_videos(self,word):
        list_title_videos = []
        up_word = word.upper()
        for video in self.videos:
            if up_word in video.title.upper():
                list_title_videos.append(video.title)
        return list_title_videos

    def watch_video(self, title):
        if self.current_user:
            up_title = title.upper()
            for video in self.videos:
                if video.title.upper() == up_title:
                    if self.current_user.age >= 18:
                        for second in range(video.time_now, video.duration):
                            sleep(1)
                            print(second+1)
                        video.time_now = 0
                        print("Конец видео")
                        break
                    else:
                        print("Вам нет 18 лет, пожалуйста покиньте страницу")
                        break
            print()
        else:
            print("Войдите в аккаунт, чтобы смотреть видео")

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