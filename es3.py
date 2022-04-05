# Realizzare un programma che data una lista con valori duplicati crei un dizionario che associ le frequenze di
# occorrenza ad ogni valore della lista

listaDuplcati = [1, 2, 2, 3, 5, 5, 5]
diz = {}
for i in listaDuplcati:
    diz[i] = listaDuplcati.count(i) # conto quante volte compare il numero

print(diz)