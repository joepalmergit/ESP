def truncate_price(price):
    """
    Truncates a given price to two decimal places without rounding.

    Parameters:
        price (float): The original price to be truncated.

    Returns:
        float: The truncated price with at most two decimal places.
    """
    return int(price * 100) / 100
