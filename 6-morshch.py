arr = [1, 3, 5, 9, 11, 0, 12, 1, 12, 21, 22, 16, 17]

print("Масив 13 елементів:")
formatted_arr = [f"\033[34m*{arr[0]}\033[0m"] + [str(x) for x in arr[1:]]
print(" ".join(formatted_arr))

try:
    k = int(input("Введіть ціле число k: "))
except ValueError:
    print("Помилка: введіть ціле число.")
    exit()

if k <= 0:
    print("За умовою k повинно бути > 0")
    exit()

shift = k % 13

print(f"Зсув вправо на {shift} елементи(ів)")

if shift > 0:
    shifted_arr = formatted_arr[-shift:] + formatted_arr[:-shift]
else:
    shifted_arr = formatted_arr

print(" ".join(shifted_arr))

