print("Break....")

for num in range(1, 11):
    if num == 6:
        break  # breaking the loop at 6
    print(num)

print("Continue....")

for num in range(1, 11):
    if num % 2 == 0:
        continue  # Skip the rest of the loop for even numbers
    print(num)