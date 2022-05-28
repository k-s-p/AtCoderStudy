from functools import lru_cache

@lru_cache(maxsize=None) #同じ計算を行うなら即座に同じ値を返す
def Fib(n) :
    if n == 0 :
        return 1
    elif n == 1 :
        return 1
    else :
        return Fib(n-1) + Fib(n-2)

N = int(input())
print(Fib(N))
