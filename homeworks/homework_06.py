import time

# --- ЗАДАНИЕ 1 ---

class User:
    def __init__(self, name, role):
        self.name = name
        self.role = role

def is_admin(func):
    def wrapper(user):
                               # Проверяем, админ ли это
        if user.role == "admin":
            return func(user)
        else:
            print("У вас нет доступа")
    return wrapper

@is_admin
def delete_video(user):
    print("Видео удалено")

                            # Проверка задания 1
admin = User("Timur", "admin")
user1 = User("Ali", "user")

delete_video(admin)
delete_video(user1)

print("." * 20)

# --- ЗАДАНИЕ 2 ---

def timer(func):
    def wrapper():
        start_time = time.time() # Время до запуска
        func()
        end_time = time.time()   # Время после завершения
        res = end_time - start_time
        print(f"Время выполнения: {round(res, 1)} секунд")
    return wrapper

@timer
def download_video():
    time.sleep(2)
    print("Видео загружено")
                                # Проверка задания 2
download_video()
