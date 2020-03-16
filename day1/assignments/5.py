num = input()
n = len(num)
sum = 0
for digit in num:
    d = int(digit)
    sum += d ** n

if sum == int(num):
    print("the number is armstrong")
else:
    print("the number is not armstrong")