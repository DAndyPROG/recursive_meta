import time

def recurcive_reverse(n):
    if n == 1:
        return 1
    
    else:
        print(n)
        time.sleep(1)
        return recurcive_reverse(n-1)


result = recurcive_reverse(10)
print(result)
