from murmurhash2 import murmurhash2


def main():
    seed = 1818321529
    
    wish_template = "I wish you a happiest birthday  ~ owo"
    flag_template = "FIA{find_a_secure_hash_function_next_time}"


    # Send birthday wish
    print("Your happy birthday wish:")
    wish = input('> ').strip()

    if not is_leet(wish, wish_template):
        print("Wrong format.")
        exit()

    wish_hash = murmurhash2(wish.encode(), seed)
    print("Hash value:", hex(wish_hash))
    

    # Send flag
    print("Confirm your message:")
    flag = input('> ').strip()

    if not is_leet(flag, flag_template):
        print("Wrong format.")
        exit()

    flag_hash = murmurhash2(flag.encode(), seed)
    print("Hash value:", hex(flag_hash))
    

    # Check hash
    if flag_hash == wish_hash:
        print("Correct!")
        print(flag, "sent to server!")


def is_leet(leet, plain):
    # About leetspeak: https://en.wikipedia.org/wiki/Leet
    
    # Our version of leet
    leet_to_plain = {'4': 'a',
                     '3': 'e',
                     '1': 'i',
                     '0': 'o',
                     '5': 's',
                     '7': 't',
                     'v': 'u'}
    
    translated = leet
    for l, p in leet_to_plain.items():
        translated = translated.replace(l, p)

    return translated == plain


if __name__ == '__main__':
    main()