# crea dictionary
dictionary = {}
print("Dictionary: ", dictionary)

# popola dictionary con chiavi-valori
dictionary = {'marca': 'Fiat', 'modello': 'Punto', 'posti': 4}
print("Dictionary: ", dictionary)

# stampare la marca usando la chiave
print('dictionary[\'marca\']:', dictionary['marca'])

# aggiungere un coppia chiave-valore
dictionary['anno'] = 2003
print("Dictionary: ", dictionary)

# cancellare una coppia chiave-valore
del dictionary['anno']
print("Dictionary: ", dictionary)

# lunghezza dictionary
print("Lunghezza dictionary:", len(dictionary))

# cercare una chiave
print('\'marca\'?', 'marca' in dictionary)

# inserire un dictionary dentro la chiave di un'altro dictionary
dictionary['alimentazione'] = {'primaria': 'benzina', 'secondaria': 'GPL'}
print("Dictionary: ", dictionary)
print('dictionary[\'alimentazione\']:', dictionary['alimentazione'])

# lista di dictionary
listaDictionary = [{
    'macchina': "V15",
    'autista': 'Musta'
},
    {'macchina': 'V25',
     'autista': 'Gibbo'
     }]
print("Lista di dictionary:", listaDictionary)

# stampa ogni dictionary della lista
for dict in listaDictionary:
    print("Dictionary:", dict)

# lista dentro un dictionary
dictionary = {'marca': 'Fiat', 'optional': ['climatizzatore', 'turbo']}
print("Dictionary:", dictionary)
print("Lista interna al dictionary:", dictionary['optional'])

# lista con dentro un dictionary con dentro un'altra lista
listaDictionaryConLista = [{
    'marca': 'Opel',
    'optional': ['clima', 'sedili in pelle']
},
    {'marca': 'Suzuki',
     'optional': ['turbo', 'mod. eco']
     }]
print("Lista con dentro un dictionary con dentro un'altra lista:", listaDictionaryConLista)

# stampa ogni dictionary e lista dentro alla lista
for dizionario in listaDictionaryConLista:
    print("dictionary:", dizionario)
    print('Liste:', dizionario['optional'])
