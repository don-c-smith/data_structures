"""
This file contains information about and implementations of the more advanced data structures used in data science.
"""

"""
SECTION 1: ADVANCED DICTIONARY SUBCLASSES
"""
from collections import OrderedDict, defaultdict, ChainMap
"""
1A: ORDERED DICTIONARIES
Ordered dictionaries (called with OrderedDict) have the ability to 'remember' the insertion order of keys.
They are not part of base Python and must be imported from the collections library: from collections import OrderedDict

Note that as of Python 3.7, standard dictionaries *do* preserve key insertion order.
However, if key order is important in an implementation, you should communicate that clearly by using an OrderedDict.

OrderedDict instances have a .move_to_end() method that is unavailable on normal dict() instances. 
Additionally, they have a more customizable .popitem() method than normal dict() instances.
"""
empty_ordered_dict = OrderedDict()  # Initializing an empty ordered dictionary
my_ordered_dict_1 = OrderedDict(One=1, Two=2, Three=3)  # Initializing and filling an ordered dictionary directly
# Initializing and filling an ordered dictionary using dict-style assignment syntax
my_ordered_dict_2 = OrderedDict()
my_ordered_dict_2[1] = 'One'
my_ordered_dict_2[2] = 'Two'
my_ordered_dict_2[3] = 'Three'

"""
1B: DEFAULT DICTIONARIES
Default dictionaries accept a 'callable' in their constructor which will return if a requested key cannot be found.

In other words, they allow you to define a default value for non-existent keys using a function.

They are not part of base Python and must be imported from the collections library.

When keys are first accessed, they are inserted with the supplied default value.
These dictionaries obviate the need to check if keys exist already, so you don't need to manually check and initialize.
"""
def default_value():
    """Function which returns 'Not Present.' Used as default value in the default dictionary."""
    return 'Not Present'
my_default_dict = defaultdict(default_value)  # Create a defaultdict with the defined and called default value
# print(my_default_dict['first_key'])  # Prints default value of 'Not Present' rather than a key error
my_default_dict['first_key'] = 'Present'
# print(my_default_dict['first_key'])  # Now that the value has been defined as 'Present,' prints 'Present'

"""
1C: CHAIN MAPS
Using a chain map allows you to group multiple dictionaries into a single mapping.
Lookup calls search the underlying mappings one by one until the specified key is found.

They are not part of base Python and must be imported from the collections library.

NOTE: Insertions, updates, and deletions only affect the *first* mapping added to the chain
"""
dict1 = {'one': 1, 'two': 2}
dict2 = {'three': 3, 'four': 4}
chain_map = ChainMap(dict1, dict2)  # Creating a chain map
# print(chain_map)  # Note that the two dictionaries are mapped together
# You can now search the chained dictionaires for specified keys
# print(chain_map['three'])  # Returns value 3 from second dictionary
# print(chain_map['one'])  # Returns value 1 from first dictionary
# If you search the chained dictionaries for a nonexistent key, a key error will fire
# print(chain_map['Jackrabbit'])

"""
SECTION 2: NAMED TUPLES
Named tuples allow you to define reusable templates which ensure that correct field names are used.

They are not part of base Python and must be imported from the collections library.
Like regular tuples, they are immutable. 

NOTE: You can’t add new fields or modify existing fields after a namedtuple instance is created.

Each object stored in a named tuple can be accessed through a unique identifier. 
This obviates the need to remember integer indexes or use workarounds like defining integer constants as mnemonics.

They can be implemented as "mini classes" in Python without the need to formally define a new custom class
"""
from collections import namedtuple
person_info = namedtuple('Person_Info', 'Name Gender Age')  # Creating the structure of the tuple
jack = person_info('Jack Jackson', 'Male', 35)  # Creating a named tuple instance with provided values
# print(jack)  # Printing the names tuple presents an easily-comprehensible representation of the object
# print(jack.Age)  # And, it's easy to access specific fields within the named tuple object

"""
SECTION 3: STACKS
Stacks are a data structure which maintain the LIFO ('Last-in, first-out') principle.

In other words, the item most recently added to a stack will be the first item returned from the stack.
(Think "a stack of plates.")

To create a 'pure' stack, you need to define a custom class. The core data structure will be a list.

The core methods of the stack are push, pop, top, size, is_empty, and __str__.

Because we append to and pop from the end of the list, this implementation is efficient.
"""
class stack:
    def __init__(self, elements=None):  # Constructor
        if elements is None:  # If no elements were passed
            self.stack = []  # Initialize the stack as an empty list
        else:  # If elements were passed
            self.stack = list(elements)  # Fill the list with those elements

    def push(self, element):  # Define the 'push' method (add to stack)
        self.stack.append(element)

    def pop(self):  # Define the 'pop' method (remove from stack)
        if self.stack:  # If the stack is not empty
            self.stack.pop()  # Pop the most recently added element off the stack

    def top(self):  # Define the 'top' method (return *but do not remove* the top element on the stack)
        if self.stack:  # If the stack is not empty
            return self.stack[-1]  # Return but do not remove the last (top) element

    def size(self):  # Define the 'size' method (how big is the stack)
        return len(self.stack)

    def is_empty(self):  # Define the 'is empty' method (is the stack empty)
        if self.stack:  # If the stack is not empty
            return False # Return False
        else:  # Otherwise, it is empty
            return True  # And we return True

    def __str__(self):  # Define the __str__ method (print current state of the stack as a string)
        return str(self.stack)

