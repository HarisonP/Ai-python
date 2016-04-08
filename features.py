special_english_sounds = ['mm', 'nn', 'rr','ll','dth','tt', 'ri', 'ch', 'sh', 'th', 'wh' ,
'ng', 'nk', 'oi', 'ow', 'oo','ur' , 'ar' , 'or'
'aw' 'zh', 'gl', 'pl', 'br', 'cr', 'dr', 'fr',
'gr', 'pr', 'tr', 'sk', 'sl', 'sp', 'st', 'sw' , 'spr' , 'str']
vowels = ['a', 'e', 'i', 'o', 'u']

def postions_with_charcode(features, name):
    features += [0] * 27
    for position, char_code in enumerate([ord(char) - 96 for char in name]):
        if char_code < 0:
            char_code = 0
        features[char_code] += (position + 1) * char_code

def is_last_letter(features, name, letter):
    features.append((1 if name[-1] == letter else 0))

def has_pair_letters(features, name, pair):
    features.append((1 if pair in name else 0))


def number_of_vowels(features, name):
    features.append(len(filter(lambda char: char in vowels, list(name))))

def ends_with_vowels(features, name):
    features.append(name[-1] in ['a', 'e', 'i', 'o', 'u'])

def starts_with_vovel(features, name):
    features.append(name[0] in ['a', 'e', 'i', 'o', 'u'])

def number_of_double_letters(features, name):
    features.append(0)
    name_as_list = list(name)
    for index, char in enumerate(name_as_list):
        if index > 0 and char == name_as_list[index - 1]:
            features[-1] += 1

def vowels_to_nonvowels(features, name):
    number_of_vowels = len(filter(lambda char: char in vowels, list(name)))
    features.append( float(number_of_vowels) / len(name))

def name_size(features, name):
    features.append(len(name))

def translate_name_in_array(name):
    name = name[0:-1]
    features = []
    postions_with_charcode(features, name)

    is_last_letter(features, name, 'a')
    is_last_letter(features, name, 'n')
    # is_last_letter(features, name, 'g')
    is_last_letter(features, name, 'l')
    # is_last_letter(features, name, 'z')

    ends_with_vowels(features, name)
    starts_with_vovel(features, name)
    number_of_double_letters(features, name)

    has_pair_letters(features, name, 'ie')
    for sound in special_english_sounds:
        has_pair_letters(features, name, sound)

    # vowels_to_nonvowels(features, name)
    # name_size(features, name)
    number_of_vowels(features, name)
    return features

def translate_name_in_array_1(name):
    name = name[0:-1]
    features = [0] * 15
    for position, char_code in enumerate([ord(char) - 96 for char in name]):
        if char_code < 0:
            char_code = 0
        features[position] = char_code

    is_last_letter(features, name, 'a')
    is_last_letter(features, name, 'n')

    ends_with_vowels(features, name)

    starts_with_vovel(features, name)
    number_of_double_letters(features, name)
    # vowels_to_nonvowels(features, name)
    # name_size(features, name)
    # number_of_vowels(features, name)
    return features
