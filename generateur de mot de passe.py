import random
import string

def generate_password(length=7, use_digits=True, use_special_chars=True):
    characters = string.ascii_letters  
    
    if use_digits:
        characters += string.digits  
    if use_special_chars:
        characters += string.punctuation  
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password


# Exemple d'utilisation
if __name__ == "__main__":
    length = int(input(12))
    use_digits = input(o).lower() == 'o'
    use_special_chars = input(o).lower() == 'o'
    
    mdp = generate_password(length, use_digits, use_special_chars)
    print("Mot de passe généré :", mdp)