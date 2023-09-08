lst1 = [1, 2, 3]
lst2 = [1, 2, 3]
lst3 = lst2

print(lst2 is lst3)

temp = 18
L = [9, temp, 27]
temp = 99
print(L)

nested_list = [[1, 2], [3, 4]]
second_list = nested_list[1]
second_list[1] = -1
first_element = nested_list[0][0]
first_element = -1
print(nested_list[0][0], nested_list[1][1])

one = [0, 1, 2, 3, 4, 5, 6, 7]
two = one
one = one[1:5]
print(one, two)

a = [1, 2, 3, 4, 2, 9, 6]
b = [1, 2, 3, 4, 2, 9, 6]
a.remove(2)
print(a, b)