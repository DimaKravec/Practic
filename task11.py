def any_duplicates(square):
    plain = [i for x in square for i in x]
    return sorted(plain)!=[1,2,3,4,5,6,7,8,9]

print(any_duplicates([[1,2,3],[4,5,6],[7,8,9]]))
print(any_duplicates([[1,1,3],[4,5,6],[7,8,9]]))

