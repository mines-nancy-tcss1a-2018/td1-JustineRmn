def score(prenom,place):
    alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    score = 0
    for k in range(len(prenom)): 
        for j in range(26):
            if prenom[k] == alphabet[j]:
                score += j+1
    score *= place
    return(score)

def solve(n):
    fichier = open('C:\Users\Public\Documents\p022_names.txt', 'r')
    total = 0
    for ligne in fichier:
        Liste_noms = ligne.split(',')
    fichier.close()
    Liste_noms.sort()
    for i in range(len(Liste_noms)):
        total += score(Liste_noms[i],i+1)
    return (score(Liste_noms[n-1],n),total)

assert(solve(938)[0] == 49714)

        
        