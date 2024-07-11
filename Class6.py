#multiple arguments xargs with numbers 

def soma(*numbers):
    resultado = 0 
    for num in numbers:
        resultado += num
    return resultado

x = soma (2, 3, 4, 7)
print(x)