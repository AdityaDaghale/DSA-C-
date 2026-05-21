"""String Operations - Palindrome, Anagram, Reversal"""

def is_palindrome(s):
    """Check if string is palindrome"""
    s = s.replace(" ", "").lower()
    return s == s[::-1]

def is_anagram(s1, s2):
    """Check if two strings are anagrams"""
    return sorted(s1.lower()) == sorted(s2.lower())

def reverse_string(s):
    """Reverse a string"""
    return s[::-1]

def count_vowels(s):
    """Count vowels in string"""
    return sum(1 for c in s.lower() if c in 'aeiou')

if __name__ == "__main__":
    print("Is 'racecar' palindrome?", is_palindrome("racecar"))
    print("Are 'listen' and 'silent' anagrams?", is_anagram("listen", "silent"))
    print("Reverse 'hello':", reverse_string("hello"))
    print("Vowels in 'programming':", count_vowels("programming"))
