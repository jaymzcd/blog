Data structures in Python part 1
################################

:date: 2014-01-07 10:00
:tags: python, data structures
:category: python
:slug: data-structures-in-python-part-1
:author: Alessandro De Noia

Stack
-----

A stack is an **ordered LIFO** (Last In First Out) type of data structure, that can have a limited capacity.
As the name suggests, all the new items are added and remove to and from the top of the stack.

The operations allowed on it are:

**push**
    Adds an element to the top of the stack

**pop**
    Removes the top element of the stack

**peek**
    Returns, but not removes, the top element of the stack

Here a simple implementation using the lists:

.. code-block:: python

    class Stack(object):
        """
        Implements a stack type data structure
        """

        def __init__(self):
            self.items = []

        @property
        def is_empty(self):
            """
            Tests to see whether the stack is empty
            """
            return self.items == []

        @property
        def size(self):
            """
            Returns the number of items on the stack
            """
            return len(self.items)

        def push(self, item):
            """
            Adds a new item to the top of the stack
            """
            self.items.append(item)

        def pop(self):
            """
            Removes and returns the top item from the stack
            """
            try:
                return self.items.pop()
            except IndexError:
                raise Exception('The stack is empty')

        def peek(self):
            """
            Returns the top item from the stack but does not remove it
            """
            try:
                return self.items[-1]
            except IndexError:
                raise Exception('The stack is empty')


Queue
-----

A queue is an **ordered FIFO** (First In, First Out) type of data structure.
The elements are appended to one end of the queue, the *rear*, and they are remove from the other end, the *front*.

The operations allowed are:

**enqueue**
    Appends an element to the rear of the queue

**dequeue**
    Removes and returns the front element from the queue

Below a Python implementation using the lists:

.. code-block:: python

    class Queue(object):
        """
        Implements a queue type data structure
        """

        def __init__(self):
            self.items = []

        @property
        def is_empty(self):
            """
            Tests to see whether the queue is empty
            """
            return self.items == []

        @property
        def size(self):
            """
            Returns the number of items on the stack
            """
            return len(self.items)

        def enqueue(self, item):
            """
            Adds a new item to the rear of the queue
            """
            self.items.index(0, item)

        def dequeue(self):
            """
            Removes and returns the front item from the queue
            """
            try:
                self.items.pop()
            except IndexError:
                raise Exception('The queue is empty')

