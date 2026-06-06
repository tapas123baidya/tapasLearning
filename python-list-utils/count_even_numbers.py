numbers = [12, 45, 7, 89, 23, 10, 8]
count = sum(1 for n in numbers if n % 2 == 0)
print("Number of even elements:", count)
