b = int(input("Base: "))
e = int(input("Exponent: "))
m = int(input("m: "))
def modPow(b, e, m):
    if m == 1:
        return 0
    else:
        r = 1
        b = b % m
        while e > 0:
            if e % 2 == 1:
                r = (r*b) % m
            b = (b*b) % m
            e = e >> 1 
        
        return r
    
print("---\nAnswer: ", modPow(b,e,m))