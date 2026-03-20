def validate_data(data):
    if not data.email or "@" not in data.email:
        return False, "Invalid email"
    if not data.content:
        return False, "Content empty"
    return True, "Valid"