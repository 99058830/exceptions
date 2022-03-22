#Jordy van Zomeren, 99058830, Pizza calculator

#Bewaren van prijzen
small = 5.95
medium = 7.95
large = 9.95

#Print simpel onderstaand menu
print("""
|------------------------------------------------
|                    ONS MENU
|------------------------------------------------
|                     SMALL
|                  20cm | 5,95 euro
|------------------------------------------------
|                     MEDIUM
|                  25cm | 7,95 euro
|------------------------------------------------
|                     LARGE
|                  30cm | 9,95 euro              
|------------------------------------------------
""")

try:
    hoeveelSmall = int(input("Aantal small size pizza's "))
except:
    print('Probeer eens een nummer in te voeren')
try:
    hoeveelMedium = int(input("Aantal medium size pizza's "))
except:
    print('Probeer eens een nummer in te voeren')
try:
    hoeveelLarge = int(input("Aantal large size pizza's "))
except:
    print('Probeer eens een nummer in te voeren')

#Reken sommen die uitgevoerd moeten worden
try:
    allPrice = hoeveelSmall * small + hoeveelMedium * medium + hoeveelLarge * large
except:
    print('Dit gaat niet werken')
try:
    prijsSmall = hoeveelSmall * small
except:
    print('Dit gaat niet werken')
try:
    prijsMedium = hoeveelMedium * medium
except:
    print('Dit gaat niet werken')
try:
    prijsLarge = hoeveelLarge * large
except:
    print('Dit gaat niet werken')

#print en uitkomst van de prijzen die opgetelt zijn door de bovenstaande rekensom
try:
    print("""
    |------------------------------------------------
    |Small hoeveelheid    :""",hoeveelSmall,"""
    |Small prijs totaal   :""",prijsSmall,"""euro
    |------------------------------------------------
    |Medium hoeveelheid   :""",hoeveelMedium,"""
    |Medium prijs totaal  :""",prijsMedium,"""euro
    |------------------------------------------------
    |Large hoeveelheid    :""",hoeveelLarge,"""
    |Large prijs totaal   :""",prijsLarge,"""euro
    |------------------------------------------------
    |Te betalen           :""",allPrice,"""euro
    |------------------------------------------------
    """)
except:
    print('Je moet bij je input alleen maar cijfers invoeren')