def is_palindrome(string):
    reversed_string = string[::-1]
    if reversed_string == string:
        return True
    else:
        return False

string = input()

if is_palindrome(string):
    print("Palindrome")
else:
    print("Not palindrome")
