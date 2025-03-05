# script5.py

def display_result(processed_data):
    """
    Displays the processed data results.
    """
    print("\n--- Final Results ---")
    
    print("Squared Numbers:")
    print(processed_data["squared"])
    
    print("\nVowel Counts per Number:")
    print(processed_data["vowel_counts"])
    
    print(f"\nTotal Vowels in All Numbers: {processed_data['total_vowels']}")
