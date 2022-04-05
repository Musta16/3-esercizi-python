# Realizzare un programma che dati due dizionari ne crei un terzo
# in cui i valori delle chiavi in comune siano fusi in una lista

diz1 = {'marca': 'Fiat', 'anno': 2005}
diz2 = {'marca': 'Opel', 'proprietario': 'Musta'}
diz3 = {}

for chiave1 in diz1: # ciclo ogni chiave dentro il primo diz
    if chiave1 in diz2: #controllo se la chiave è presente anche nel secondo diz
        diz3[chiave1] = [diz1[chiave1], diz2[chiave1]] #se sì, aggiungo i valori dentro una list nel diz3
    else:
        diz3[chiave1] = diz1[chiave1] #se no, aggiungo la coppia chiave-valore nel diz3

for chiave2 in diz2: #ciclo ogni chiave dentro il secondo diz
    if chiave2 not in diz1: #controllo se non è presente nel primo diz
        diz3[chiave2] = diz2[chiave2] #aggiungo come chiave-valore dentro il diz3

print(diz3)