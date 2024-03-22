sum = 0
for i in range(6):
     chislo = int(input("Введіть ціле число: "))
     if chislo % 5 == 0:
         sum += chislo
print("Сума чисел = " ,sum)