Base (radix) conversion in Python 
##################################
:date: 2013-08-05 10:43
:author: sdonk
:category: Algorithm, Python
:slug: base-radix-conversion-algorithm

In mathematical numeral systems, the radix or base is the number of
unique digits, including zero, that a positional numeral system uses to
represent numbers. (from `Wikipedia`_)

Converting an integer in base 10 into another base is one of the most
common task asked in skill tests and interviews. Here my solution in
Python:

.. code-block:: python

    import string

    def baseConversion(N, K):
    """
    N and K must be integers
    """
        # create dictionary lookup for reminder>=10
        LETTERS = {i+10: string.lowercase[i] for i in range(26)}
        result = ''
        while N>K:
            reminder = N % K
            N = N / K
            if 36>reminder>9:
                result += LETTERS.get(reminder)
            else:
                result += str(reminder)
        # append the result of the last division
        result += str(N)
        # reverse the string
        return result[::-1]

.. _Wikipedia: https://en.wikipedia.org/wiki/Radix
