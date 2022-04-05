# Realizzare un programma “registro” che permetta di manipolare un semplice registro di voti di studenti

# dizionario di tre studenti
s1 = {'Mostafa-AbouKelila': [25, 30, 18]}
s2 = {'Martina-Spaggiari': [29, 27, 22]}
s3 = {'Simone-Farini': [26, 30, 19]}

# registro di dizionari
reg = [s1, s2, s3]

# Menu
while True:
    print("Registro elettronico")
    print("1) Inserisci studente")
    print("2) Aggiungi un voto")
    print("3) Mostra dati")
    print("4) Mostra media-studente")
    print("5) Esci")

    # Prendo la risposta
    while True:  # ciclo di controllo input
        try:
            risp = int(input())
        except ValueError:  # eccezione
            print("Non hai inserito un opzione valida! Ritenta!")
            continue
        except:
            print("Non hai inserito un opzione valida! Ritenta!")
            continue
        if risp > 5 or risp < 1:
            print("Non hai inserito un opzione valida! Ritenta!")
            continue
        else:
            break

    # Smisto la riposta
    # 1) Inserisci studente
    if risp == 1:
        s4 = {}
        nome = input("Inserisci il nome: ")
        cognome = input("Inserisci il cognome: ")
        s4['Nome'] = nome
        s4['Cognome'] = cognome
        print("Hai inserito:", s4)
        reg.append(s4)
        input("Premi un tasto per tornare al Menu..")

    # 2) Aggiungi un voto
    elif risp == 2:
        print("A chi aggiungere un voto?")
        print("1)", s1)
        print("2)", s2)
        print("3)", s3)
        # prendo la riposta
        while True:  # ciclo di controllo input
            try:
                scelta = int(input())
            except ValueError:  # eccezione
                print("Non hai inserito un opzione valida! Ritenta!")
                continue
            except:
                print("Non hai inserito un opzione valida! Ritenta!")
                continue
            if scelta > 3 or scelta < 1:
                print("Non hai inserito un opzione valida! Ritenta!")
                continue
            else:
                break
        # prendo il voto
        while True:  # ciclo di controllo input
            try:
                voto = int(input("Inserire un voto da 18 a 30: "))
            except ValueError:  # eccezione specifica
                print("Non hai inserito un voto valido! Ritenta!")
                continue
            except:  # eccezione generale
                print("Non hai inserito un voto valido! Ritenta!!")
                continue
            else:
                break
        # smisto la riposta e aggiungo il voto
        if scelta == 1:
            s1['Voti'].append(voto)
            print("Lista aggiornata dei voti:", s1['Voti'])
        elif scelta == 2:
            s2['Voti'].append(voto)
            print("Lista aggiornata dei voti:", s2['Voti'])
        else:
            s3['Voti'].append(voto)
            print("Lista aggiornata dei voti:", s3['Voti'])
        input("Premi un tasto per tornare al Menu..")

    # 3) Mostra dati
    elif risp == 3:
        print("Registro studenti:")
        for i in reg:
            print(i)
        input("Premi un tasto per tornare al Menu..")

    # 4) Mostra media-studente
    elif risp == 4:
        print("Di chi vuoi la media voti?")
        print("1)", s1)
        print("2)", s2)
        print("3)", s3)
        # prendo la riposta
        while True:  # ciclo di controllo input
            try:
                scelta = int(input())
            except ValueError:  # eccezione
                print("Non hai inserito un opzione valida! Ritenta!")
                continue
            except:
                print("Non hai inserito un opzione valida! Ritenta!")
                continue
            if scelta > 3 or scelta < 1:
                print("Non hai inserito un opzione valida! Ritenta!")
                continue
            else:
                break
        # smisto la riposta e aggiungo il voto
        if scelta == 1:
            listaVoti = list(s1['Voti'])
            somma = 0
            for i in listaVoti:
                somma = somma + i
            media = somma / len(listaVoti)
            print("media dei voti:", media)
        elif scelta == 2:
            listaVoti = list(s2['Voti'])
            somma = 0
            for i in listaVoti:
                somma = somma + i
            media = somma / len(listaVoti)
            print("media dei voti:", media)
        else:
            listaVoti = list(s3['Voti'])
            somma = 0
            for i in listaVoti:
                somma = somma + i
            media = somma / len(listaVoti)
            print("media dei voti:", media)
        input("Premi un tasto per tornare al Menu..")

    # 5) Esci
    else:
        break