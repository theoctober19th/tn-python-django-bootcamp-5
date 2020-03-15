nums = [int(x) for x in input("Enter numbers: ").split()]
for num in nums:
    if num % 3 == 0 and num % 5 == 0:
        print(num, end=' ')