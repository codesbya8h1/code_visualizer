class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."

    def get_initials(self):
        return "".join(part[0].upper() for part in self.name.split())

    def is_adult(self):
        return self.age >= 18
def greet(name):
    return f"Hello, {name}!"

def capitalize_words(text):
    return text.title()

def another_random_function():
    pass

def random_function():
    another_random_function()

def count_vowels(string):
    vowels = 'aeiou'
    random_function()
    return sum(1 for char in string.lower() if char in vowels)


def not_main():
    user_name = "alice smith"
    greeting = greet(user_name)
    capitalized_name = capitalize_words(user_name)
    vowel_count = count_vowels(user_name)
    
    print(greeting)
    print(f"Capitalized name: {capitalized_name}")
    print(f"Number of vowels in the name: {vowel_count}")

if __name__ == "__main__":
    not_main()