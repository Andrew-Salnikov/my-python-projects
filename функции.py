def minimal(L):
    min_number = L[0]
    for el in L:
        if el < min_number:
            min_number = el
    
    return min_number

nums1 = [5, 7, 3]
min1 = minimal(nums1)

nums2 = [2.1, 3.4, 11.6]
min2 = minimal(nums2)

print(f"{min1} and {min2}")

func = lambda x, y: x * y
print(func(5, 2))