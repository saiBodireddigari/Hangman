# put your python code here
list = []
s = []
n = 0
while True:
    n = int(input())
    list.append(n)
    for a in list:
        n = n + a
    if sum(list) == 0:
        break
for a in list:
    b = a * a
    s.append(b)

print(sum(s))

