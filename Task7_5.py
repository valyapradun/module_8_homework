"""
Implement a function to check that number is even (number > 3).
A number should be passed as a string.
Throw different exceptions for different situations.
Custom exceptions must be derived from custom base exception (not Base Exception class).
"""


class CustomException(Exception):
    pass


class ValueTooSmallException(CustomException):
    """Raised when the input value is too small (< 4)"""
    pass


class ValueTooLargeException(CustomException):
    """Raised when the input value is too large (> 100)"""
    pass


class ValueIsOddException(CustomException):
    """Raised when the input value is odd"""
    pass


class ValueIsNotIntException(CustomException):
    """Raised when the input value is not int"""
    pass


def even_number(number: str) -> bool:
    try:
        int_number = int(number)
    except Exception as err:
        raise ValueIsNotIntException(f'Number {number} should be integer') from err

    if int_number < 4:
        raise ValueTooSmallException(f'Number {number} must be greater than 3')

    if int_number > 100:
        raise ValueTooLargeException(f'Number {number} must be less than 100')

    if int_number % 2 == 0:
        return True
    else:
        raise ValueIsOddException(f'Number {number} must be even')


if __name__ == '__main__':
    print(even_number('7'))
    print(even_number('24'))
    print(even_number('0'))
    print(even_number('qwerty'))


