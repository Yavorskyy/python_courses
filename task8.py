__author__ = 'andriy'
def is_palindrome(word):
    for i in xrange(len(word) // 2):
        if word[i] != word[-i-1]:
            return False
    return True

word = raw_input("Enter:")
z = is_palindrome(word)
print z
