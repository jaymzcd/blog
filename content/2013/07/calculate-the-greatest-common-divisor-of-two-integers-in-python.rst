Calculate the greatest common divisor of two integers in Python
###############################################################
:date: 2013-07-28 10:48
:author: sdonk
:category: Algorithm, Python
:slug: calculate-the-greatest-common-divisor-of-two-integers-in-python

The greatest common divisor of two integers is the largest positive
integer that divides the numbers without a remainder. (from
`Wikipedia`_)

Here my recursive approach in Python:

.. code-block:: python

    def gdc(a,b):
    """
    Return the greatest common divisor between a and b
    a and b are positive integer
    """
        if b is 0:
            return a
        else:
            r = a % b
            if r == 0: #check if there's no remainder
                return b
            else: #if use use that for the next iteration
                gdc(b, r)

.. _Wikipedia: https://en.wikipedia.org/wiki/Greatest_common_divisor
