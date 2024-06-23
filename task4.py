def recursive_revesed_word(n):
    
    if len(n) == 0:
        return n
    
    else:
        return recursive_revesed_word(n[1:]) + n[0]
    

result = recursive_revesed_word('hello')
print(result)
