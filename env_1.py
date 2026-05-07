import os

surname = os.environ.get("STUDENT_SURNAME")

if surname:
    print(f"\033[34m Значення змінної знайдено: {surname} \033[0m")
else:
    print("\033[31m Помилка: Змінна відсутня. \033[0m")
