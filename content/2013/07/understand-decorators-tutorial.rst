Understanding decorators
########################
:date: 2013-07-10 20:16
:author: sdonk
:category: Python
:tags: decorator, python
:slug: understand-decorators-tutorial

I've asked a few Python developers to explain and show me what a
decorator is a what it does, surprisingly the answers were uncertain and
confused.

According to the `Python wiki <https://wiki.python.org/moin/PythonDecorators#What_is_a_Python_Decorator>`_,
a decorator allows us to alter functions and methods using a simple syntax.

Technically a decorator is a function that takes a function as argument
and returns a function as result. It's useful to perform some common
tasks across our code that have to be executed before the decorated
function executes itself. Some of these tasks can include:

-  Session and access control (`login\_required Django decorator <https://docs.djangoproject.com/en/dev/topics/auth/default/#the-login-required-decorator>`_)
-  Logging
-  Web access control (think about a is\_ajax decorator for Django
   views)

I have to admit the definition is not very clear so let's see an example
to better understand what a decorator does and when to use it.

Let's say in our development scenario we want to log to the standard
output (the screen) all the arguments and the keyword arguments passed
to the functions. Embedding the logging code into each function would
not only violate the "don't repeat yourself" rule but it will result in
a mess if we want to change this simple logging system at some point. In
that case we would have to go through each single logging embedded code
and change it. A nightmare! This is when a decorator can save your life:

.. code-block:: python

    def log_args(func):
        """
        Print the args of func to the standard output
        """
        def wrapper(*args, **kwargs):
            print args, kwargs
        return wrapper

The decorator *log\_args* is a simple function that takes a function as
single argument (*func*) and returns the function *wrapper* as result.
Before doing it, the function *wrapper* prints the args and the kwargs
(of the decorated function test below!) and print those to the screen.

Let's see how we can use the decorator now:

.. code-block:: python

    @log_args
    def test(arg1, arg2):
        """
        Do nothing, gracefully
        """
        pass

As the Python wiki says, the decorator syntax is easy and it uses the @
symbol to decorate the function *test*.

Let's see the result:

.. code-block:: python

    >>> test('guido', 'linus', style='nerd')

    ('guido', 'linus') {'style': 'nerd'}

We can apply this decorator to as many functions (and methods) we want
across our code, and changing the logging system would be as easy as
changing one single part of our code.
