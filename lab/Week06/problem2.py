def get_min_max(L:list) -> int:
    max = L[0]
    min = L[0]

    for element in L:
        if element > max:
            max = element
        if element < min:
            min = element
    L.remove(min)
    L.remove(max)
    
    return min,max

nlist = [3, 5, 9, 1, 2]
min, max = get_min_max(nlist)

print(min)
print(max)
print(nlist)