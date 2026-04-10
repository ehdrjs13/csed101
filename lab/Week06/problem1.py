def get_char_count(char:str) -> dict:
    alphabet = []
    count = {}
    for i in char:
        if i not in alphabet:
            alphabet.append(i)
    for s in alphabet:
        count[s] = char.count(s)
    
    return count

if __name__ == "__main__":
    print(get_char_count("HelloWorld"))