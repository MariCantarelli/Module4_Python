#multiple arguments xargs with numbers 

def sum(*numbers):
    result = 0 
    for num in numbers:
        result += num
    return result

x = sum (2, 3, 4, 7)
print(x)