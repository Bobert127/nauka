import random

temp = 15
temp_2 = '15'
mnozenie = temp * int(temp_2)


dodawanie = temp + int(temp_2)


dzielenie = temp / int(temp_2)



print(mnozenie, dodawanie, dzielenie)
print(type(temp))
print(type(temp_2))

if type(temp) == int:
    print(f'Mnożenie zmiennej {temp} temp * 5')
elif type(temp) == float:
    print(temp / 5)
elif type(temp) == string:
    print(temp)

no_of_stars = random.randint(1, 20)
print(f'Wylosowana liczba {no_of_stars}')
print(no_of_stars * "*")

rows = random.randint(5, 15)
columns = random.randint(5, 15)
print(f'Wartość zmiennej rows {rows}')
print(f'Wartość zmiennej columns {columns}')

for i in range(rows):
    for j in range(columns):
        print ("*", end = ' ')
    print()






size = random.randint(3, 9)
print(f'Wielkość choinki: {size}')

for i in range(1, size +1):
    print(i * "*")

