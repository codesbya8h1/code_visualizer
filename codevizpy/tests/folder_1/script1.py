# script1.py
from script2 import greet_user
from script4 import process_data
from script5 import display_result

def main():
    print("Starting the program...")
    
    # Step 1: Greet the user
    user_name = "Alice"
    greeting = greet_user(user_name)
    print(greeting)
    
    # Step 2: Process some data
    data = [1, 2, 3, 4, 5]
    processed_data = process_data(data)
    print(f"Processed Data: {processed_data}")
    
    # Step 3: Perform final output
    display_result(processed_data)

if __name__ == "__main__":
    main()
