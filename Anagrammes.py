#Def Un mot w est un anagramme d'un mot v s'il existe une permutation des lettres qui transforme w en v.
#Etant donné un ensemble de n mots de longueur au plus k, on veut détecter toutes les classes d'anagrammes.

#Entrée: "le chien marche vers sa niche et trouve une limace de chine nue pleine de malice qui lui fait du charme"

#Sortie: {une nue}, {marche charme}, {chien chine niche}, {malice limace}.

#Complexité La solution proposée résout ce problème en temps O(nk log k) en moyenne, en O(n²k log k) dans le pire cas dû
# à l'utilisation d'un dictionaire.

def anagrams(w):
    """
    >>> anagrams("le chien marche vers sa niche et trouve une limace de chine nue pleine de malice qui lui fait du charme")
    [['charme', 'marche'], ['niche', 'chine', 'chien'], ['malice', 'limace'], ['une', 'nue']]
    """
    w = w.split()
    w = list(set(w))
    d = {}                  #grouper les mots par meme signature
    for i in range(len(w)):
        s = ''.join(sorted(w[i]))   #signature
        if s in d:
            d[s].append(i)
        else:
            d[s] = [i]
    # -- extraire anagrammes
    reponse = []
    for s in d:
        if len(d[s]) > 1:
            reponse.append([w[i] for i in d[s]])    #ignorer mots sans anagrammes
    return reponse

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    w = "le chien marche vers sa niche et trouve une limace de chine nue pleine de malice qui lui fait du charme"
    print(anagrams(w))
