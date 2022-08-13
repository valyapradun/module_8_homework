"""
Create console program for proving Goldbach's conjecture.
Program accepts number for input and print result.
For pressing 'q' program successfully close.
Use function from Task 7.5 for validating input, handle all exceptions and print user friendly output.
"""

from Task7_5 import even_number
import functools
import math


@functools.lru_cache()
def is_prime(number: int) -> bool:
    return math.factorial(number - 1) % number == number - 1


def goldbach(number) -> list:
    if even_number(number):
        int_number = int(number)

        for part1 in range(3, int_number):
            part2 = int_number - part1
            if is_prime(part1) and is_prime(part2):
                return [part1, part2]


def main():
    while True:
        try:
            input_num = input('Enter a number (press "q" to exit): ')
            if input_num == 'q':
                break
            result = goldbach(input_num)
            print('Result: ' + str(result))
        except Exception as exc:
            print(f'{exc.__str__()}\nTry again!\n')


if __name__ == '__main__':
    main()
