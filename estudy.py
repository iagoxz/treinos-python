i = int(input())

a = int(i / 365)

s = i - a*365

m = int(s / 30)
dias = s - m*30

print(a,'anos')
print(m,'meses')
print(dias,'dias')
