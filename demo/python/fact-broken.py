# ce fichier est intentionnellement cassé
# essayez de le lancer pour trouver ce qui ne va pas

def factorial(n)
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)


import sys
n = int(sys.argv[1])

print(f"fact({n}) = {factorial(n)}")
