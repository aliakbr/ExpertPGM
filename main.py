"""
    Main program
"""
# Tes
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
    print ("More Spesific ?")
    print ("1. VMS Deposit")
    print ("2. Uranium Deposit")
    print ("3. Porphyry Copper Deposit")
    print ("4. Diamond")
    print ("5. Lode Gold")
    print ("6. Coal")
    option_2 = 0
    while option_2 <= 0 or option_2 > 6:
        option_2 = int(input("Insert your input :"))
        if option_2 <= 0 or option_2 > 6:
            print ("Insert a correct option (1-6)")
        if option_2 == 1:
            print ("1. Air")
            print ("2. Ground")
            option_3 = 0
            while option_3 <= 0 or option_3 > 2:
                option_3 = int(input("Insert your input :"))
                if option_3 <= 0 or option_3 > 2:
                    print ("Insert a correct option (1-2)")
            if option_3 == 1:
                print ("1. Geological Framework")
                print ("2. Direct Targeting")
                option_4= 0
                while option_4 <= 0 or option_4 > 2:
                    option_4 = int(input("Insert your input :"))
                    if option_4 <= 0 or option_4 > 2:
                        print ("Insert a correct option (1-2)")
                if option_4 == 1:
                    print ("Magnetic and Radiometric")
                else:
                    print ("Magnetic, EM, and Gravity")
            else:
                print ("1. Geological Framework")
                print ("2. Direct Targeting")
                option_4= 0
                while option_4 <= 0 or option_4 > 2:
                    option_4 = int(input("Insert your input :"))
                    if option_4 <= 0 or option_4 > 2:
                        print ("Insert a correct option (1-2)")
                if option_4 == 1:
                    print ("Magnetic")
                else:
                    print ("Magnetic, EM, Electrical, and Gravity")
                
        elif option_2 == 2:
            print ("1. Air")
            print ("2. Ground")
            option_3 = 0
            while option_3 <= 0 or option_3 > 2:
                option_3 = int(input("Insert your input :"))
                if option_3 <= 0 or option_3 > 2:
                    print ("Insert a correct option (1-2)")
            if option_3 == 1:
                print ("1. Geological Framework")
                print ("2. Direct Targeting")
                option_4= 0
                while option_4 <= 0 or option_4 > 2:
                    option_4 = int(input("Insert your input :"))
                    if option_4 <= 0 or option_4 > 2:
                        print ("Insert a correct option (1-2)")
                if option_4 == 1:
                    print ("Magnetic, EM, and Radiometric")
                else:
                    print ("EM and Radiometric")
            else:
                print ("1. Geological Framework")
                print ("2. Direct Targeting")
                option_4= 0
                while option_4 <= 0 or option_4 > 2:
                    option_4 = int(input("Insert your input :"))
                    if option_4 <= 0 or option_4 > 2:
                        print ("Insert a correct option (1-2)")
                if option_4 == 1:
                    print ("Magnetic, EM, Gravity, and Radiometric")
                else:
                    print ("EM and Radiometric")
        elif option_2 == 3:
            print ("1. Air")
            print ("2. Ground")
            option_3 = 0
            while option_3 <= 0 or option_3 > 2:
                option_3 = int(input("Insert your input :"))
                if option_3 <= 0 or option_3 > 2:
                    print ("Insert a correct option (1-2)")
            if option_3 == 1:
                print ("1. Geological Framework")
                print ("2. Direct Targeting")
                option_4= 0
                while option_4 <= 0 or option_4 > 2:
                    option_4 = int(input("Insert your input :"))
                    if option_4 <= 0 or option_4 > 2:
                        print ("Insert a correct option (1-2)")
                if option_4 == 1:
                    print ("Magnetic and Radiometric")
                else:
                    print ("Magnetic and Radiometric")
            else:
                print ("1. Geological Framework")
                print ("2. Direct Targeting")
                option_4= 0
                while option_4 <= 0 or option_4 > 2:
                    option_4 = int(input("Insert your input :"))
                    if option_4 <= 0 or option_4 > 2:
                        print ("Insert a correct option (1-2)")
                if option_4 == 1:
                    print ("Magnetic and Radiometric")
                else:
                    print ("Magnetic, Electric, and Radiometric")
        elif option_2 == 4:
            print ("1. Air")
            print ("2. Ground")
            option_3 = 0
            while option_3 <= 0 or option_3 > 2:
                option_3 = int(input("Insert your input :"))
                if option_3 <= 0 or option_3 > 2:
                    print ("Insert a correct option (1-2)")
            if option_3 == 1:
                print ("1. Geological Framework")
                print ("2. Direct Targeting")
                option_4= 0
                while option_4 <= 0 or option_4 > 2:
                    option_4 = int(input("Insert your input :"))
                    if option_4 <= 0 or option_4 > 2:
                        print ("Insert a correct option (1-2)")
                if option_4 == 1:
                    print ("Magnetic")
                else:
                    print ("Magnetic, EM, and Gravity")
            else:
                print ("1. Geological Framework")
                print ("2. Direct Targeting")
                option_4= 0
                while option_4 <= 0 or option_4 > 2:
                    option_4 = int(input("Insert your input :"))
                    if option_4 <= 0 or option_4 > 2:
                        print ("Insert a correct option (1-2)")
                if option_4 == 1:
                    print ("Magnetic, EM, and Gravity")
                else:
                    print ("Magnetic, EM, and Gravity")
        elif option_2 == 5:
            print ("1. Air")
            print ("2. Ground")
            option_3 = 0
            while option_3 <= 0 or option_3 > 2:
                option_3 = int(input("Insert your input :"))
                if option_3 <= 0 or option_3 > 2:
                    print ("Insert a correct option (1-2)")
            if option_3 == 1:
                print ("1. Geological Framework")
                print ("2. Direct Targeting")
                option_4= 0
                while option_4 <= 0 or option_4 > 2:
                    option_4 = int(input("Insert your input :"))
                    if option_4 <= 0 or option_4 > 2:
                        print ("Insert a correct option (1-2)")
                if option_4 == 1:
                    print ("Magnetic and Radiometric")
                else:
                    print ("EM and Radiometric")
            else:
                print ("1. Geological Framework")
                print ("2. Direct Targeting")
                option_4= 0
                while option_4 <= 0 or option_4 > 2:
                    option_4 = int(input("Insert your input :"))
                    if option_4 <= 0 or option_4 > 2:
                        print ("Insert a correct option (1-2)")
                if option_4 == 1:
                    print ("Magnetic and Radiometric")
                else:
                    print ("Magnetic, Electrical, and Radiometric")
        elif option_2 == 6:
            print ("Gravity, Seismic Reflection, Seismic Refraction, and Magnetic ")
