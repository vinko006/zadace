"""
Potrebno napisati regex koji vraca podudaranje ukoliko se unese
string koji počinje kao prvo slovo vašeg imena, a završava kao prvo slovo
prezimena. String mora sadržavati bar jedan broj između 0 i 5 i razmak.
"""

import re

a = input("Unesi string:")
regex = "^V.*S$"
uvijet1 = re.match(regex, a)

regex2 = "[0-5]"
uvijet2 = re.search(regex2, a)

regex3 = "\s"
uvijet3 = re.search(regex3, a)

if uvijet1 and uvijet2 and uvijet3:
    print("Točno")
else:
    print("Netočno")
