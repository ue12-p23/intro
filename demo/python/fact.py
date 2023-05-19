# une fonction qui calcule factorielle
def fact(n):
    return 1 if n <= 1 else n * fact(n-1)


# on affiche quelques résultats
for n in [4, 25]:
    print(f"fact({n}) = {fact(n)}")
