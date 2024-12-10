pocetna_pozicija = 0 
cilj = 150
trenutna_pozicija = 0
brzina= 15


for x in range(14): 
    print(trenutna_pozicija)
    if trenutna_pozicija == cilj:
        print("stigao na cilj")
        break
    elif trenutna_pozicija > cilj:
        print("prosli ste")
    elif trenutna_pozicija < cilj:
        print("niste jos stigli")

    trenutna_pozicija += brzina
