def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

num1 = int(input("Entrez le premier nombre entier: "))
num2 = int(input("Entrez le deuxième nombre entier: "))

print("Le PGCD de", num1,"et", num2,"est", gcd(num1, num2))