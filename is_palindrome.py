def is_palindrome(text):
    cleaned = text.lower().replace(" ", "")
    return cleaned == cleaned[::-1]


word = input("Enter a word or phrase: ")
if is_palindrome(word):
    print("It's a palindrome.")
else:
    print("It's not a palindrome.")
