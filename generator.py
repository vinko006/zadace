"""
Napraviti generator funkcije za ispis svih parnih i svih
neparnih brojeva manjih od prosljeđenog parametra
"""
def parni(broj):
    for i in range(broj):
        if i % 2 == 0:
            yield i

def neparne(broj):
    for i in range(broj):
        if i % 2 != 0:
            yield i

a = int(input("Unesi neki broj:"))

for broj in parni(a):
    print("Parni brojevi manj od", a, ":", broj)

for broj in neparne(a):
    print("Neparni brojevi manj od", a, ":", broj)
