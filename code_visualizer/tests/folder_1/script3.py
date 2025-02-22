# script3.py

def capitalize_words(text):
    """
    Capitalizes each word in the given text.
    """
    return " ".join(word.capitalize() for word in text.split())

def count_vowels(text):
    """
    Counts the number of vowels in the given text.
    """
    vowels = "aeiou"
    return sum(1 for char in text.lower() if char in vowels)
