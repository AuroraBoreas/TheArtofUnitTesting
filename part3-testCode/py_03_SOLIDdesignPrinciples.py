"""

A good place to look at design objectives that adhere more to the idea of testable design is 
Bob Martin’s timeless SOLID design series of articles. 

SOLID stands for 
- Single Responsibility Principle
- Open Closed Principle
- Liskov Substitution Principle
- Interface Segregation Principle
- Dependency Inversion Principles 

These principles can be found at http://butunclebob.com/ArticleS.UncleBob.PrinciplesOfOod.

Table: class design principles
+-----+-------------------------------------+-------------------------------------------------------------------+
| SRP | the single responsibility principle | a class should have one, and only one, reason to change           |
+-----+-------------------------------------+-------------------------------------------------------------------+
| OCP | the open closed principle           | u should be able to extend a classes behavior, w/o modifying it   |
+-----+-------------------------------------+-------------------------------------------------------------------+
| LSP | the Liskov substitution principle   | derived classes must be substitutable for their base classes      |
+-----+-------------------------------------+-------------------------------------------------------------------+
| ISP | the interface segregation principle | make fine-grained interfaces that are client specific             |
+-----+-------------------------------------+-------------------------------------------------------------------+
| DIP | the dependency inversion principle  | depend on abstractions, not on concretions                        |
+-----+-------------------------------------+-------------------------------------------------------------------+

Table: package principles, "cohesion"
+-----+-----------------------------------------+------------------------------------------------------+
| REP | the release reuse equivalency principle | the granule of reuse is the granule of release       |
+-----+-----------------------------------------+------------------------------------------------------+
| CCP | the common closure principle            | classes that change together are packaged together   |
+-----+-----------------------------------------+------------------------------------------------------+
| CRP | the common reuse principle              | classes that are used together are packaged together |
+-----+-----------------------------------------+------------------------------------------------------+

Table: package principles, "couplings btwn pkgs" 
+-----+------------------------------------------+------------------------------------------------------+
| ADP | the acyclic dependencies principle       | the dependency graph of packages must have no cycles |
+-----+------------------------------------------+------------------------------------------------------+
| SDP | the stable dependencies principle        | depend in the direction of stability                 |
+-----+------------------------------------------+------------------------------------------------------+
| SAP | the stable abstractions principle        | abstractness increases with stability                |
+-----+------------------------------------------+------------------------------------------------------+

"""