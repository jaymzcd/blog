Class factory methods in Objective-C
####################################

:date: 2013-12-02 15:00
:tags: objective-c, ios, xcode
:category: objective-c
:slug: class-factory-methods-objective-c
:author: Alessandro De Noia

In the last couple of weeks I've been playing with Objective-C and Xcode at work. We needed a simple internal iPad app.
Coming from Python it took me a couple of hours to grasp the concepts of interface and implementation.
Create an object in Python is very easy and straightforward, for example the object Person (with two properties: name and surname)
would look like this:

.. code-block:: python

class Person(object):

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

Objective-C (and C) has a different way of doing it. We need to create an interface for the class first and then write
the correspondent implementation.
In the interface, as the name suggests, the public methods and properties are declared. In simple words, it's the place
where the public "bits" of the class are exposed to external world.
The implementation is the place where to put the actual code for the properties and methods declared in the interface,
hence the name.

Our person class would then look like this:

**interface**

.. code-block:: objective-c

    //  Person.h

    #import <Foundation/Foundation.h>

    @interface Person : NSObject {

    }

    @property (nonatomic, copy) NSString* name;
    @property (nonatomic, copy) NSString* surname;

    @end


** implementation**

.. code-block:: objective-c

    // Person.m

    #import "Person.h"

    @implementation Person

    @synthesize name = _name;
    @synthesize surname = _surname;

    @end

The properties name and surname are declared in the interface file, while in the implementation file the statement
synthesize automatically creates the setter and getter for a property.

It would be great to have a class method that can initiate the class as well as set the values of the two property.
We need to write a class factory!

**interface**

.. code-block:: objective-c

    //  Person.h

    #import <Foundation/Foundation.h>

    @interface Person : NSObject {

    }

    @property (nonatomic, copy) NSString* name;
    @property (nonatomic, copy) NSString* surname;

    + (Person*)personWithName:(NSString*)aName withSurname:(NSString*)aSurname;

    - (id)initPersonWithName:(NSString*)aName withSurname:(NSString*)aSurname;

    @end

The plus sign (+) in front of the method *personWithName* defines a class method, a special method that can be called
on the class itself and not on its instance.

** implementation**

.. code-block:: objective-c

    // Person.m

    #import "Person.h"

    @implementation Person

    @synthesize name = _name;
    @synthesize surname = _surname;

    + (Person*)personWithName:(NSString *)aName withSurname:(NSString *)aSurname {
        return [[Person alloc] initPersonWithName:aName withSurname:aSurname];
    }

    - (id)initPersonName:(NSString *)aName withSurname:(NSString *)aSurname {
        self = [super init];
        if (self) {
            _name = [aName copy];
            _surname = [aSurname copy];
        }
        return self;
    }

    @end



The code