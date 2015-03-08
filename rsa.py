# define base of encrypting
word = 'індеферентність'
alph = 'абвґгдеєжзиіїйклмнорпстуфхцчшщьюя'
p    = 13
q    = 11
d    = 119
e    = 246

# find position of each letter of word in alphabet
position = [alph.find(i)+1 for i in word]