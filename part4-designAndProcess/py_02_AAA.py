"""
? how to write unit test?
AAA
- arrange
- act
- assert


? test doubles?
link: https://blog.pragmatists.com/test-doubles-fakes-mocks-and-stubs-1a7491dfa3da

## Fake

Fakes are objects that have working implementations, but not same as production one. 
Usually they take some shortcut and have simplified version of production code.

An example of this shortcut, can be an in-memory implementation of Data Access Object or Repository. 
This fake implementation will not engage database, 
but will use a simple collection to store data.

Apart from testing, fake implementation can come handy for prototyping and spikes. 
We can quickly implement and run our system with in-memory store, 
deferring decisions about database design. 

Another example can be also a fake payment system, 
that will always return successful payments.

## Stub

Stub is an object that holds predefined data and uses it to answer calls during tests. 
It is used when we cannot or don’t want to involve objects that 
would answer with real data or have undesirable side effects.

## Mock

Mocks are objects that register calls they receive.
In test assertion we can verify on Mocks that all expected actions were performed.

## TIP

The easiest way to tell we’re dealing with a stub is to notice that the
stub can never fail the test. The asserts the test uses are always against
the class under test.

"""