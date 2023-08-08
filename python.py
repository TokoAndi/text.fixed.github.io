with open("kbbi.txt") as f:
    words = f.read().splitlines()


def find_matches(s):
    matches = []
    for word in words:
        if all(word.count(c) == s.count(c) for c in set(s)) and len(word) <= len(s):
            matches.append(word)
    return matches


while True:
    s = input("Input: ")
    if not s:
        break
    matches = find_matches(s)
    if matches:
        result = ""
        for match in matches:
            if len(match) <= len(s):
                result += match + "\n"
        print(result)
    else:
        print("Tidak ada hasil ditemukan")
