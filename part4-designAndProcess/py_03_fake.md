# fake

A fake is a generic term that can be used to describe either a stub or a mock
object (handwritten or otherwise), because they both look like the real object.

Whether a fake is a stub or a mock depends on how it’s used in the current
test. 

If it’s used to <font color="blue">check an interaction</font> (asserted against), it’s a <font color="blue">mock object</font>.
Otherwise, it’s a stub.