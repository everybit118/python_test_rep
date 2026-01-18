def greet(name):
    return f"Привет, {name}! Добро пожаловать в мой репозиторий."

if __name__ == "__main__":
    user_name = input("Введите ваше имя: ")
    print(greet(user_name))