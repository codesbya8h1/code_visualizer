# script4.py
from script3 import count_vowels

def process_data(data):
    """
    Processes a list of numbers by calculating their squares and counting vowels in their string representation.
    """
    squared_data = [x**2 for x in data]
    
    # Count vowels in the string representation of squared numbers
    vowel_counts = [count_vowels(str(num)) for num in squared_data]
    
    return {
        "squared": squared_data,
        "vowel_counts": vowel_counts,
        "total_vowels": sum(vowel_counts)
    }
