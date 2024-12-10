pocetna_pozicija = 0 

cilj = 200
trenutna_pozicija = 10
brzina= 12


for x in range(20)

    print(trenutna_pozicija)
    if trenutna_pozicija == cilj:
        print("stigao na cilj")
        break
    elif trenutna_pozicija > cilj:
        print("prosli ste")
    elif trenutna_pozicija < cilj:
        print("niste jos stigli")

    trenutna_pozicija += brzina
