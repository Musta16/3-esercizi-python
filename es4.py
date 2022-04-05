# Realizzare un programma “sondaggio” che (i) chieda il nome utente e (ii) ponga una domanda (finchè la risposta
# non è “quit”), registrando la risposta associandola all’utente (e/o viceversa)

print("Benvenuto nel sondaggio di gatti! Scrivere \"Quit\" per uscire")
diz = {}

# ciclo di domande con uscita
while True:
    nome = input("Come ti chiami? ")
    if nome == "Quit" or nome == "quit" or nome == "QUIT":
        break;
    gatto = input("Quale è il tuo gatto preferito? ")
    if gatto == "Quit" or nome == "quit" or nome == "QUIT":
        break;

    diz[nome] = gatto

print("Sondaggio:", diz)

# a. mostrare quanti utenti hanno risposto

print("Hanno riposto in:", len(diz))

# b. mostrare la risposta più frequente

listaValori = list(diz.values())

# ciclo massima frequenza valore in lista
max = 0
for i in listaValori:
    if listaValori.count(i) > max:
        max = listaValori.count(i)
        massimo = i

print("La risposta più frequente è stata:", massimo, "(", max, "volta/e).")

# c. creare un dizionario che associ ad ogni risposta la sua percentuale di frequenza

# ciclo percentuale frequenza ogni elemento in lista
totalePersone = len(diz)
dizFreqPerc = {}
for i in listaValori:
    freqPerc = (listaValori.count(i) / totalePersone) * 100
    if i not in dizFreqPerc:
        dizFreqPerc[i] = freqPerc

print("Dizionario con frequenza riposte:", dizFreqPerc)
