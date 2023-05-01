pos_a = int(input())
pos_b = int(input())
pos_c = int(input())

if pos_b-pos_a < pos_c-pos_b:
    print("1")
elif pos_b-pos_a > pos_c-pos_b:
    print("-1")
elif pos_b-pos_a == pos_c-pos_b:
    print("0")