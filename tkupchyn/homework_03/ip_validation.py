import re


def is_valid_ip(ip_address: str) -> bool:

    """
    Checks if the given IP address is valid.

    Args:
        ip_address (str): The input string that may contain a mixture of digits and letters.

    Returns:
        bool: True if ip address is valid, False otherwise.
    """

    octets = ip_address.split('.')

    if len(octets) != 4:
        return False

    for octet in octets:
        if not octet.isdigit() or int(octet) not in range(0, 256) or re.match(r'^0\d', octet):
            return False

    return True
