import time
import os
from datetime import datetime


def get_datetime_now():
    """
    Вернуть текущие дату и время.
    TODO: вернуть в нужном формате.
    """
    datetime_now = datetime.now()
    return datetime_now


def get_memory():
    """
    Вернуть ответ команды free.
    TODO: распарсить ответ.
    """
    memory_response = os.popen("free").read()
    return memory_response


def get_host():
    """
    Вернуть hostname тачки.
    """
    host = os.uname()[1]
    return host


def get_output_response(host, datetime_now, memory_response):
    """
    Вернуть ответ скрипта. Куда писать ответ, напишешь сам далее.
    """
    response = str(datetime_now) + "\n"
    response += f"Показатели памяти {host}:\n"
    response += memory_response + "\n"
    response += "Твоё дело распарсить ответ и сохранить"
    response += " показатели в файл | БД | др.\n"
    return response


def main():
    """
    Вызов методов и вывод ответа программы.
    """
    datetime_now = get_datetime_now()
    memory = get_memory()
    host = get_host()
    output_response = get_output_response(host, datetime_now, memory)
    print(output_response)


if __name__ == "__main__":
    print("Для остановки скрипта нажми Ctrl + C")
    while True:
        try:
            time.sleep(1)
            main()
        except KeyboardInterrupt:
            print("\nТы завершил работу скрпта. Ай ай ай.")
            break
