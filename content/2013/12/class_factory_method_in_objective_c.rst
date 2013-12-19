Class factory methods in Objective-C
####################################

:date: 2013-12-02 15:00
:tags: objective-c, ios, xcode
:category: objective-c
:slug: class-factory-methods-objective-c
:author: Alessandro De Noia

In the last couple of weeks I've been playing with Objective-C and Xcode at work. We needed a simple internal iPad app
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


