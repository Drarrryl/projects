n = [14, 15, 16]
nID = id(n)
n2 = n 
n2[0] = 15
print(n, n2)
print("Same IDs:", nID == id(n))
print("ID for n:", id(n))
print("ID for n2:", id(n2))