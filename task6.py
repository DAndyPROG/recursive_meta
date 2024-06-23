def recursive_fibonacci(n):
    if n == 0:
        return 0
    
    elif n == 1:
        return 1
   
    else:
        return recursive_fibonacci(n-1) + recursive_fibonacci(n-2)
    

result = recursive_fibonacci(10) # повертає 55
result2 = recursive_fibonacci(9) # повертає 34 як на прикладі, певно там помилка

print(f"{result}\n{result2}")
