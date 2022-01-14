import sys
import hashlib

crack_hash = sys.argv[1]

if sys.argv[2].upper():
    wordlist = sys.argv[3]
    with open(wordlist, 'r', encoding='latin-1') as file:
        for word in file.readlines():
            hash_word = hashlib.new(sys.argv[2].lower())
            hash_word.update(word.strip().encode("utf-8"))
            if hash_word.hexdigest() == crack_hash:
                print(f"Password Found: {word}")
                break
