while True:
    a, b = map(int, input().split())
    if a > b:
        print("Decrescente")
    elif b > a:
        print("Crescente")
    elif a == b:
        break
    