nums = [int(x) for x in input("Enter a list of numbers").split()]

for num in nums:
    if num%2==1 and num<14:
        print(num, end=' ')