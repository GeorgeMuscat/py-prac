def linear_congruence(a, b, m):
    if b == 0:
        return 0

    if a < 0:
        a = -a
        b = -b

    b %= m
    while a > m:
        a -= m

    return (m * linear_congruence(m, -b, a) + b) // a

def valueFinder(a, b, m):
    origM = m
    i = b

    while i > 0:
        if a % i == 0 and b % i == 0 and m % i == 0:
            a = int(a / i)
            b = int(b / i)
            m = int(m / i)
        i -= 1
        
    x = linear_congruence(a, b, m)
    i = m
    resultSet = []
    while x < origM:
        resultSet.append(x)
        x += m
        
    return resultSet

def numbasSetForm(set):
    
    s = ", ".join(str(i) for i in set)

    print("\nset(" + s + ")")

a = int(input("a: "))
b = int(input("b: "))
m = int(input("m: "))
numbasSetForm(valueFinder(a, b, m))
