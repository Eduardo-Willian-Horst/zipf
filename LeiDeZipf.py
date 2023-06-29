import re

with open('Texto.txt', 'r', encoding='utf-8') as arquivo:
    texto = arquivo.read()

texto = texto.upper()
texto_limpo = re.sub(r'[^a-zA-Z0-9\s]', '', texto)
words = {}

word = ''

for char in texto_limpo:
    if char != ' ':
        word += char
    else:
        if word != '':
            if word in words:
                words[word] += 1
            else:
                words[word] = 1
            word = ''


if word != '':
    if word in words:
        words[word] += 1
    else:
        words[word] = 1


words_sorted = sorted(words.items(), key=lambda x: x[1], reverse=True)


for key, value in words_sorted:
    print(f'Palavra: {key} - Ocorrências: {value}')
