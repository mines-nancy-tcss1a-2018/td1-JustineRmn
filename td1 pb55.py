def palindrome(nombre):
    chaine=str(nombre)
    i=0
    while chaine[i] == chaine[-1-i] and i < len(chaine)//2:
        i=i+1
    if i == len(chaine)//2:
        return (True)
    else:
        return (False)

def sommeLychrel(nombre):
    chaine = str(nombre) #convertir en caract pour inverser
    chaineinv = ''
    for k in range(len(chaine)):
        chaineinv += chaine[-1-k]
    return(nombre+int(chaineinv))
    
def solve(n):
    total = 0 #nombre de Lychrel numbers
    verif=0
    for i in range(1,10001): #10 000 premiers nombres
        j = 0 #compteur d'itérations
        somme = i #initialisation
        if palindrome(i):
            somme=2*i
            while not palindrome(somme) and j<49:
                somme = sommeLychrel(somme)
                j += 1
            if palindrome(somme):
                total += 1
        else:
            while not palindrome(somme) and j<50:
                somme = sommeLychrel(somme)
                j += 1
            if i==n:
                verif=j
            if palindrome(somme):
                total += 1
    return (verif,10000-total)

print(solve(0)[1])

assert(solve(349)[0] == 3)

        
        