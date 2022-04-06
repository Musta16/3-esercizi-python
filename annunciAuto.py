listaAnnunci = []

while True:
    print("Benvenuto su annunci.it\n i) Inserire nuovo annuncio\n q) Cerca annuncio\n x) Esci")
    cmd = input("Inserisci \"i\" o \"q\" o \"x\" per uscire: ")
    if cmd == "i" or cmd == 'I':
        prod = input("Nome produttore:")
        mod = input("Modello:")
        prez = int(input("Prezzo:"))
        descr = input("Descrizone vendita:")
        listaAnnunci.append({'Produttore': prod, 'Modello': mod, 'Prezzo': prez, 'Descrizione': descr})
        print(listaAnnunci)
    elif cmd == 'q' or cmd == 'Q':
        if len(listaAnnunci) == 0:
            print("Errore! Devi prima inserire un annuncio!")
            continue
        else:
            print("Ricerca in base a:\n a) Produttore\n b) Modello\n c) Prezzo")
            cmd2 = input("Inserisci \"a\" o \"b\" o \"c\": ")
            if cmd2 == 'a' or cmd2 == 'A':
                filtro_produttore = input("Nome produttore:")
                for i in listaAnnunci:
                    if i.get('Produttore') == filtro_produttore:
                        print(i)
            elif cmd2 == 'b' or cmd2 == 'B':
                filtro_modello = input("Nome modello:")
                for i in listaAnnunci:
                    if filtro_modello == i.get('Modello'):
                        print(i)
            elif cmd2 == 'c' or cmd2 == 'C':
                filtro_prezzo = input("Nome prezzo:")
                for i in listaAnnunci:
                    if i.get('Modello') == filtro_prezzo:
                        print(i)
            else:
                print("Non hai inserito un valore corretto!")
                continue
    else:
        break
