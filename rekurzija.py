"""
Napisati rekurzivnu funkciju koja kao parametar prima string,
a kao rezultat taj string ispisuje sa zada
"""

def obrnuti(a):
    if len(a) <= 1:
        return a
    else:
        return obrnuti(a[1:]) + a[0]


tekst = input("Unesi neki string: ")


print("String unazad je:", obrnuti(tekst))
