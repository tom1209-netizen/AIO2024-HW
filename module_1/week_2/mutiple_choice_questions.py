# Q5
def check_the_number(N):
    list_of_numbers = []
    result = ""

    for i in range(1, 5):
        list_of_numbers.append(i)

    if N in list_of_numbers:
        result = "True"
    else:
        result = "False"

    return result


# Test
N = 7
assert check_the_number(N) == "False"

N = 2
result = check_the_number(N)
print(result)


# Q6
def my_function(data, max_val, min_val):
    result = []
    for i in data:
        if i < min_val:
            result.append(min_val)
        elif i > max_val:
            result.append(max_val)
        else:
            result.append(i)
    return result


# Test
my_list = [5, 2, 5, 0, 1]
max_val = 1
min_val = 0
assert my_function(max_val=max_val, min_val=min_val, data=my_list) == [1, 1, 1, 0, 1]

my_list = [10, 2, 5, 0, 1]
max_val = 2
min_val = 1
print(my_function(max_val=max_val, min_val=min_val, data=my_list))


# Q7
def my_function(x, y):
    x.extend(y)
    return x


# Test
list_num1 = ['a', 2, 5]
list_num2 = [1, 1]
list_num3 = [0, 0]

assert my_function(list_num1, my_function(list_num2, list_num3)) == ['a', 2, 5, 1, 1, 0, 0]

list_num1 = [1, 2]
list_num2 = [3, 4]
list_num3 = [0, 0]

print(my_function(list_num1, my_function(list_num2, list_num3)))


# Q8
def my_function(n):
    return min(n)


# Test
my_list = [1, 22, 93, -100]
assert my_function(my_list) == -100

my_list = [1, 2, 3, -1]
print(my_function(my_list))


# Q9
def my_function(n):
    return max(n)


# Test
my_list = [1001, 9, 100, 0]
assert my_function(my_list) == 1001

my_list = [1, 9, 9, 0]
print(my_function(my_list))


# Q10
def My_function(integers, number = 1):
    return any(i == number for i in integers)


# Test
my_list = [1, 3, 9, 4]
assert My_function(my_list, -1) == False

my_list = [1, 2, 3, 4]
print(My_function(my_list, 2))


# Q11
def my_function(list_nums = [0, 1, 2]):
    var = 0
    for i in list_nums:
        var += i
    return var / len(list_nums)


# Test
assert my_function([4, 6, 8]) == 6
print(my_function())


# Q12
def my_function(data):
    var = []
    for i in data:
        if i % 3 == 0:
            var.append(i)
    return var


# Test
assert my_function([3, 9, 4, 5]) == [3, 9]
print(my_function([1, 2, 3, 5, 6]))


# Q13
def my_function(y):
    var = 1
    while y > 1:
        var *= y
        y -= 1
    return var


assert my_function(8) == 40320
print(my_function(4))


# Q14
def my_function(x):
    return x[::-1]


# Test
x = 'I can do it'
assert my_function(x) == "ti od nac I"

x = 'apricot'
print(my_function(x))


# Q15
def function_helper(x):
    return 'T' if x > 0 else 'N'


def my_function(data):
    res = [function_helper(x) for x in data]
    return res


# Test
data = [10, 0, -10, -1]
assert my_function(data) == ['T', 'N', 'N', 'N']

data = [2, 3, 5, -1]
print(my_function(data))


# Q16
def function_helper(x, data):
    for i in data:
        if x == i:
            return 0
    return 1


def my_function(data):
    res = []
    for i in data:
        if function_helper(i, res):
            res.append(i)
    return res


# Test
lst = [10, 10, 9, 7, 7]
assert my_function(lst) == [10, 9, 7]

lst = [9, 9, 8, 1, 1]
print(my_function(lst))
