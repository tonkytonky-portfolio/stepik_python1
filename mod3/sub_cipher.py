alphabet, cipher, encode, decode = input(), input(), input(), input()

# Create encode and decode dictionaries
enc_dict = {letter: char for letter, char in zip(alphabet, cipher)}
dec_dict = {char: letter for char, letter in zip(cipher, alphabet)}

# Pull each letter or char through the dictionary to encode or decode it
print("".join([enc_dict[letter] for letter in encode]))
print("".join([dec_dict[char] for char in decode]))
