def detectCapitalUse(word):
    if word.isupper() or word.islower()or (word[0].isupper() and word[1:].islower()):
        return True
    else:
        return False
print detectCapitalUse("Google")