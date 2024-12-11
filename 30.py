from random import randint
N=randint(1,100)
b = 0
for j in range(1, int(N // 2)+1):
        if N % j==0:
            b+=j
if b==N:
    print(N, "является совершенным числом")
else:
    print (N, "не является совершенным числом")
