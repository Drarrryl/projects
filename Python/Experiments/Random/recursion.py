def sum_lists(lst: list) -> int:
    if len(lst) == 1:
        if type(lst[0]) != list:
            return lst[0]
        else:
            return sum_lists(lst[0])
    else:
        sum = 0
        for i in lst:
            if type(i) != list:
                sum += i
            else:
                sum += sum_lists(i)
        return sum

def factorial(num: int) -> int:
    if num <= 1:
        return 1
    else:
        return num * factorial(num - 1)

def reverse(string: str) -> str:
    if string[0:1] == string:
        return string
    else:
        return string[-1:] + reverse(string[0:len(string)-1])

def countDown(count: int) -> None:
    if count < 0:
        return
    elif count == 0:
        print(count)
    else:
        print(count)
        countDown(count - 1)

def digitsToWords(num: int) -> str:
    if (len(str(num)) == 1 and num == 0):
        return ''
    else:
        chosen = int(str(num)[0:1])
        result = intToName(chosen) + ' '
        result += digitsToWords(num - ((chosen)*10**(len(str(num))-1)))
        return result

def intToName(num: int) -> str:
    if num == 0:
        return 'zero'
    if num == 1:
        return 'one'
    if num == 2:
        return 'two'
    if num == 3:
        return 'three'
    if num == 4:
        return 'four'
    if num == 5:
        return 'five'
    if num == 6:
        return 'six'
    if num == 7:
        return 'seven'
    if num == 8:
        return 'eight'
    if num == 9:
        return 'nine'
    return ''

def reverseNum(num: int) -> int:
    if len(str(num)) == 1:
        return num
    else:
        chosen = int(str(num)[0:1])
        next = int(str(num)[1:len(str(num))])
        return chosen + reverseNum(next)*10

def power(num: int, pow: int) -> int:
    if pow == 0:
        return 1
    else:
        return num * power(num, pow-1)

def combineLists(lst1: list, lst2: list) -> list:
    if len(lst1) == 0:
        return lst2
    elif len(lst2) == 0:
        return lst1
    elif len(lst1) == len(lst2):
        combined = [lst1[0]]
        new_lst1 = []
        for i,val in enumerate(lst1):
            if i != 0:
                new_lst1.append(val)
        combined += combineLists(new_lst1, lst2)
        return combined
    else:
        combined = []
        new_lst = []

        if len(lst1) > len(lst2):
            combined = [lst1[0]]
            for i,val in enumerate(lst1):
                if i != 0:
                    new_lst.append(val)
            combined += combineLists(new_lst, lst2)
        else:
            combined = [lst2[0]]
            for i,val in enumerate(lst2):
                if i != 0:
                    new_lst.append(val)
            combined += combineLists(lst1, new_lst)
        
        return combined
        
def fibonacci(num: int) -> int:
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fibonacci(num-2) + fibonacci(num-1)

def sumOfDigits(num: int) -> int:
    if num <= 0:
        return 0
    elif num < 10:
        return num
    else:
        sum = int(str(num)[0])
        new_num = int(str(num)[1:])
        return sum + sumOfDigits(new_num)

def sumOfNaturals(num: int) -> int:
    if num == 1:
        return 1
    else:
        return num + sumOfNaturals(num-1)

def LCM(num1: int, num2: int) -> int:
    r = num1 % num2
    if r == 0:
        return num1
    else:
        return num1 * LCM(num2, r) // r

def GCD(num1: int, num2: int) -> int:
    r = num1 % num2
    if r == 0:
        return num2
    else:
        return GCD(num2, r)

def mergeSort(lst: list) -> None:
    size = len(lst)
    if size > 1:
        mid = size // 2

        left = lst[:mid]
        right = lst[mid:]

        mergeSort(left)
        mergeSort(right)

        l_size = len(left)
        r_size = len(right)

        i = 0
        j = 0
        k = 0

        while i < l_size and j < r_size:
            if left[i] < right[j]:
                lst[k] = left[i]
                i += 1
            else:
                lst[k] = right[j]
                j += 1
            k += 1
        
        while i < l_size:
            lst[k] = left[i]
            i += 1
            k += 1
        
        while j < r_size:
            lst[k] = right[j]
            j += 1
            k += 1


lst1 = [8, 2, 3, 4, 5, 6, 7, 1]
lst2 = [4, 5, 6]

#mergeSort(lst1)

print(reverseNum(10001242140120401))