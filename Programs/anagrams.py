
def anagrams(string1, string2):
    is_anagram = False
    if len(string1) != len(string2):
        return is_anagram
    string1 = ''.join(sorted(string1.lower()))
    string2 = ''.join(sorted(string2.lower()))
    print(string1, string2)
    if string1 == string2:
        is_anagram = True
    return is_anagram

print(anagrams("gaurav", "vargau"))