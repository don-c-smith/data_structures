"""
This file contains information about and implementations of the 'core' data structures used in data science.
"""

"""
1. LISTS
Lists are generic collections - our 'default' data structure.
In Python, lists are mutable dynamic arrays. They can contain heterogeneous data types.
Appends, pops, access by index, assignment, len(), and 'in' all take constant time. 
Sorting, reversing, concatenation take O(N log N) time. 
Inserts and deletes take linear time since elements must shift.
Iteration, mapping, and reducing also take linear time.
"""
empty_list = []  # Initialize an empty list
my_list = [1, 2, 3, 'Hello']  # Initialize and fill a list
comp_list = [i for i in range(11)]  # List comprehension
nested_list = ['Jack', 'Jill', [1, 2, 3]]  # Lists may be nested

"""
2. TUPLES
Python tuples are immutable sequences that allow constant time access by index. 
Because they are immutable, inserts, deletes, sorts, etc. are not supported. 
Basic operations like len(), slicing, adding, and multiplying also happen in constant time. 
Iteration through elements, mapping, and reducing all take linear time. 
Tuples have a compact memory footprint because they are immutable.
While they are immutable, tuples can contain mutable elements within them.
"""
empty_tuple = ()  # Initialize an empty tuple
my_tuple = (1, 2, 3)  # Initialize and fill a tuple
comp_tuple = (letter for letter in 'Thomas')  # Tuple comprehension
tuple_mutable_elems = ([1, 2, 3], ['Jack', 'Jill'], 7, 'Hello')  # Tuple containing mutable elements

"""
3. DICTIONARIES
Python dictionaries are implemented as hash tables allowing constant time lookups, inserts and deletes.
They are organized in the key-value-pair paradigm. 
Keys must be immutable objects such as strings or tuples. Dictionaries will allow heterogeneous data as values. 
Common operations like accessing values, setting new keys, and checking key existence take constant time. 
Iteration over keys, values or items takes linear time, although order is arbitrary. 
Mapping and filtering also run in linear time.
In Python, collisions are avoided using open addressing.
"""
empty_dict = {}  # Initialize an empty dictionary
my_dict = {1: 'Jack', 2: 'Jill', 3: 'Jim', 4: 'Janet'}  # Initialize and fill a dictionary
# print(my_dict[1])  # Prints value at key position 1
# print(my_dict.keys())  # Prints all keys in dictionary
# print(my_dict.values())  # Prints all keys in dictionary
# print(my_dict.items())  # Prints all K-V pairs in dictionary as tuples
comp_dict = {x: x**2 for x in range(10)}  # Dictionary comprehension

"""
4. SETS
Python sets are implemented as mutable hash tables which allow constant time lookups, inserts and deletes.
Checking membership and existence in sets also takes constant time. 
Sets are unordered and contain *unique,* immutable objects. They are intrinsically deduplicated. 
Common operations like union, intersection, difference run in O(len(set1) + len(set2)) time. 
Iterating over elements in a set take linear time, but order varies. 
Because order varies, sets do not support indexing or slicing. 
"""
empty_set = set()  # Initialize an empty set
my_set_1 = set([1, 2, 3])  # Initialize and fill a set with a function call
my_set_2 = {1, 2, 3}  # Initialize and fill a set with the set literal (Dictionary-type brackets with no K-V pairs)
comp_set = {x**2 for x in range(11)}
# print(comp_set)  # Note that repeated print calls  return different element orders
# You can implement an immutable 'frozen' set using the frozenset() function call
my_frozenset = frozenset([1, 2, 3])  # Initialize and fill a frozenset
