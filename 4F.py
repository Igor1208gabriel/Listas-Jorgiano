a1, a2 = map(int, input().split())
b1, b2 = map(int, input().split())
p1, p2 = map(int, input().split())
    
media_a = ((a1*p1)+(a2*p2))//(p1+p2)
media_b = ((b1*p1)+(b2*p2))//(p1+p2)
    
if media_a >= media_b:
    print(1)
elif media_b > media_a:
    print(2)
