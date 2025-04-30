import string

def evaluate_password_strength(password):
    length_ok = len(password) >= 8
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in string.punctuation for c in password)

    if all([length_ok, has_upper, has_lower, has_digit, has_special]):
        return "Strong password"
    elif length_ok and ((has_upper and has_lower) or (has_digit and has_special)):
        return "Moderate password"
    else:
        return "Weak password"

pwd = input("Enter your password: ")
print(evaluate_password_strength(pwd))
