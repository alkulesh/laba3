with open("Клиент банка.txt", "r", encoding="utf-8") as file:
    try:
        sum_ =0
        for line in file:
            data = line.split()
            name = data[0]
            amount = int(data[1])
            last = data[2]
            if amount == 0:
                print(name)
            sum_ = sum_ + amount
        print("Общая сумма вложений всех клиентов равна:", sum_)
    except IOError:
        print("Ошибка при открытии файла! ")