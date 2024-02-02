def check_ip(ip_address: str) -> bool:
    """
    Validates if given string has valid IPv4 format
    :param ip_address: str to validate
    :return: result of validation True or False
    """
    if type(ip_address) is not str:
        return False
    elif len(ip_address.split('.')) != 4:
        return False
    return all(map(lambda i: -1 < int(i) < 256, ip_address.split('.')))


if __name__ == '__name__':
    # Check yourself""
    assert check_ip('') is False
    assert check_ip('192.168.0.1') is True
    assert check_ip('0.0.0.1') is True
    assert check_ip('10.100.500.32') is False
    assert check_ip(700) is False
    # I corrected the check below since initially it was equal to '127.0.1' that is not valid ip address
    assert check_ip('127.0.0.1') is True
