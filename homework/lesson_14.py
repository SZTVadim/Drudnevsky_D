# 1. Создайте функцию calculate_total(price, tax_percent):

# 2. Создайте функцию get_level(points):


def calculate_total(price, tax_price):

    if tax_price >= 20 or price <= 0:
        return "Error"

    else:
        return price, (price * (float(tax_price) / 100))


# 2. Создайте функцию get_level(points):


def get_level(point):

    if point >= 100:
        return "Эксперт"
    elif point >= 50:
        return "Продвинутый"
    elif point >= 20:
        return "Начинающий"
    else:
        return "Новичок"


# ЗАДАНИЕ 2: Функции с условиями и match/case

# 1. Создайте функцию process_status(status) с match/case:


def process_status(status):

    match status:
        case "active":
            return "Статус активен"
        case "inactive":
            return "Статус не активен"
        case "pending":
            return "Статус в ожидании"
        case "blocked":
            return "Статус заблокирован"
        case _:
            return "Неизвестный статус"
