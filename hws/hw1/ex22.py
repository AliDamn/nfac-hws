# 💎 Exercise 22: check-anagrams
#
# Declare 2 strings
# Check if the strings are anagrams (ignoring case)
# Print the result
#
# *Anagram - a word, phrase, or name formed by rearranging the letters of another, such as spar, formed from rasp.

def solution(word1, word2):
    if len(word1) != len(word2):
        return False

    for letter in word1:
        if letter not in word2:
            return False

        word1 = word1.replace(letter, '', 1)
        word2 = word2.replace(letter, '', 1)

    return True

print(solution('lfywlaqpgotebagxokgwflwnhijvmhbsarrqxohpswofzbtyjfxszfbtsmytouybtyuuiydjduqnbngntxoftfjstfgcrcomuzql', 'lfywlaqpgotebagxokgwflwnhijvmhbsarrqxohpswofzbtyjfxszfbtsmytouybtyuuiydjduqnbngntxoftfjstfgcrcomuzqq'))
