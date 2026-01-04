
rows=5
for i in range(rows):
    for k in range(rows -i -1):
        print( end=" ")
    for j in range(i + 1):
        print(i,end=" ")
    print()

for i in range(rows):
    for k in range(i):
        print(end=" ")
    for n in range(rows-i):
        print(rows-i-1,end=" ")
    print()













