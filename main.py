with open("F1.txt","w") as f1:
    while True:
        line = input("Введите строку (для окончания ввода введите пустую строку)")
        if line == "":
            break
        f1.write(line + "\n")
with open("F1.txt", "r") as f1, open("F2.txt", "w") as f2:
    for line in f1:
        if not any(char.isdigit() for char in line):
            f2.write(line)
with open("F2.txt","r") as f2:
    lines = f2.readlines()
    if len(lines) == 0:
        print("Файл F2 пустой!")
    else:
        last_line = lines[-1]
        word = last_line.split(  )
        if len(word) == 0:
            print("Последняя строка файла F2 не содержит слов!")
        else:
            words = len(word)
            print("Количество слов в последней строке файла F2: ", words)