

def solve1(a,b,c):
    x = (c + 2*b)/a
    return x

def solve2(a,b,c):
    x = (c**2-2*b)/a
    return x
coeffs = input("input a,b, and c for mononomial in the form ax-2b=c to solve for x")
a, b, c = coeffs.split()
print(solve1(int(a), int(b), int(c)))
coeffs2 = input("input a,b, and c for mononomial in the form sqrt(ax+2b) to solve for x")
a, b, c = coeffs2.split()
print(solve2(int(a), int(b), int(c)))
