num = int (input())

while num not in range(2,10001):
    num = int (input())

i = 1;

while i <=10:
    tabuada = i * num
    print(i,'x',num,'=',tabuada)
    i+=1