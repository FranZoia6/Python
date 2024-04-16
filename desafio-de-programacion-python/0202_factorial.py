def factorial_it(numero):
    n = 1
    for i in range(1,numero+1):
        n = n*i
    return n

def factorial_re(numero):
    if numero==0:
        return 1
    return numero * factorial_re(numero-1)

print(factorial_it(0))
print(factorial_re(0))
print(factorial_it(3))
print(factorial_re(3))
print(factorial_it(5))
print(factorial_re(5))
    