def potenciacion(a, b):
    if b == 0:
        return 1
    elif b < 0:
        return 1 / potenciacion(a, -b)
    else:
        return a * potenciacion(a, b - 1)


print(potenciacion(10, 0))
print(potenciacion(5, 5))
print(potenciacion(2, -1))
