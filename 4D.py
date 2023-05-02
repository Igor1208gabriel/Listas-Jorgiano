com = int(input())
dis = int(input())
lit = int(input())
 
div = dis / com
nec = div - lit 
 
if nec < 0:
    print(0.0)
else:
    print(f"{nec:.1f}")
