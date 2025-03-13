def date_order_valid(date1, date2):
    """
    Checks if the second date occurs after the first date.

    Args:
        date1 (datetime): The first datetime object.
        date2 (datetime): The second datetime object, expected to be later than date1.

    Returns:
        bool: True if date2 is later than date1, False otherwise.
    """
    valid = False

    if date2 > date1:
        valid = True

    return valid
