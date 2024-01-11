import time
import os
from datetime import datetime


def main():
    datetime_now = datetime.now()
    memory_response = os.popen("free").read()
    print(f"\nПоказатели памяти на {datetime_now} такие."
          "\nТвоё дело распарсить ответ и сохранить"
          " показатели в файл | БД | др.\n")
    print(memory_response)


if __name__ == "__main__":
    print("Для остановки скрипта нажми Ctrl + C")
    while True:
        try:
            time.sleep(1)
            main()
        except KeyboardInterrupt:
            print("\nТы завершил работу скрпта. Ай ай ай.")
            break
