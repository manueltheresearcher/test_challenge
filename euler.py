__author__ = 'cripton'
"""
https://projecteuler.net/problem=1
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
"""

import sys

def sum_multiple(a, b, c):

    total=0
    for i in range(1,c):
        if i % a == 0 or i%b==0:
            total=total+i
    print total

def main():
    # This command-line parsing code is provided.
    # Make a list of command line arguments, omitting the [0] element
    # which is the script itself.
    args = sys.argv[1:]
    if not args:
        print 'usage: num1 num2'
        sys.exit(1)

    if not args[0].isdigit():
        print "error: must specify two numbers"
        print 'usage:  num1 num2'
        sys.exit(1)
    num1=args[0]
    del args[0]
    if not args[0].isdigit():
        print "error: must specify two numbers"
        print 'usage:  num1 num2'

    num2=args[0]

    sum_multiple(int(num1),int(num2),1000)


if __name__ == '__main__':
    main()

