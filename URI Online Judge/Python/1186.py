op = input()
total = 0
count = 0
l = []
for row in range(12):
    for colum in range(12):
        value = float(input())
        if (row + colum) > 11 :
            total += value
            l.append(value)
            count += 1
if op == 'S':
    print('{:.1f}'.format(total))
else:
    print('{:.1f}'.format(total/count))
