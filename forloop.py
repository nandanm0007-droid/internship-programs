mylist = [3, 4, 3, 22, 3, 4, 5, 4]

for i in range(len(mylist)):
    print(mylist[i])

i = 1
while i < 30:
    if i % 5 == 0 or i % 7 == 0:
        print(i, end="  ")
    i += 1

k = 1
print("\n")

while k <= 30:
    print(k, end=" ")
    k += 1