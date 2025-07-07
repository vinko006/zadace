"""
Koristeći listu imena iz prethodnog zadatka svakom studentu generirati
nasumičnu ocjenu od 1 do 5.
Prebrojati u rječnik koliko ima kojih ocjena.
Izračunati postotak prolaznosti. (sve ocjene veće od 1)
"""
import random
imena = ['Karlo', 'Ana-Marija', 'Antonio', 'Marko', 'Matea', 'Vice', 'Sara', 'Ivana', 'Ante', 'Ivan Entoni', 'Tonka', 'Antonio',
'Mateo', 'Mateo', 'Josip', 'Marko', 'Tino', 'Azer', 'Tomislava', 'Katarina', 'Karlo', 'David', 'Ivan', 'Petar', 'Marija',
'Antonio', 'Mario', 'Josip', 'Leonardo', 'Antonio', 'Renato', 'Matej', 'Matej', 'Jozo Matej', 'Petar', 'Ivan', 'Stjepan',
'Petar', 'Dražen', 'Zvonimir', 'Marin', 'Antonio', 'Stipe', 'Ana', 'Mate', 'Miroslav', 'Karlo', 'Marino', 'Mija', 'Kristijan',
'Ante', 'Ana', 'Iva', 'Mladen', 'Ivan', 'Frano', 'Mate', 'Mateo', 'Harun']


rijecnik = dict()
for ime in imena:
    rijecnik[ime] = random.randint(1, 5)
    
print(rijecnik)

ocjene = dict()
for ocjena in rijecnik.values():
    if ocjena in ocjene:
        ocjene[ocjena] += 1
    else:
        ocjene[ocjena] = 1
        
print(ocjene)

broj_ucenika=len(rijecnik)

zbroj = 0
for ocjena in rijecnik.values():
    if ocjena > 1:
        zbroj += 1
        
postotak = (zbroj/broj_ucenika) * 100

print("Postotak prolaznosti je",round(postotak,2),"%")