test_stack = stack([1, 2, 3, 4, 5])
# print(test_stack.is_empty())
# print(test_stack)
# print(test_stack.top())
# print(test_stack.size())
# test_stack.pop()
# print(test_stack)
# print(test_stack.size())
# test_stack.push(8)
# print(test_stack)
# print(test_stack.size())

"""
SECTION 4: QUEUES
Queues are a data structure which maintain the FIFO ('First-in, first-out') principle.

In other words, the item that was first added to a queue will be the first item returned from the queue.
(Think "a line at a bank.")

To create a 'pure' queue, you need to define a custom class. The core data structure will be a list.

The core methods of the stack are enqueue, dequeue, front, size, is_empty, and __str__.

Because we append to the end of the list but pop from the front of the list, *this implementation is NOT efficient.*
"""
class queue:
    def __init__(self):
        self.queue = []  # Initialize the queue as an empty list

    def enqueue(self, element):
        self.queue.append(element)  # Add an element to the end of the queue

    def dequeue(self):
        if self.queue:
            return self.queue.pop(0)  # Remove and return the first element of the queue
        else:
            return None  # Return None if the queue is empty

    def front(self):
        if self.queue:
            return self.queue[0]  # Return the first element without removing it
        else:
            return None  # Return None if the queue is empty

    def is_empty(self):
        return len(self.queue) == 0  # Return True if the queue is empty, False otherwise

    def size(self):
        return len(self.queue)  # Return the size of the queue

    def __str__(self):  # Define the __str__ method (print current state of the queue as a string)
        return str(self.queue)

"""
SECTION 5: DEQUES (DOUBLE-ENDED QUEUES)
The deque (double-ended queue) data structure, which is part of the collections library, implements a double-ended
queue structure which allows the push and pop methods at *both* ends of the collection to run in constant time.

Using a deque (which is not part of base Python and must be imported from the collections library) allows you to
efficiently implement a queue.
"""
from collections import deque

class my_queue:
    """Implements a FIFO-paradigm queue using a deque as the underlying data structure."""
    def __init__(self, element_type):  # Construct with type declaration
        self.element_type = element_type  # Can be used for 'assert' checks
        self.queue = deque()  # Initialize the queue as an empty deque

    def enqueue(self, element):  # Constructing the 'enqueue' functionality
        assert type(element) == self.element_type  # Assert check for datatype consistency
        self.queue.append(element)  # Define enqueue as adding the value to the end of the queue

    def empty(self):  # Constructing the 'check if empty' functionality
        return len(self.queue) == 0  # The queue is empty if its length is zero. This 'state' can be repeatedly checked

    def dequeue(self):  # Constructing the 'dequeue' functionality
        if not self.empty():  # If the queue is not empty
            return self.queue.popleft()  # Pop the element from the left/'front' of the queue - this is FIFO-compliant

        else:  # Otherwise, if the queue is empty
            raise IndexError('ERROR - Dequeue has been called on an empty queue.')  # Raise an error

    def front(self):  # Constructing the 'front' functionality
        if not self.empty():  # If the queue is not empty
            return self.queue[0]  # Return the element at the 'front' of the queue - this is FIFO-compliant

        else:  # Otherwise, if the queue is empty
            raise IndexError('ERROR - Front has been called on an empty queue.')  # Raise an error

"""
SECTION 6: PRIORITY QUEUES
A priority queue manages a set of records with totally-ordered keys to provide quick access to the record with the 
smallest or largest key in the set.

You can think of a priority queue as a 'modified' queue. Instead of retrieving the next element by insertion time, 
it retrieves the *highest-priority* element. 
The priority of individual elements is decided by the order applied to their keys.

The easiest way to implement a priority queue is with heapq: a binary heap implementation using an ordinary list, 
which supports insertion and extraction of the *smallest* element in O(log n) time. Note that heapq only provides a 
*min-heap* implementation. The heapq implementation is not part of base Python and must be imported.

A more advanced and more stable way is to use the pre-built PriorityQueue structure, imported from the queue library.
This structure uses heapq internally and shares the same time and space complexities. 
The key difference is that PriorityQueue is synchronized, and provides locking semantics to support multiple 
concurrent producers and consumers. 
"""
import heapq
from queue import PriorityQueue

# Starting with a heapq implementation
pri_q_heap = []  # Initialize an empty list
# Push elements into the queue with a priority value
heapq.heappush(pri_q_heap, (2, 'Sleep'))
heapq.heappush(pri_q_heap, (1, 'Eat'))
heapq.heappush(pri_q_heap, (3, 'Work'))
# Observe how the elements pop off
# print(heapq.heappop(pri_q_heap))  # The first element off the queue is the second element pushed onto the queue.
# print(heapq.heappop(pri_q_heap))
# print(heapq.heappop(pri_q_heap))

# Now a PriorityQueue implementation
pri_q_PQ = PriorityQueue()
# Note that this class uses 'put' and not 'push,' but the same outcome occurs
pri_q_PQ.put((2, 'Sleep'))
pri_q_PQ.put((1, 'Eat'))
pri_q_PQ.put((3, 'Work'))
# This class uses get() rather than pop(), but the same outcome occurs
# print(pri_q_PQ.get())  # The first element off the queue is the second element pushed onto the queue.
# print(pri_q_PQ.get())
# print(pri_q_PQ.get())
