def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)

# cette fois-ci on veut pouvoir donner le nombre 'n'
# sur la ligne de commandes en tapant
# 
# python fact-argument.py 12
# 
# voici la façon la plus simple de retrouver ce '12'
# (pas forcément la meilleure dans la pratique d'ailleurs)

import sys
n = int(sys.argv[1])

# du coup on n'a plus qu'à imprimer le calcul
print(f"fact({n}) = {factorial(n)}")
