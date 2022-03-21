# realizzare un programma che date due liste, una di chiavi, una di valori
# crei il dizionario che leghi chiave e valore in stessa posizione

listaChiavi = ['nome', 'cognome', 'età'] #lista delle chiavi
listaValori = ['Mostafa', 'Abou Kelila', 26] #lista dei valori
dizionario = {} #dictionary vuoto

for i in range(len(listaChiavi)): # ciclo per inserire una chiave alla quale corrisponde un valore
    dizionario[listaChiavi[i]] = listaValori[i]

print("dizionario:", dizionario)