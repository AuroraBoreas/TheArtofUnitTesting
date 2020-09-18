"""
P75
? concept: stubs
using "stubs" to break dependencies

A stub is a controllable replacement for an existing dependency (or collaborator) in the system. 
By using a stub, you can test your code without dealing with the dependency directly. 

* concepts: test pattern names <<xUnit Test Pattern>>

+---------+-------------------------
| pattern |
+=========+
| fakes   |
+
| stubs   |
+
| mocks   |

? concept: external dependency

An external dependency is an object in your system that your code under
test interacts with, and over which you have no control. 
(Common examples are filesystems, threads, memory, time, and so on.)

? concept: mock 

a plastic knife :^)

? concept: isolation frameworks aka mock framework

? concept: refactoring
refactoring is an act of changing the code's design w/o breaking existing functionality

? concept: seams
seams are places in your code where you can plug in different functionality,
such as stub classes.

"""