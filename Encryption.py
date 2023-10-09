import string

def caesar(text, shift, alphabets):
    
    def shift_alphabet(shift, alphabets):
        shifted_alphabets = []
        for alphabet in alphabets:
            shifted_alphabet = alphabet[shift:] + alphabet[:shift]
            shifted_alphabets.append(shifted_alphabet)
        return tuple(shifted_alphabets)
    
    shifted_alphabets = shift_alphabet(shift, alphabets)
    final_alphabet = ''.join(alphabets)
    final_shifted_alphabet = ''.join(''.join(a) for a in shifted_alphabets)
    table = str.maketrans(final_alphabet, final_shifted_alphabet)
    return text.translate(table)

plain_text = "This is a secret message"
print(caesar(plain_text, 7, [string.ascii_lowercase, string.ascii_uppercase, string.punctuation]))





