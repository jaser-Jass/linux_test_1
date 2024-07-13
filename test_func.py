import subprocess

def check_command_output(command, text):
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        if text in result.stdout:
            return True
        else:
            return False
    except subprocess.CalledProcessError:
        return False

# Пример использования функции
command = "ls -l"  # Команда для проверки (в данном случае вывод списка файлов в текущей директории)
text = "example.txt"  # Текст, который необходимо найти в выводе команды

if check_command_output(command, text):
    print("Текст найден в выводе команды")
else:
    print("Текст не найден в выводе команды")