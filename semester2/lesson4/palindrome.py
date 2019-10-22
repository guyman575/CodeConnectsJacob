from stack import Stack
from queue import Queue

# Return true if a string is the same forwards as it is backwards
# Implement using stacks and queues
def isPalindrome(word):
    forward = Queue()
    backward = Stack()
    for letter in word:
        forward.push(letter)
        backward.push(letter)
    for i in range(forward.size()):
        if forward.pop() != backward.pop():
            return False
    return True

# Not palindromes
print(isPalindrome("hello"))
print(isPalindrome("test"))

# Palindromes
print(isPalindrome("racecar"))
print(isPalindrome("a"))
print(isPalindrome("civic"))
print(isPalindrome("able was I ere I saw elba"))

