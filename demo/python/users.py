
# une classe nous permet de représenter des données applicatives
# ici on veut créer comme un seul objet 'User' une collection d'informations
# on peut ensuite passer cet objet unique à d'autres fonctions

class User:
    
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        
    def __repr__(self):
        return f"{self.first_name} ({self.last_name}), {self.age} ans"
    
    
# on crée maintenant deux objets de ce type    
users = [
    User("Emilie", "Lambert", 25),
    User("Julien", "Masson", 30),
]

# on peut les afficher
for user in users:
    print(user)

