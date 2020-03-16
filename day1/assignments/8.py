PI = 3.1415

def time_period(L, g=9.8):
    return 2 * PI * (L/g) ** 0.5

L = float(input("Enbter length"))
g = input("enter acc due to gravity")
if g == '':
    print("Time period=", time_period(L))
else:
    g = float(g)
    print("time period=", time_period(L,g))