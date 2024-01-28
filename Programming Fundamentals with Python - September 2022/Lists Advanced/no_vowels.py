text = input()
vowels_lst = ['a', 'o', 'u', 'e', 'i','A','O','U','E','I']

no_vowels = ''.join([char for char in text if char not in vowels_lst])

print(no_vowels)
