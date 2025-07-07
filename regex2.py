"""
Napisati regex za provjeru validnosti unosa e-maila.
E-Mail mora biti formata ime.prezime@fpmoz.sum.ba
Nakon toga napisati regex za provjeru eduId koji mora biti
formata iprezimeX@sum.ba gdje je i prvo slovo
imena + prezime.
X predstavlja bilo koji broj (moze ici u beskonacnost),
a taj broj ne mora postojati (može biti samo
iprezime@sum.ba).
Od korisnika zatražiti unos maila i eduid te ispisati uspješnost.
Istražiti greedy i non-greedy quantifiers.
"""

import re

a = input("Unesite vašu email adresu:")

regex1 = "^[a-zA-Z]+\.[a-zA-Z]+@fpmoz\.sum\.ba$"

rezultat = re.match(regex1, a)
print(rezultat)

b = input("Unesite vaš eduID:")

regex2 = "^[a-zA-Z][a-zA-Z]+[0-9]*@sum\.ba$"

rezultat2 = re.match(regex2, b)

print(rezultat2)

if rezultat and rezultat2:
    print("Vaš Email i eduID su ispravni!")
else:
    print("Vaš Email ili eduID nisu ispravni!")
