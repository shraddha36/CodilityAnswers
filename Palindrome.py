def palindrome(fd):
    a=fd[::-1]
    if a==fd:
        return True
    return False
print(palindrome("MADAM"))
