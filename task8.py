__author__ = 'and'
def is_palindrome(wor):
    for i in xrange(len(wor) // 2):
        if wor[i] != word[-i-1]:
            return False
    return True

word = raw_input("Enter:")
z = is_palindrome(word)
print z

print "test"
