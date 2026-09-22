def is_valid_number(value):
    """
    Checks whether the entered value contains only
    digits, '-' and '.'.

    Valid examples:
    123
    -123
    12.5
    -12.5
    0.5
    """

    if value == "":
        return True

    # Only digits, '-' and '.' are allowed
    for char in value:
        if char not in "0123456789.-":
            return False

    # '-' can only be at the beginning
    if "-" in value and not value.startswith("-"):
        return False

    # Only one '-' is allowed
    if value.count("-") > 1:
        return False

    # Only one decimal point is allowed
    if value.count(".") > 1:
        return False

    return True