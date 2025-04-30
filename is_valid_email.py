def is_valid_email(email):
    if "@" not in email or email.count("@") != 1:
        return False

    local_part, domain = email.split("@")

    if not local_part or not domain:
        return False

    if "." not in domain:
        return False

    domain_name, *domain_parts = domain.rsplit(".", 1)
    if not domain_name or not domain_parts[0].isalpha():
        return False

    return True


email_input = input("Enter an email address: ")
if is_valid_email(email_input):
    print("Valid email address.")
else:
    print("Invalid email address.")
