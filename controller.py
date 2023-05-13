from view import *


def get_sandwich(amount):
    '''
    This function is to calculate the entry put in for sandwiches and check for the entry to
    be a valid number. Then to return it to view file to be displayed.
    :param amount:
    :return: sandwich_amount
    '''
    try:
        amount = int(amount)
        sandwich_amount = 4 * amount
    except ValueError:
        return print("Entry for sandwiches should be a number")
    return sandwich_amount

def get_cookie(amount):
    '''
    This function is to calculate the entry put in for cookies and check for the entry to
    be a valid number. Then to return it to view file to be displayed.
    :param amount:
    :return:
    '''
    try:
        amount = int(amount)
        cookie_amount = 1.5 * amount
    except TypeError:
        return print("Entry for cookies should be a number")
    return cookie_amount

def get_water(amount):
    try:
        amount = int(amount)
        water_amount = 1 * amount
    except TypeError:
        return print("Entry for water should be a number")
    return water_amount
