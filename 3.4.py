import json
with open("Фирмы.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()
profit_data = {}
total_profit = 0
count = 0
for line in lines:
    data = line.split()
    revenue = int(data[2]) #прибыль
    costs = int(data[3]) #издержки
    profit = revenue - costs
    name = data[0]
    profit_data[name]= profit
    if profit > 0:
        count +=1
        total_profit += profit
average_profit = total_profit / count
result = [profit_data, {"average_profit": average_profit}]
with open("firm_data.json", "w") as file:
    json.dump(result, file)