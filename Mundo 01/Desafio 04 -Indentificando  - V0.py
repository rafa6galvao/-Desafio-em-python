import emoji
numero = str(input('Digite uma frase qualquer: '))
en = str.isnumeric(numero)
ealn = str.isalnum(numero)
ealfa = str.isalpha(numero)
eisca = str.isascii(numero)
edec = str.isdecimal(numero)
edig = str. isdigit(numero)
eide = str.isidentifier(numero)
eup = str.isupper(numero)
elo = str.islower(numero)
epr = str.isprintable(numero)
eesp = str.isspace(numero)
eti = str.istitle(numero)
semCor = '\033[m'
verm = '\033[4;31;40m'
verd = '\033[4;30;42m'
azul = '\033[4;30;46m'
preto = '\033[0;30;47m'
tec = emoji.emojize(':keyboard:')
simb = emoji.emojize(':input_symbols:')
num = emoji.emojize(':input_numbers:')
gal = emoji.emojize(':input_latin_uppercase:')
pal = emoji.emojize(':input_latin_lowercase:')
sal = emoji.emojize(':input_latin_letters:')
print('{} é {}númerico:{}{} {}'.format(numero, verm, semCor, num, en))
print('{} é {}alfanumérico:{}{}{} {}'.format(numero, verd, semCor, num, pal, ealn))
print('{} é {}alfabetico:{}{} {}'.format(numero, azul, semCor, gal, ealfa))
print('{} esta {}vazio ou ascaii:{} {}'.format(numero, azul, semCor, eisca))
print('{} é {}decimal:{}{} {}'.format(numero, verd, semCor, num, edec))
print('{} são {}digitos:{}{} {}'.format(numero, verd, semCor, num, edig))
print('{} é {}identificavel:{}{} {}'.format(numero, verm, semCor, simb, eide))
print('{} esta em {}maiusculo:{}{} {}'.format(numero, verd, semCor, gal, eup))
print('{} esta me {}minusculo:{}{} {}'.format(numero, preto, semCor, pal, elo))
print('{} é {}printabel:{}{} {}'.format(numero, verd, semCor, tec, epr,))
print('{} tem {}espaços:{}{} {}'.format(numero, azul, semCor, simb, eesp))
print('{} é {}titlecased:{}{} {}'.format(numero, verd, semCor, sal, eti))

