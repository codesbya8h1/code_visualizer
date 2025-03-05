# script2.py
from script3 import capitalize_words

def greet_user(name):
    """
    Greets the user with a capitalized name.
    """
    capitalized_name = capitalize_words(name)
    return f"Hello, {capitalized_name}!"
