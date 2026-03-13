def merge_list(L1, L2) -> list:
    List = L1 + L2
    List.sort()
    return List

L = [3, 5, 9, 1, 2]
ml1 = merge_list(L, [2, 1])
ml2 = merge_list([6, 9, 4], L)

print(ml1)
print(ml2)