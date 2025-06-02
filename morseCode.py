# Morse Code Translator

MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----',
    ',': '--..--', '.': '.-.-.-', '?': '..--..', '/': '-..-.', '-': '-....-',
    '(': '-.--.', ')': '-.--.-', ' ': '/'
}

# Reverse dictionary for decoding
REVERSE_MORSE_DICT = {v: k for k, v in MORSE_CODE_DICT.items()}


def text_to_morse(text):
    """Convert text to Morse code"""
    morse_code = []
    for char in text.upper():
        if char in MORSE_CODE_DICT:
            morse_code.append(MORSE_CODE_DICT[char])
        else:
            morse_code.append(' ')  # Unknown characters become space
    return ' '.join(morse_code)


def morse_to_text(morse):
    """Convert Morse code to text"""
    text = []
    for code in morse.split(' '):
        if code in REVERSE_MORSE_DICT:
            text.append(REVERSE_MORSE_DICT[code])
        elif code == '':
            text.append(' ')  # Handle multiple spaces
        else:
            text.append('?')  # Unknown Morse code
    return ''.join(text)


def main():
    print("Morse Code Translator")
    while True:
        print("\nOptions:")
        print("1. Text to Morse Code")
        print("2. Morse Code to Text")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            text = input("Enter text to translate to Morse code: ")
            print("Morse Code:", text_to_morse(text))
        elif choice == '2':
            morse = input("Enter Morse code to translate to text (separate letters with spaces, words with '/'): ")
            print("Text:", morse_to_text(morse))
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
