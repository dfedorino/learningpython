c = {'a':10, 'b':1, 'c':22}
print( sorted( [ (v, k) for k, v in c.items() ] ) )

# c.items() -> [('a'; 10), ('b'; 1), ('c'; 22)]
# (v, k) for k, v in c.items() -> for k, v in c.items():
#                                      (k, v) = (v, k)
# sorted( [ (v, k) for k, v in c.items() ] ) -> sorts the tuples in the list according to their key value
