i = int(input())

a = i//365

s = i - a*365

m = s / 30
dias = s - m*30

print(a, 'ano(s)')
print(m, 'mes(es)')
print(d, 'dia(s)')