def fibonacci (n):
    if n==1:
        return 1
    if n==2:
        return 1
    else:
        return (n-1)+fibonacci(n-1)
if __name__=="__main__":
    n=int(input("Introduzca un numero"))
    fibonacci(n)
    print(fibonacci(n))