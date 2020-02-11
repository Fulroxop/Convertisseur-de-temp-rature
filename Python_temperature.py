conv = {}
conv[("Celsius","Kelvin")] = lambda x: x+273.15
conv[("Celsius","Fahrenheit")] = lambda x: x*(9/5)+32
conv[("Celsius","Rankine")] = lambda x: (x+273)*(9/5)
conv[("Fahrenheit","Celsius")] = lambda x: (x+459.67)*(5/9)
conv[("Fahrenheit","Kelvin")] = lambda x: x+459.67
conv[("Fahrenheit","Rankine")] = lambda x: (x-32)*(5/9)
conv[("Kelvin","Celsius")] = lambda x: (x-491.67)*(5/9)
conv[("Kelvin","Fahrenheit")] = lambda x: x-459.67
conv[("Kelvin","Rankine")] = lambda x: x*(5/9)
conv[("Rankine","Celsius")] = lambda x: x-273.15
conv[("Rankine","Fahrenheit")] = lambda x: x*(9/5)-459.67
conv[("Rankine","Kelvine")] = lambda x: x*(9/5)

#Menu
def Menu():
    global Numero
    global l
    error = True
    print("----------------------------------------------")
    print("Bienvenu sur mon convertisseur de temperature")
    print("---------------FDP---------------------------")
    i=1
    l=[]
    for k,v in conv:
        for kk,vv in conv:
            if k!=kk and (k,kk) not in l:
                l.append((k,kk))
                print(f"{i} Pour convertir de {k} à {kk}")
                i+=1
    print("0 Pour quitter")
    while error == True:
        try:
            Numero=int(input("\nQu'as tu décidé de choisir ? "))
            error = False
            assert 0 <= Numero <= 12
        except ValueError:
            print("Woooops tu n'as pas choisie un chiffre")
            error = True
        except AssertionError:
            print("Le chiffre choisie est supperieur a 12 ou inferieur a 0 ")
            error= True
    return Numero
continuer=1
while continuer == 1:
    Menu()
    while Numero != 0:
        error = True
        while error == True:
            try:
                Temperature= int(input("A combien s'eleve votre temperature ? "))
                error = False
            except ValueError:
                print("whoops tu n'as pas choisie un chiffre")
                error = True
        Reponse= conv[l[Numero]](Temperature)
        if Reponse != Temperature:
            print(f"La conversion donne {Reponse}")
            Numero=0
    error2=True
    while error2 == True:
        try:
            continuer = int(input("Voulez vous convertire une autree temperature ? 0 pour Non, 1 Oui "))
            assert 0<=continuer<2
            error2=False
        except ValueError:
            print(":rage: choisie entre 0 pour non et 1 pour oui :rage:")
            error2=True
        except AssertionError:
            print("J'ai dis choisie entre 0 pour non et 1 pour oui :rage::rage::rage::rage:")
            error2=True