s = input("enter a string:")
frequency = {}
for char in s:
    if char in frequency:
        frequency[char] += 1
    else:
        frequency[char] = 1
print(frequency)
