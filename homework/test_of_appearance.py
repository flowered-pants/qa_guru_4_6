from datetime import time


def test_dark_theme():
    current_time = time(hour=4)
    if current_time.hour >= 22 or current_time.hour <= 6:
        is_dark_theme = True
    else:
        is_dark_theme = False
    assert is_dark_theme is True

    current_time = time(hour=16)
    dark_theme_enabled = True
    if dark_theme_enabled is True:
        is_dark_theme = True
    elif current_time.hour >= 22 or current_time.hour <= 6:
            is_dark_theme = True
    else:
            is_dark_theme = False

    assert is_dark_theme is True

def test_find_suitable_user():

    users = [
        {"name": "Oleg", "age": 32},
        {"name": "Sergey", "age": 24},
        {"name": "Stanislav", "age": 15},
        {"name": "Olga", "age": 45},
        {"name": "Maria", "age": 18},
    ]

    suitable_user = {}

    for user in users:
        if user["name"] == "Olga":
            suitable_user.update({'name': user['name'], 'age' : user['age']})
    assert suitable_user == {"name": "Olga", "age": 45}

    # TODO найдите всех пользователей младше 20 лет
    suitable_users = []
    for user in users:
        if user["age"] < 20:
            suitable_users.append(user)

    assert suitable_users == [
        {"name": "Stanislav", "age": 15},
        {"name": "Maria", "age": 18},
    ]
print(test_find_suitable_user.__name__)

    # Сделайте функцию, которая будет печатать
    # читаемое имя переданной ей функции и значений аргументов.
    # Вызовите ее внутри функций, описанных ниже
    # Подсказка: Имя функции можно получить с помощью func.__name__
    # Например, вызов следующей функции должен преобразовать имя функции
    # в более читаемый вариант (заменить символ подчеркивания на пробел,
    # сделать буквы заглавными (или первую букву), затем вывести значения всех аргументов этой функции:
    # >>> open_browser(browser_name="Chrome")
    # "Open Browser [Chrome]"


def test_readable_function():
    open_browser(browser_name="Chrome")
    go_to_companyname_homepage(page_url="https://companyname.com")
    find_registration_button_on_login_page(page_url="https://companyname.com/login", button_text="Register")

def correction_name_of_readable_function(func, **kwargs):
    description_of_function = f'{func.__name__.title().replace("_", " ")} [{", ".join(kwargs)}]'
    print(description_of_function)
    return description_of_function

def open_browser(browser_name):
    actual_result = correction_name_of_readable_function(browser_name="Chrome")

def go_to_companyname_homepage(page_url):
    actual_result = correction_name_of_readable_function(page_url= "https://companyname.com")
    assert actual_result == "Go To Companyname Homepage [https://companyname.com]"

def find_registration_button_on_login_page(page_url, button_text):
    actual_result = correction_name_of_readable_function(page_url = "https://companyname.com/login", button_text = "Register")
    assert actual_result == "Find Registration Button On Login Page [https://companyname.com/login, Register]"


