def merge_sort(data):
    if len(data) > 1:
        mitad = len(data) // 2
        izquierda = data[0:mitad:1]
        derecha = data[mitad::]
        print(f"{izquierda}  --- {derecha}")
        merge_sort(izquierda)
        merge_sort(derecha)
        # marge
        i = 0
        d = 0
        k = 0
        while (i < len(izquierda) and d < len(derecha)):
            if izquierda[i] < derecha[d]:
                data[k] = izquierda[i]
                i += 1
            else:
                data[k] = derecha[d]
                d += 1
            k += 1

        # acomodar los restantes
        while i < len(izquierda):
            data[k] = izquierda[i]
            i += 1
            k += 1

        while d < len(derecha):
            data[k] = derecha[d]
            d += 1
            k += 1
    print(f"regreso de rec: {data}")
    return data


print(".-.-.-.-.-.- MERGE --.-.-.-.-")
info = [38, 27, 43, 3, 9, 82, 10, 19, 50, 61]
print(merge_sort(info))

print(".-.-.-. suma recursiva --------")
