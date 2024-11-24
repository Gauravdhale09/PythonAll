# palindrome function

def palindrome(string):
    # Remove non-alphanumeric characters and convert to lowercase
    # clean_string = ''.join(e.lower() for e in string if e.isalnum())
    clean_string = string
    # Check if the cleaned string is equal to its reverse
    return clean_string == clean_string[::-1]

# Test the function
x = "madam"
print(f"{x} is a palindrome: {palindrome(x)}")