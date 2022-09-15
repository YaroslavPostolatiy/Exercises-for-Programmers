
password = input("password:")

def how_strong(password):
    if is_very_weak(password):
        def is_very_weak(password):
            return len(password) < 8 and password.isnumeric()
        print("very weak")
    elif is_weak(password):
        def has_number(input_string):
            return any(char.isdigit() for char in input_string)
        print("weak")
    elif is_very_strong(password):
        def has_special_characters(input_string):
            return any(not c.isalnum() for c in input_string)
        print("very strong")
    print("strong")


