from time import sleep

class User: # nickname, password, age
    def __init__(self,nickname,password,age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age
    def __str__(self):
        s = f'{self.nickname}, {self.age}'
        return s

class Video: # title, duration, time_now, adult_mode
    def __init__(self,title,duration,adult_mode = False):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode
    def __str__(self):
        s = f'Видео; {self.title}, длительнсть {self.duration} секунд'
        return s

class UrTube: # users, videos, current_uses
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self,login_,password):
       # print(login_)
       # print(hash(password))
        for user in self.users:
            if login_ == user.nickname and hash(password) == user.password:
                self.current_user = login_
                print(f'{login_} - залогинился')
                break
            else:
                print('Неверный пароль')

    def register(self,nickname,password,age):
        user = User(nickname,password,age)
        if user in self.users:
            self.log_in(nickname,password)
        else:
            print('Регистрация')
            print(user)
            self.users.append(user)
            self.current_user = nickname

    def log_out(self):
        print(f'{self.current_user} - вышел')
        self.current_user = None

    def add(self,*args):
        for arg_ in args:
            self.videos.append(arg_)
            print(arg_)

    def get_videos(self,str_): # поиск Video по слову
        list_f = []
        for video in self.videos:
            if str_.lower() in video.title.lower():
                list_f.append(video.title)
        return list_f

    def watch_video(self,str_):
        if self.current_user == None:
            print('Войдите в аккаунт, чтобы смотреть видео')
        else:
            t=0
            age = 18
            adult = False
            bool_ = False
            for video in self.videos:
                if str_ == video.title:
                    t = video.duration
                    adult = video.adult_mode
                    bool_ = True
                    break
            for user in self.users:
                if user.nickname == self.current_user:
                    age = user.age
            if age < 18 and adult:
                bool_ = False
                print('Вам нет 18 лет, пожалуйста покиньте страницу')
            if bool_:
                for i in range(1,t+1):
                    print(i,end=' ')
                    sleep(1)
                print('Конец видео')

if __name__ == '__main__':
    ur = UrTube();
#    ur.register('Vasay','123',23)
#    print(ur.users)
#    print(ur.current_user)
#    ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
#    print(ur.current_user)
#    ur.register('vasya_pupkin', 'lolkekcheburek', 13)
#    print(ur.current_user)
#    print(ur.users,'\n\n')
#    ur.log_in('urban_pythonist', 'iScX4vIJClb9YQavjAgF')
#print('\n',ur.current_user)

    print('# Добавление видео')
    v1 = Video('Лучший язык программирования 2024 года', 200)
    v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)
    v3 = Video('Когда кодить проще пареной репой?', 33)
    ur.add(v1, v2, v3)

    print('\n# Проверка поиска')
    print(ur.get_videos('лучший'))
    print(ur.get_videos('ПРОГ'))
    print(ur.get_videos('пАр'))


    print('\n #Проверка на вход пользователя и возрастное ограничение')
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('vasya_pupkin', 'lolkekcheburek', 13)
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
    ur.watch_video('Для чего девушкам парень программист?')

    print('\n # Проверка входа в другой аккаунт')
    ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
    print(ur.current_user)

    print('\nПопытка воспроизведения несуществующего видео')
    ur.watch_video('Лучший язык программирования 2024 года!')
