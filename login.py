def login(username, password):
    if username == "admin" and password == "12345":
        return "Вход разрешен"
    else:
        return "Ошибка входа"
