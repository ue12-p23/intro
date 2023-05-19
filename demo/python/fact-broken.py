# ce fichier est intentionnellement cassé

def factorial(n)
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)


import sys
n = int(sys.argv[1])

print(f"fact({n}) = {factorial(n)}")