elif option_1 == 2:
    print ("1. Inorganic Contaminant")
    print ("2. Man Made Buried Object")
    print ("3. Natural Condition")
    option_2= 0
    while option_2 <=0 or option_2 > 3:
        option_2 = int(input("Insert your input :"))
        if option_2 <= 0 or option_2 > 3:
            print ("Insert a correct option (1-3)")
    if option_2 == 1:
        print ("1. Soil Salinity")
        print ("2. Salt Water Intrusion")
        print ("3. Land Fill")
        option_3 = 0
        while option_3 <= 0 or option_3 > 3:
            option_3 = int(input("Insert your input :"))
            if option_3 <= 0 or option_3 > 3:
                print ("Insert a correct option (1-3)")
        if option_3 == 1:
            print ("DC Resistivity and Frequency Domain EM")
        elif option_3 == 2:
            print ("DC Resistivity, Frequency Domain EM, and Time Domain EM")
        elif option_3 == 3:
            print ("DC Resistivity, Frequency Domain EM, Time Domain EM")
    elif option_2 == 2:
        print ("1. Utilities (Cable, Pipe, etc)")
        print ("2. Abandoned Wells")
        print ("3. Forensic")
        print ("4. Archeology")
        option_3 = 0
        while option_3 <=0 or option_3 > 4:
            option_3 = int(input("Insert your input :"))
            if option_3 <=0 or option_3 > 4:
                print ("Insert a correct option (1-4)")
        if option_3 == 1:
            print ("Ground Penetrating Radar (GPR)")
        elif option_3 == 2:
            print ("Magnetic")
        elif option_3 == 3:
            print ("Frequency Domain EM")
        elif option_3 == 4:
            print ("Frequency Domain EM, GPR, Magnetic")
    elif option_2 == 3:
        print ("1. Depth to Water Table")
        print ("2. Karst")
        print ("3. Buried Channel")
        print ("4. Sinkhole")
        print ("4. Sinkhole")
        print ("5. Dam/Lagoon Leakage")
        print ("6. Buried Fault/Dyke")
        print ("7.Starigraphical")
        option_3 = 0
        while option_3 <=0 or option_3 > 7:
            option_3 = int(input("Insert your input :"))
            if option_3 <=0 or option_3 > 7:
                print ("Insert a correct option (1-7)")
        if option_3 == 1:
            print ("DC Resistivity, Seismic Refraction, and GPR")
        elif option_3 == 2:
            print ("Microgravity and GPR")
        elif option_3 == 3:
            print ("DC Resistivity and Seismic Refraction")
        elif option_3 == 4:
            print ("GPR and Microgravity")
        elif option_3 == 5:
            print ("DC Resistivity, Seismic, and Magnetic")
        elif option_3 == 6:
            print ("Sediment Overbedrock")
            print ("1. Sand and Gravel Overlaying Bedrock, Water Table, Low in Sand & Gravel")
            print ("2. Sand and Gravel Overlaying Bedrock, Water Table, High in Sand & Gravel")
            print ("3. Clay Overlaying Bedrock")
            option_4 = 0
            while option_4 <=0 or option_4 > 3:
                option_4 = int(input("Insert your input :"))
                if option_4 <=0 or option_4 > 3:
                    print ("Insert a correct option (1-3)")
            if option_4 == 1:
                print ("1. Land")
                print ("2. Marine")
                option_5 = 0
                while option_5 <=0 or option_5 > 2:
                    option_5 = int(input("Insert your input :"))
                    if option_5 <=0 or option_5 > 2:
                        print ("Insert a correct option (1-2)")
                if option_5 == 1:
                    print ("Seismic Refraction")
                else:
                    print ("Continuous Reflection Seismic Profilling (CRSP)")
            elif option_4 == 2:
                print ("1. Land")
                print ("2. Marine")
                option_5 = 0
                while option_5 <=0 or option_5 > 2:
                    option_5 = int(input("Insert your input :"))
                    if option_5 <=0 or option_5 > 2:
                        print ("Insert a correct option (1-2)")
                if option_5 == 1:
                    print ("Resistivity")
                else:
                    print ("Continuous Reflection Seismic Profilling (CRSP)")
            elif option_4 == 3:
                print ("1. Land")
                print ("2. Marine")
                option_5 = 0
                while option_5 <=0 or option_5 > 2:
                    option_5 = int(input("Insert your input :"))
                    if option_5 <=0 or option_5 > 2:
                        print ("Insert a correct option (1-2)")
                if option_5 == 1:
                    print ("Resistivity, Seismic Refraction")
                else:
                    print ("Continuous Reflection Seismic Profilling (CRSP)")
