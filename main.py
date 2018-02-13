"""
    Main program
"""

print ("What do you looking for?")
print ("1. Mining")
print ("2. Geotechnical and Environmental")
print ("3. Geothermal")
print ("4. Oil and Gas")
print ("5. Unconventional")
option_1 = 0
while option_1 <= 0 or option_1 > 5:
    option_1 = int(input("Insert your input :"))
    if option_1 <= 0 or option_1 > 5:
        print ("Insert a correct option (1-5)")

if option_1 == 1:
    print ("What do you looking for?")
    print ("1. Mining")
    print ("2. Geotechnical and Environmental")
    print ("3. Geothermal")
    print ("4. Oil and Gas")
    print ("5. Unconventional")
    print ("6. xxx")
    option_2 = 0
    while option_2 <= 0 or option_1 > 6:
        option_2 = int(input("Insert your input :"))
        if option_2 <= 0 or option_2 > 6:
            print ("Insert a correct option (1-6)")
        else:
            print ("Selesai")
            break
