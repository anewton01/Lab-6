#the authors' names are Abby Newton and Mandy Guo
def fib(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib(n-1)+fib(n-2)
    
