"""Программа-лаунчер"""


import subprocess

process = []

while True:
    action = input('Выберите действие: q - выход , s - запустить сервер и клиенты, x - закрыть все окна:')
    if action == 'q':
        break
    elif action == 's':
        clients_count = int(input('Введите количество тестовых клиентов для запуска: '))
        # Запускаем сервер!
        process.append(subprocess.Popen('python server.py', creationflags=subprocess.CREATE_NEW_CONSOLE))
        # Запускаем клиентов:
        process.extend(
            subprocess.Popen(
                f'python client.py -n test{i + 1}',
                creationflags=subprocess.CREATE_NEW_CONSOLE,
            )
            for i in range(clients_count)
        )

    elif action == 'x':
        while process:
            process.pop().kill()
