# Если учесть что входные данные целлые числа
c1 = int(input())
b1 = int(input())
new_c1, time, res, ostatok = 0, 2, 0, 0

while c1:
    res += c1 * time
    new_c1, ostatok = (c1+ostatok) // b1 * 2, (c1+ostatok) % b1
    c1 = new_c1
print(f'Сколько часов будет гореть огонек - {res}')