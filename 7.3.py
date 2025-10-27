def check_password(password):
    if (len(password) >= 8 and
        any(ch.isupper() for ch in password) and
        any(ch.islower() for ch in password) and
        any(ch.isdigit() for ch in password) and
        any(ch in "!#$%^&*()" for ch in password)):
        return "storng"
    else:
        return "weak"
print(check_password("Abc@1234"))
print(check_password("abcd1234"))
