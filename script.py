import string

translation_dict = {'א': "'", 'ב': 'b', 'ג': 'g', 'ד': 'd', 'ה': 'h', 'ו': 'w',
                    'ז': 'z', 'ח': '.h', 'ט': '.t', 'י': 'y', 'כ': 'k',
                    'ך': 'K', 'ל': 'l', 'מ': 'm', 'ם': 'M', 'נ': 'n', 'ן': 'N',
                    'ס': 's', 'ע': '`', 'פ': 'p', 'ף': 'P', 'צ': '.s',
                    'ץ': '.S', 'ק': 'q', 'ר': 'r', 'ש': '/s', 'ת': 't',
                    ' ': ' ', ',': ',', '.': '.'}

while True:
    inp = input()
    if inp == '':
        break
    translated_string = ''
    for char in inp:
        if char in string.punctuation or char in string.digits:
            translated_string += char
        else:
            translated_string += translation_dict[char]
    print(inp, translated_string, sep='\n', end='\n\n')
