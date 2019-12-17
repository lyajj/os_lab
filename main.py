import signal
from shell import parse_cmd

def interrupt(*args):
    exit()

def main():
    username = 'user'
    signal.signal(signal.SIGINT, interrupt)

    while True:
        inp = input(f'{username}$ ')
        cmd = parse_cmd(inp)

main()

"""

Запуск:
python3 main.py

Пример использования:

user$ ls
.git __pycache__ main.py shell.py utils.py vim.py
user$ touch file.txt
user$ cat file.txt


user$ vim file.txt
1. 
1. This is vim! 

user$ cat file.txt
This is vim!
user$ rm file.txt
user$ ls
.git __pycache__ main.py shell.py utils.py vim.py
user$

Работа с vim (такие тупые хоткеи, потому что пробломно настроить нормальные с macOS для запуска в Windows :))) ):
Левый Shift – переход к строке сверху
Правый Shift – переход к строке снизу

Левый Alt – ввести заданную строку (предыдущее значение затрется)
Правый Alt – новая строка после текущей и переход на нее

Левый Ctrl – удаление строки
Правый Ctrl – сохранить

"""