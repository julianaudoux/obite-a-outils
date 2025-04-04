listcaracter = "abc"
def generer_mots_recursif(x, prefixe=""):
    if x == 0:
        return [prefixe]
        
    mots = []
    for carac in listcaracter:
        mots += generer_mots_recursif(x - 1, prefixe + carac)
    return mots
    

taille = 3 
liste_pwds = generer_mots_recursif(taille)
print(liste_pwds)