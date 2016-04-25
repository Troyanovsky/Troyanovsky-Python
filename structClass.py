######################################################
# Structs (save in structClass.py (do not save in struct.py!))
######################################################

# Here we use 'struct' in the classic sense:
#   https://en.wikipedia.org/wiki/Struct_(C_programming_language)

# Note that this is not the same as Python's struct module:
#   https://docs.python.org/3/library/struct.html

class Struct(object):
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def __repr__(self):
        d = self.__dict__
        results = [type(self).__name__ + "("]  # or: self.__class__.__name__
        for key in sorted(d.keys()):
            if (len(results) > 1): results.append(", ")
            results.append(key + "=" + repr(d[key]))
        results.append(")")
        return "".join(results)

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __hash__(self):
        return hash(repr(self)) # inefficient but simple

def testStructClass():
    print("Testing Struct class...", end="")

    obj = Struct()
    obj.x = 42
    assert(obj.x == 42)

    obj = Struct(x=2, b=True, s="abc")
    assert((obj.x == 2) and (obj.b == True) and (obj.s == 'abc'))
    obj.x = 3
    assert(obj.x == 3)
    assert(str(obj) == "Struct(b=True, s='abc', x=3)") # alphabetical keys
    assert(str([obj]) == "[Struct(b=True, s='abc', x=3)]")

    obj2 = eval(repr(obj))
    assert(obj == obj2)
    assert(obj is not obj2) # they are equal, but not aliases

    s = set()
    assert(obj not in s)
    s.add(obj)
    assert(obj in s)
    assert(obj2 in s)       # since (obj == obj2)
    obj.x += 1              # obj is mutable, which is bad, because...
    assert(obj not in s)    # sigh...

    class Person(Struct): pass
    joe = Person(name="Joe", age=42)
    assert(str(joe) == "Person(age=42, name='Joe')")

    assert(type(joe) == Person)
    assert(isinstance(joe, Person) == True)
    assert(isinstance(joe, Struct) == True)
    print("Passed!")

if __name__ == "__main__":
    testStructClass()