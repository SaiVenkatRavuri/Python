s = input("enetr a string:")
vowels = "aeiouAEIOU"
vowel_count = 0
consonant_count = 0
for char in s:
    if 'a' <= char.lower() <= 'z':
        if char in vowels:
            vowel_count += 1
        else:
            consonant_count += 1
print(f"Number of vowels: {vowel_count}")
print(f"Number of consonants: {consonant_count}")
