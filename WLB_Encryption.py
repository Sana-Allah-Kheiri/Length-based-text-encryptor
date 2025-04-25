def left_shift_word(word, n):
    if len(word) <= 1 or not word.isalpha():
        return word
    n = n % len(word)  # Ensure n is within word length
    return word[n:] + word[:n]

def encrypt_word(word):
    alpha_only = ''.join(filter(str.isalpha, word))
    length = len(alpha_only)

    if length == 1:
        shift = 0
    elif length == 2:
        shift = 1
    elif length == 3:
        shift = 2
    elif length == 4:
        shift = 1
    else:
        shift = 3

    return left_shift_word(word, shift)

def encrypt_text(text):
    words = text.split()
    encrypted_words = [encrypt_word(word) for word in words]
    return ' '.join(encrypted_words)

def main():
    print("--- Custom Encryption Program ---")
    text = input("Enter the plain text: ")
    encrypted = encrypt_text(text)
    print("Encrypted text:", encrypted)

if __name__ == "__main__":
    main()