a, b, c = sorted(map(int, input().split()))
 
if c*c == b*b + a*a:
    print("r")
elif c >= b + a:
    print("n")
elif c*c > b*b + a*a:
    print("o")
else:
    print("a")
