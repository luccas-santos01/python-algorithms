def is_palindrome_iterative(word):
    if word == "":
        return False
    n = len(word)
    for i in range(n // 2):
        if word[i] != word[n - 1 - i]:
            return False
    return True
