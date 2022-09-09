# блоки try, except, finally, else
# ловля исключения
# ловля нескольких исключений на выбор
# написание собственного класса исключений
import requests

print("Открытие соединения с базой")  # открытие транзакции, тратим оперативную память, занимаем сокет,


# заставляем базу делать вычисления


class MyException(Exception):
    def __init__(self, message: str):
        self.message = message
    # def __new__(cls, *args, **kwargs): # - cls - ссылка на класс
    # super()

    def get_error_message(self) -> str:
        return f"состояние: {self.message}"

    def __str__(self) -> str:
        return self.get_error_message()

try:
    print("Опасные вычисления")
    val1 = 10
    val2 = 0

    # requests.get(timeout=3)

    request = {
        "name": "afaef",
        "headers": {
            "Authorization": "admin admin"
        }
    }

    request2 = {
        "name": "afaef",
        "headers": {
            "Authorization": ""
        }
    }

    Authorization = request2["headers"].get('Authorization', None)
    if Authorization:
        pass
    else:
        raise MyException(message='Неверные заголовки (авторизация)')

    # print(val1 / val2)
except MyException as error:
    print(f"333333333333 Наш код упал! {error}")
else:
    print("ошибки не было!")
finally:
    print("Закрытие соединения с базой")  # высвобождает ресурсы, commit or rollback,

# with open("") as file
# with aiohttp.ClientSession() as session
