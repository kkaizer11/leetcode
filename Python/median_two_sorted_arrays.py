def findMedianSortedArrays(nums1: list[int], nums2: list[int]) -> float:
    comb = sorted(nums1 + nums2)
    # Se a quantidade de numeros for impar apenas identifica o elemento e retorna ele
    if len(comb) % 2== 1:
        return comb[int((len(comb)/2) - 1/2)]
    # Se a quantidade for par retorna a media dos dois centralizados
    else:
        return (comb[int(len(comb)/2)] + comb[int(len(comb)/2-1)])/2


# val1 = [1,3]
# val2 = [2,7]

# print(findMedianSortedArrays(val1, val2))