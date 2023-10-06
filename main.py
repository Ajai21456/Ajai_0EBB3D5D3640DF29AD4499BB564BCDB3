def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

result= factorial(5)
print("the factorial of given number is:",result)
      
