"""Программа-лаунчер"""


import subprocess

PROCESSES = []

while True:
    ACTION = input('Выберите действие: q - выход, '
                   's - запустить сервер и клиенты, '
                   'x - закрыть все окна: ')

    if ACTION == 'q':
        break
    elif ACTION == 's':
        PROCESSES.extend(
            (
                subprocess.Popen(
                    'python server.py',
                    creationflags=subprocess.CREATE_NEW_CONSOLE,
                ),
                subprocess.Popen(
                    'python client.py -n test1',
                    creationflags=subprocess.CREATE_NEW_CONSOLE,
                ),
                subprocess.Popen(
                    'python client.py -n test2',
                    creationflags=subprocess.CREATE_NEW_CONSOLE,
                ),
                subprocess.Popen(
                    'python client.py -n test3',
                    creationflags=subprocess.CREATE_NEW_CONSOLE,
                ),
            )
        )

    elif ACTION == 'x':
        while PROCESSES:
            VICTIM = PROCESSES.pop()
            VICTIM.kill()
