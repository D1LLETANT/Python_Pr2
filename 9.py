fib1 = 0
fib2 = 1
n = 20
i = 3
while i <= n:
     fib_sum = fib1 + fib2
     fib1 = fib2
     fib2 = fib_sum
     if i >= 5:
         print (fib_sum)
     i = i + 1


p = 1
while p <= 20:
     if p%2 == 0:
         print(p)
     p += 1


o = -1
while o >= -21:
     if o%3 == 0:
         print(o)
     o -= 1
