def solve(n):
    chaine = str(2**n)
    somme = 0
    for i in range (len(chaine)):
        somme += int(chaine[i])
    return somme
    
assert solve(15)==26

print(solve(1000))
