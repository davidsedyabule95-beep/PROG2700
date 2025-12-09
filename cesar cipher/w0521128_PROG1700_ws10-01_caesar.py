

import os
import csv
from datetime import datetime


def demo_alphabet_index_method():
    alphabet = " abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
    text = input("[DEMO] Enter text (lowercase only, spaces allowed): ").strip().lower()
    key = int(input("[DEMO] Enter key (1–26): "))

    keyword = []

    if 0 < key <= 26:
        for letter in text:
            get_letter = alphabet.index(letter) + key
            keyword.append(alphabet[get_letter])
        print("[DEMO] Encrypted (alphabet/index method):", "".join(keyword))
    else:
        print("[DEMO] Key must be between 1 and 26.")




def encrypt_char(ch: str, step: int) -> str:
    # lowercase
    if 'a' <= ch <= 'z':
        base = ord('a')
        offset = ord(ch) - base
        new_offset = (offset + step) % 26
        return chr(base + new_offset)

    # uppercase
    elif 'A' <= ch <= 'Z':
        base = ord('A')
        offset = ord(ch) - base
        new_offset = (offset + step) % 26
        return chr(base + new_offset)

    # punctuation / digits / spaces remain unchanged
    return ch


def encrypt_text(plaintext: str, step: int) -> str:
    ciphertext = ""
    for ch in plaintext:
        ciphertext += encrypt_char(ch, step)
    return ciphertext


def decrypt_char(ch: str, step: int) -> str:
    # lowercase
    if 'a' <= ch <= 'z':
        base = ord('a')
        offset = ord(ch) - base
        new_offset = (offset - step) % 26
        return chr(base + new_offset)

    # uppercase
    elif 'A' <= ch <= 'Z':
        base = ord('A')
        offset = ord(ch) - base
        new_offset = (offset - step) % 26
        return chr(base + new_offset)

    return ch


def decrypt_text(ciphertext: str, step: int) -> str:
    decrypted = ""
    for ch in ciphertext:
        decrypted += decrypt_char(ch, step)
    return decrypted




def read_file_to_string(filename: str) -> str:
    try:
        with open(filename, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        print(f"ERROR: File '{filename}' not found.")
        return ""


def write_string_to_file(filename: str, content: str) -> None:
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)




def load_dictionary(filename: str) -> set:
    words = set()
    try:
        with open(filename, "r", encoding="utf-8") as f:
            for line in f:
                word = line.strip().lower()
                if word != "":
                    words.add(word)
    except FileNotFoundError:
        print(f"Dictionary file '{filename}' not found.")
    return words


def brute_force_decrypt(ciphertext: str, dictionary_words: set) -> None:

    best_match_count = 0
    best_step = None
    best_text = ""

    for s in range(1, 26):
        candidate = decrypt_text(ciphertext, s)

        # Clean punctuation for comparison
        words = [w.strip(",.!?;:'\"").lower() for w in candidate.split()]

        count = sum(1 for w in words if w in dictionary_words)

        if count > best_match_count:
            best_match_count = count
            best_step = s
            best_text = candidate

    print("\n===== BEST BRUTE-FORCE RESULT =====")
    if best_step is None:
        print("No likely match found. Dictionary may be too small.")
    else:
        print(f"Best step guess: {best_step}")
        print("Decrypted text sample:")
        print(best_text)




def main():
    print("PROG1700 – Workshop 10 Activity 01: Caesar Cipher\n")

    print("\n=== PART 1: ENCRYPTION ===")
    step = int(input("Enter shift value (1–26): "))

    plaintext = read_file_to_string("plaintext.txt")
    ciphertext = encrypt_text(plaintext, step)
    write_string_to_file("ciphertext.txt", ciphertext)

    print("Encryption complete → ciphertext.txt")

    print("\n=== PART 2: DECRYPTION ===")
    cipher_in = read_file_to_string("ciphertext.txt")
    decrypted = decrypt_text(cipher_in, step)
    write_string_to_file("decrypted_known_step.txt", decrypted)

    print("Decryption complete → decrypted_known_step.txt")

    print("\n=== PART 3: BRUTE FORCE (OPTIONAL) ===")
    choice = input("Try brute-force decryption? (y/n): ").lower()

    if choice == "y":
        dictionary_words = load_dictionary("dictionary.txt")
        brute_force_decrypt(cipher_in, dictionary_words)

    print("\nActivity complete — answer reflection questions at bottom.\n")


if __name__ == "__main__":
    main()



#  Reflection


# 1. In plain language, what is the difference between encryption and decryption?
#    Encryption scrambles readable text into unreadable text. Decryption reverses it.

# 2. Why is Method B (ord/chr) generally superior to the alphabet-index approach?
#    It works for uppercase, lowercase, punctuation, and does not crash on unknown characters.

# 3. What kinds of characters does your script preserve correctly?
#    Spaces, numbers, punctuation, symbols — anything not a letter.

# 4. How might a brute-force attack break a Caesar cipher easily?
#    There are only 25 possible shifts, so a computer can try all quickly.

# 5. What part of this activity helped you understand text processing the most?
#    Handling each character individually and working with files.