elif option_1 == 3:
    print ("1. Exploration")
    print ("2. Deveploment")
    option_2 = 0
    while option_2 <= 0 or option > 2:
        option_2 = int(input("Insert your input :"))
        if option_2 <=0 or option_2 > 2:
            print ("Insert a correct option (1-2)")
    if option_2 == 1:
        print ("1. Clay Cap Distribution")
        print ("2. Delineation Reservation & Basement")
        option_3 = 0
        while option_3 <=0 or option_3 > 2:
            option_3 = int(input("Insert your input :"))
            if option_3 <=0 or option_3 > 2:
                print ("Insert a correct option (1-2)")
        if option_3 == 1:
            print ("MT, Gravity, Time Domain EM")
        else:
            print ("MT, Gravity, Magnetic, Passive Seismic, Time Domain EM")
    else:
        print ("1. Well Target Zone")
        print ("2. Monitoring")
        option_3 = 0
        while option_3 <=0 or option_3 > 2:
            option_3 = int(input("Insert your input :"))
            if option_2 <=0 or option_3 > 2:
                print ("Insert a correct option (1-2)")
        if option_3 == 1:
            print ("Passive Seismic, MT, and Gravity")
        else:
            print ("Microearthquake, Microgravity")
elif option_1 == 4:
    print ("Exploration")
    print ("1. Delineation Reservoir Hydrocarbon")
    print ("2. Delineation Basement")
    print ("3. Structural Mapping")
    option_2 = 0
    while option_2 <=0 or option_2 > 3:
        option_2 = int(input("Insert your input :"))
        if option_2 <=0 or option_2 > 3:
            print ("Insert a correct option (1-3)")
    if option_2 == 1:
        print ("Seismic Reflection")
    elif option == 2:
        print ("Gravity, Seismic Reflection")
    else:
        print ("Gravity, Seismic Reflection, Magnetic, Seismic Refraction")
else:
    print ("1.Shale Gas and Shale Oil")
    print ("2. Hydrate Gas")
    option_2 = 0
    while option_2 <=0 or option > 2:
        option_2 = int(input("Insert a correct option (1-2)"))
        if option_2 <=0 or option > 2:
            print ("Insert a correct option (1-2)")
    if option_2 == 1:
        print ("Seismic Reflection, Gravity")
    else:
        print ("Seismic Reflaction")