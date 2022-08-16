n = int(input())
sum = 0
if n > 0 :
    for x in range(n, (n*2)+1):
        sum += x
else:
    for x in range((n*2), n+1):
        sum += x
print(sum)