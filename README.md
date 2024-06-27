Python pills
============
Copyright (C) 2023 Michele Welponer
- [Overview](#overview)
  * [print](#print)
  * [Syntax](#syntax)
    + [if statement](#if-statement)
    + [loops](#loops)
  * [string](#string)
  * [Functions](#functions)
    + [pass by object reference](#pass-by-object-reference)
    + [nested Functions](#nested-functions)
    + [non-local variable declaration](#non-local-variable-declaration)
    + [decorators](#decorators)
    + [generators](#generators)
    + [lambda function](#lambda-function)
    + [map function](#map-function)
    + [function parameters type annotations](#function-parameters-type-annotations)
    + [timeit](#timeit)
  * [Classes](#classes)
    + [Inheritance and override](#inheritance-and-override)
    + [iterable and iterator](#iterable-and-iterator)
    + [abstract classes](#abstract-classes)
  * [Enumerations](#enumerations)
- [Data Structures](#data-structures)
  * [Array](#array)
  * [Stack](#stack)
  * [Queue](#queue)
  * [Hashset](#hashset)
  * [Hashmap](#hashmap)
    + [defaultdict](#defaultdict)
    + [counter](#counter)
  * [Tuple](#tuple)
    + [namedtuple](#namedtuple)
  * [Priority queue](#priority-queue)
    + [minheap](#minheap)
    + [maxheap](#maxheap)
    + [heapify](#heapify)
    + [heap of lists](#heap-of-lists)
- [Custom Data Structures](#custom-data-structures)
  * [Liked list](#liked-list)
  * [Binary tree](#binary-tree)
    + [Bredth first search BSF](#bredth-first-search-bsf)
    + [Depth first search DSF](#depth-first-search-dsf)
    + [recursive DFS](#recursive-dfs)
  * [Trie or Prefix tree](#trie-or-prefix-tree)
  * [Graphs](#graphs)
    + [graph algoritms](#graph-algoritms)
- [Math](#math)
  * [min max](#min-max)
  * [math problems](#math-problems)
    + [factorial](#factorial)
    + [prime number](#prime-number)
    + [great common divisor GCD](#great-common-divisor-gcd)
    + [least common multiple LCM](#least-common-multiple-lcm)
    + [fibonacci](#fibonacci)
    + [Newton square root of a number](#newton-square-root-of-a-number)
- [Numpy](#numpy)
  * [initialization](#initialization)
  * [shape reshape flatten copy](#shape-reshape-flatten-copy)
  * [concatenate stack split](#concatenate-stack-split)
  * [search filter](#search-filter)
  * [sorting](#sorting)
  * [operations](#operations)
- [Matrix linear algebra](#matrix-linear-algebra)
  * [sum](#sum)
  * [inner product](#inner-product)
    + [dot product](#dot-product)
    + [matmul](#matmul)
  * [outer product](#outer-product)
- [Pandas](#pandas)
  * [Series](#series)
  * [dataframe](#dataframe)
  * [info](#info)
  * [retrieving data](#retrieving-data)
  * [analyzing data](#analyzing-data)
    + [some statistic](#some-statistic)
  * [cleaning data](#cleaning-data)
  * [correlation and plot](#correlation-and-plot)
    + [plot all columns](#plot-all-columns)
    + [plot x y](#plot-x-y)
    + [plot histogram](#plot-histogram)
- [Standard input](#standard-input)
- [Input file stream](#input-file-stream)
  * [reading a file](#reading-a-file)
  * [writing a file](#writing-a-file)
- [Try except raise](#try-except-raise)
- [Concurrency vs Parallelism](#concurrency-vs-parallelism)
  * [multi threading](#multi-threading)
  * [multi processing](#multi-processing)
  * [map reduce](#map-reduce)
- [Other](#other)
  * [binary representation](#binary-representation)
    + [tricks](#tricks)
  * [binary search](#binary-search)

<small><i><a href='http://ecotrust-canada.github.io/markdown-toc/'>Table of contents generated with markdown-toc</a></i></small>


# Overview

## print

```python
name = "Alice"
age = 45
balance = 5.61743
mydict = {'name':'Alice', 'age':35}
print( "Hello, " + name +  "!") # >>> Hello, Alice!
print( "Hello,", name, "!") # >>> Hello, Alice !

##### f-string 
print( f"Hello, {name}, I am {age}!")
f"result: {[n for n in range(5)]}" # expression >>> result: [0, 1, 2, 3, 4]
f"Balance: ${balance:.2f}" # precision >>> Balance: 5.62
f"{name:=^10}" # fill with = string lenght 10 center with ^ >>> ==Alice===
f"thousand separators: {1000000:,}" # >>> thousand separators: 1,000,000
f"separators + 2decimals: {1234567.9876:,.2f}" # >>> separators + 2decimals: 1,234,567.99

##### .format()
print( "Hi {}, I am {}!".format(name, age)) # >>> Hi Alice, I am 45!
"Hi {1}! {0} years old.".format(age, name) # {index} >>> Hi Alice! 45 years old.
"{1} is {0}. I said {0}!".format(age, name) # >>> Alice is 45. I said 45! 
"Hi {name}, I am {age}!".format(**mydict) # using ** dictionary unpacking 
"Balance: ${:.2f}".format(5.9292) # precision {index:.decimalstype} >>> Balance: 5.93
"{:=^10}".format("Mike") # centers Mike in 10 spaces using = as filler >>> ===Mike===

##### modulo %
print( "Hello, %s!" % name) # %s converts name to string >>> Hello Alice!
"%(name)s is %(age)s." % {'name': 'Jane', 'age':25} # using dictionary >>> Jane is 25.
"Balance: $%.2f" % 5.9292 # precision >>> Balance: 5.93

##### usefull print arguments
print('a', 'b', 'c', sep='/') # >>> /a/b/c
print(name, end='.\n') # >>> Alice.
```

## Syntax

```python
# WRITING ON MULTIPLE LINES
print("one, " + "two, " \
	+ "three, " + "four, " \
	+ "five.")
if ( n > 2 and
	n < 10): print("ciao")

# MULTIPLE ASSIGNMENTS
n, m = 0, "abc" # n = 0 and m = "abc"

# INCREMENTING A VARIABLE
n = n + 1
n += 1
# n++  NO!

# GET THE UNIQUE ID ASSIGNED TO AN OBJECT
var = 5
print(var, "has id:", id(var)) # >>> 5 has id: 4527716784
```

### if statement

```python
if n > 2:
	print("more than 2")
elif n == 2:
	print("2")
else: print("less then 2")
```

### loops

```python
while n > 0: 
	print(n)
	n -= 1

for i in range(0, 5): # >>> 0, 1, 2, 3, 4
for i in range(5) # >>> 0, 1, 2, 3, 4
for i in range(0, 5, 2) # from 0 to 5 excluded, step 2 >>> 0, 2, 4
for _ in range(n): # _ indicates a throwaway variable, it won't be used
```

## string

```python
s = 'a$b$c'
arr = ["ab", "cd", "ef"]

s1 = f'{s}$d' # >>> 'a$b$c$d'

s[0:3] # substring >>> a$b
s[:3] # substring >>> a$b
s[2:5] # substring >>> b$c
s[2:] # substring >>> b$c 
s[::-1] # reverse string >>> "c$b$a"
s += "def" # a new string will be created >>> a$b$cdef

int('123') + int('123') # string to int >>> 246
str(123) + str(123) # int to string >>> 123123
ord("a") # char to ascii code >>> 97
chr(97) # ascii code to ascii value >>> a

'A'.lower() # char string to lowercase >>> a
'a'.upper() # char string to uppercase >>> A

import string
string.ascii_lowercase # lowercase alphabet >>> abcdefghijklmnopqrstuvwxyz
string.ascii_uppercase # uppercase alfabet >>> ABCDEFGHIJKLMNOPQRSTUVWXYZ

"?".join(arr) # join list elements with separator >>> ab?cd?ef
s.split('$') # split string >>> ['a', 'b', 'c']
s.partition('$') # partition string >>> ('a', 'b', 'c')
list(s) # string to list >>> ['a', '$', 'b', '$', 'c']

s.find('b$') # first occurence of b$, -1 if not found >>> 2

import re
[m.start() for m in re.finditer('$', s)] # find all occurences of $ >>> [1, 3]
# OR using list comprehension
[i for i in range(len(s)) if s[i] == '$'] # list comprehension >>> [1, 3]
```

## Functions

```python
def myFunc(n, m):
	return n * m
	
myFunc(3, 4) # >>> 12

#### function stub
def myfunction():  
	pass # placeholder for future code
```

### pass by object reference

Python’s argument-passing model is neither “*Pass by Value*” nor “*Pass by Reference*” but it is “**Pass by Object Reference**”. 
Depending on the type of object you pass in the function, the function behaves differently. Immutable objects show “pass by value” whereas mutable objects show “pass by reference”.

```python
def func(va, tu, li):
    va = 666 # variable
    tu = (666, 1, 2) # tuple
    li[0] = 666 # list
    
v = 0 # integer is an immutable object!
t = (0, 1, 2) # tuple is an immutable object!
l = [0, 1, 2] # list is a mutable object!

print(v, t, l) # >>> 0 (0, 1, 2) [0, 1, 2]
func(v, t, l)
print(v, t, l) # >>> 0 (0, 1, 2) [666, 1, 2]
```

### nested Functions

```python
def outer(a, b):
	c = "c"

	def inner():
		# this inner function has access to
		# all of the declared variables
		return a + b + c
	return inner()

outer("a", "b") # >>> 'abc'
```

### non-local variable declaration

```python
def outer(v1,v2):
    def helper():
        v1 = 6 # this declares another v1 variable work!
        nonlocal v2 # makes al v2 accessible and editable
        v2 = 3
        print('inside helper', v1, v2)

    helper()
    print('outside helper', v1, v2)

outer(0, 0) 
# >>> inside helper 6 3
# >>> outside helper 0 3
```

### decorators

Decorators allow us to wrap another function in order to extend the behaviour of the wrapped function, without permanently modifying it.

declare a decorator to execute a function, calculate and print the duration of the function

```python
import time
import math

def calculate_time(func):
	# if function takes any arguments, can be added like this
	def inner1(*args, **kwargs):
        begin = time.time()
        func(*args, **kwargs) # pass arguments to the function
        end = time.time()
        print("Time taken:", func.__name__, end - begin)
 
    return inner1
```

add the decorator to a function using '@',  like this:

```python
@calculate_time # this is how to add a decorator 
def factorial(num):
    time.sleep(2) # to see an actual difference
    print(math.factorial(num))
```

or directly like this:

```python
factorial = calculate_time(factorial)
```

and finally we call the function

```python
factorial(10)
# >>> 3628800
# >>> Time taken: factorial 2.006180286
```


### generators

Generators are useful when we want to produce a large sequence of values, but we don't want to store all of them in memory at once. Generators use **def** like functions and **yield** instead of return. The `yield` keyword returns a value to the caller, but unlike `return`, it preserves the state of the function, allowing it to resume execution from where it left off

generators return an **iterable object**.

```python
def PowTwoGen(max=0):
	for i in range(max):
		yield 2**i
        
for n in PowTwoGen(6): print(n) # >>> 1 2 4 8 16 32

# or using list comprehension
res = [n for n in PowTwoGen(6)]
```

so the power of generator is that I can start getting results without the need to wait for the whole process to end

```python
count =  0
for i in powOf2(1000,000):
	if count ==  10:
		break
	print(i)
	count +=  1
```

Example using generator and decorator together

```python
import time
# define the decorator 
def timeCount(func):
    # inner function 
    def inner(*args, **kwargs): # take all func arguments
        start = time.time()
        res = func(*args, **kwargs)
        end = time.time()
        print('time elapsed:', end - start)
        return res # timeCount returns the return of func
    return inner

# generator, yields k powers of 2 
def pows2Gen(max=0):
	for i in range(max):
		yield 2**i

# define main function with timeCount decorator to get elapsed time
@timeCount
def powsTwo(k):
    return [n for n in pows2Gen(k)]

# use the decorated main function
res = powsTwo(10)
print(res)
```

### lambda function

It is an anonymous function 

Example:

```python
import math

##### lambda as function
area = lambda x : math.pi*(x**2) # to calculate circle area
area(1) # >>> 3.14

##### to sort a list of coordinates by distance from the origin
coords = [(7, 2), (3, 6), (0, 3), (4, 0)] 
sorted( coords, key=lambda p : math.sqrt(p[0]**2 + p[1]**2) ) 
# >>> [(0, 3), (4, 0), (3, 6), (7, 2)]
sorted(coords, key=lambda p: math.dist(p, (0,0)))
# >>> [(0, 3), (4, 0), (3, 6), (7, 2)]
```


### map function

It applies a function to each item in an iterable and returns the value of that function.
The synax for `map()` function is `list(map(function, iterable))`

Example:

```python
def square(n): # the function
	return n*n
nums = [1, 2, 3, 4] # the iterable

list( map(square, nums) ) # >>> [1, 4, 9, 16]

#### or using lambda expression
list( map(lambda x : x**2, nums) ) # >>> [1, 4, 9, 16]
```

### function parameters type annotations

```python
# specify that a variable should be a list of a specific type
from typing import List # also Tuple, Dict, Set, etc.

def process(items: List[int]) -> None:
    for item in items: 
	    print(item)

def add(x : float, y : float) -> float:
	return x + y

# specify that a parameter can be optionally None 
from typing import Optional  

def greet(name: Optional[str]) -> str: 
	if name is not None: return f"Hello, {name}!"  
	else: return  "Hello, there!"
```

### timeit

to measure the performance of a statement, e.g. the square of numbers from 0 to 99

```python
import timeit

timeit.repeat(
    stmt="[i ** 2 for i in range(100)]", # the statement to test
    number=1000, # repeat stmt 1000 times and return the average time
    repeat=3 # repeat it 3 times, i.e. returns a list of 3 timings
)

code_to_test = """
a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
"""
print(timeit.timeit(code_to_test, number=10))
print(timeit.repeat(code_to_test, repeat=3))

timer = timeit.Timer(code_to_test)
print(timer.timeit())
```

## Classes

```python
from datetime import date

class Entity:
    # Constructor
	def __init__(self, name, age): # self can be whatever other word but first parameter!
        self.name = name # public members
        self.age = age # public members
		self._cname = 'Entity' # protected member thanks to _
		self.__other = 0 # private member thanks to __

    # toString magic method
    def __str__(self):
        return f'{self.name}, {self.age} years old'
        
    # hashing magic method
    def __hash__(self):
        return hash((self.name, self.age)) # define tuple(name, age) as hash function
    
    # equality magic method
    def __eq__(self, other): 
        if isinstance(other, Entity) and hash(other) == hash(self):
			return True
        return False

    # private method, prefix the member name with __
    def __calculateAge(self, birthYear):
        return date.today().year - birthYear

    @staticmethod
    def isAdult(age): # don't use self in static methods
        return age > 18

    @classmethod # a sort of constructor variation
    def createFromYear(self, name, birthYear): 
        return self(name, self.__calculateAge(birthYear))


print(Entity.isAdult(23)) # static method >>> True

print(Entity('mike', 46)) # use of __str__ magic method >>> mike, 46 years old
e2 = Entity.createFromYear('tom', 1977) # using @classmethod >>> tom, 47 years old

print(e1 == e2) # use of __eq__ and __hash__ magic methods >>> False
Entity('mike', 46) == e1 # >>> True, same class and same hash (name, age)
```

**NB**: 
- **@classmethod** decorator to create *factory methods*. Factory methods return *class objects* ( similar to a constructor ) for different use cases.
- **@staticmethod** decorator to create utility functions.

other magic methods:
ref. https://docs.python.org/3/reference/datamodel.html#specialnmes



### Inheritance and override

```python
from datetime import date

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.classname = 'person'

    def __str__(self):
        return f'{self.classname}: {self.name}, {self.age} years old'

    # protected method: children can use it!
    def _getAge(birthYear):
        return date.today().year - birthYear
    
    # private method: only self can use it!
    def __somePrivate(self, something):
        pass

    @classmethod
    def createByBirthYear(self, name, birthYear):
        return Person(name, self._getAge(birthYear))

    @staticmethod    
    def great():
        print('hello!')
    
class Student(Person): # child class
    def __init__(self, name, age, matricola):
        super().__init__(name, age) # with super() access to parent class
        self.matricola = matricola
        self.classname = 'student' # override member

    # override method 
    @classmethod
    def createByBirthYear(self, name, birthYear, matricola):
        # use protected method _getAge()
        return Student(name, super()._getAge(birthYear), matricola)


print(Person('jack', 18)) # >>> person: jack, 18 years old
print(Person.createByBirthYear('mike', 1977)) # >>> person: mike, 47 years old

Person.great() # static method >>> hello!
Student.great() # inherit from parent >>> hello!

print(Student('alice', 33, 1234)) # >>> student: alice, 33 years old
s = Student.createByBirthYear('bob', 1980, 5678) # >>> student: bob, 44 years old
s.matricola # >>> 5678
```

**NB**: the `super()` function allows to access the parent class’s methods and attributes 


### iterable and iterator

Example of **iterables** are *lists, tuples, set, dictionaries*, i.e. containers that hold data
**Iterators** are objects that allows you to iterate over collections of data, implementing the *iterator design pattern*, i.e. they must implement the `__iter__()` and the `__next__()` methods

```python
class myIterator:
	def __init__(self, data): # initialize the iterator
		self.data = data
		self.index = 0
		
	def __iter__(self): # __iter__ usually returns the object itself
		return self

	def __next__(self): # __next__ defines how to navigate through the data
		if self.index < len(self.data):
			item = self.data[index]
			self.index += 1
			return item
		else:
			raise StopIteration # special exception to rise when we reach end of sequence

it = myIterator([5, 6, 7, 8])
while val = it.next():
	print(val)		
```


### abstract classes

`ABC` means abstract base class

```python
from abc import ABC, abstractmethod

class Polygon(ABC):
	@abstractmethod
	def noofsides(self):
		pass	

class Triangle(Polygon):
	# overriding abstract method
	def noofsides(self):
		print("I have 3 sides")

class Pentagon(Polygon):
	# overriding abstract method
	def noofsides(self):
		print("I have 5 sides")
```

## Enumerations

```python
from enum import Enum

class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

class Status(Enum):
    PENDING = 'pending'
    APPROVED = 'approved'
    REJECTED = 'rejected'

# Accessing enum members
Color.RED # >>> Color.RED
Color.RED.value  # >>> 1
if Color.RED == Color.GREEN

# Iterating over enum members
for color in Color:
    print(color) 
# >>> Color.RED 
# >>> Color.GREEN 
# >>> Color.BLUE
```

# Data Structures

## Array
a.k.a. list
dynamic non hashable arrays

```python
# DECLARATION array/list
arr = [1, 2, 3] 
[5, 'a', 3]
[0] * 3 # >>> [0, 0, 0]
[0 for _ in range(8)] # list comprehension >>> [0, 0, 0, 0, 0, 0, 0] 
list(range(5)) # >>> [0, 1, 2, 3, 4]
[i for i in range(5)] # >>> [0, 1, 2, 3, 4] 
# 2d LISTS
[[0] * 2 for _ in range(3)] # >>> [[0, 0], [0, 0], [0, 0]]
[[0] * 2] * 3 # >>> [[0,  0], [0,  0], [0,  0]]

# OPERATIONS
# O(1) time
arr[0] = 0 # write
arr[1] # read
arr[-1] # read last element
len(arr) # get the length of the array
arr.append(4) # append a new value at the end
arr.pop() # removes last element
arr.pop(3) # removes element at index 3
# O(n) time
arr.remove(2) # removes first element 2
arr.insert(1, 7) # insert 7 in position 1

arr = [True, False, False]
if any(arr): print("Yess!") # checks if any element in arr is True

# LOOPING 
for i in range(len(arr)): 
	print(arr[i]) # >>> from first to last
	print(arr[~i]) # >>> from last to first (if i = 0 then ~i = -1)
for n in arr: 
	print(n)
for i, n in enumerate(arr): 
	print(i, ":", n)

# LIST COMPREHENSION
[i for i in range(5)] # >>> [0, 1, 2, 3, 4]
[i for i in range(5) if i % 2 == 0] # >>> [0, 2, 4]
list(reversed(range(1,5))) # >>> [4, 3, 2, 1]

# SUBLIST 
# arr[start:end:stride] 
# start included default 0, end excluded default len(arr), stride or step default is 1
arr[1:3] # elements at index 1 and 2
arr[:3] # elements from index 0 included to index 3 excluded

# CONCATENATION
arr3 = arr1 + arr2 # concatenate arr1 and arr2 into arr3
arr1.extend(arr2) # concatenate, arr1 now equal to arr3

# SORT
s = sorted(arr) # sorted in s 
arr.sort() # sort arr ascending
arr.sort(reverse=True) # sort arr descending
arr.sort(key=lambda x: len(x)) # sort based on elements length

# REVERSE
arr.reverse() # reverse arr
arr = arr[::-1] # reverse arr
arr = list(reversed(arr)) # reverse arr

# UNPACKING
a, b, c =  [1,  2,  3] # un-packing
for v1, v2 in zip(arr1, arr2): # un-packing multiple arrays
	print(v1, v2) 
```

## Stack

```python
arr = [] # stack uses a normal list
arr.append(4)  # push a new value
arr.pop()  # remove last appended
arr[-1]  # peek: get the last element appended without removing it

# check if stack is not empty
len(arr) # number of elements inside the array
if arr: # True if not empty, False if empty
if not arr: # True if empty, False if not empty
while arr: # while stack is not empty
```

## Queue

```python
from collections import deque

myQ = deque() # declare queue

myQ.append(1) # enqueue element
myQ.popleft() # dequeue
myQ[0] # peek

len(myQ) # number of elements inside the queue
while myQ: # while queue is not empty
myQ.appendleft(1) # undo popleft, add 1 again
 
# INITIALIZATION
myQ = deque([1, 2, 3]) # a list of values
myQ.popleft() # 1

myQ = deque( [[0, 0], [1, 1]] ) # a list of coordinates (as lists)
myQ.popleft() # [0, 0]

myQ = deque( [(0, 0), (1, 1)] ) # a list of coordinates (as tuples)
myQ.popleft() # (0, 0)
```

## Hashset
a.k.a. set

```python
mySet = set() # declare hashset/set

mySet.add(1) # add element, complexity O(1)
if 1 in mySet: # check element, complexity O(1)
mySet.remove(1) # remove element, complexity O(1)
mySet.clear() # empty the set

len(mySet) # number of elements in the set
if mySet: # checks if the set is non-empty

# INITIALIZATION
mySet = {1, 2, 3, 4} # {1, 2, 3, 4}
mySet = {0, 'apple', 3.5} # initialize set
mySet = { i for i in range(5) } # initialize set using list comprehension

mySet = set([1, 2, 3, 4]) # list to set >>> {1, 2, 3, 4}
myList = list(mySet) # set to list >>> [1, 2, 3, 4]
```
**NB**: intersect of sets using operator ``&``. Union of sets using the operator ``|``


## Hashmap
a.k.a. dictionary

```python
myMap = {} # declare hashmap/dictionary

myMap["alice"] = 88 # insert item
if myMap: # checks if the map is non-empty
if 'alice' in myMap: # check if a key is in the map
myMap.get("alice") # get value of key 'alice' >>> 88
myMap['alice'] # get the value of key 'alice'
myMap.pop("alice") # remove item that has key 'alice'
myMap.clear() # empty the dictionary

myMap.get("tom", 0) # if key not found returns 0
myMap.get("tom", 'notFound') # if key not found returns 'notFound'
myMap["tom"] = myMap.get("tom", 0) + 1 # safe increment

list(myMap.keys()) # list of keys 
list(myMap.values()) # list of values
list(myMap.items()) # list of tuples (key, value)
len(myMap) # number of elements in the map

# LOOPING
myMap = {'alice': 90, "bob": 70}
for key in myMap: print(key, myMap(key)) # default looping to key: values
for val in myMap.values(): print(val) # or directly the values, if no key needed
for key, val in myMap.items(): print(key, val) # or using un-packing

# SORTING
d = {2:'a', 1:'c', 3:'b'}
sorted(d) # list of sorted keys >>> [1, 2, 3]
sorted(d.keys()) # list of sorted keys >>> [1, 2, 3]

# list of values sorted by key >>> ['c', 'a', 'b']
[d[k] for k in sorted(d)]

# list of keys sorted by value >>> [2, 3, 1]
sorted(d, key=d.get)
sorted(d, key=lambda x: d[x])

# NOT REALLY TO BE USED!
dictSortedByValue = dict(sorted(d.items(), key=lambda item: item[1])) 
# >>> {2:'a', 3:'b', 1:'c'}
dictSortedByKey = dict(sorted(d.items(), key=lambda item: item[0])) 
# >>> {1:'c', 2:'a', 3:'b'}

# INITIALIZATION
myMap = {'alice': 90, "bob": 70}
myMap = dict(one=1, two=2, three=3) # using dict
myMap = dict( [('two', 2), ('one', 1), ('three', 3)] ) # list of tuples

myMap = { i: 2*i for i in range(3) } # list comprehension >>> {0:0, 1:2, 2:4} 

characters = ["Iron Man", "Spider Man", "Captain America"]
actors = ["Downey", "Holland", "Evans"]
myMap = {x:y for x in characters for y in actors}
myMap = dict( zip(characters, actors) )
```

### defaultdict

defaultdict never raise a KeyError. It provides a default value for the key that does not exists

```python
from collections import defaultdict

d = defaultdict(int) # declare hashmap key:value with int values
d["a"] = 1 # add an item
print(d["c"]) # if key not found it returns 0 by default

d = defaultdict(lambda:str("Not Present"))
print(d["c"]) # if key not found it returns 'Not Present' by default

d = defaultdict(list) # declare hashmap key:value with List values
d["a"] = [1, 2] # set list [1,2] to item with key 'a'
d["a"].append(3) # append element 3 to the list corresponding to key "a"
```

### counter

```python
from collections import Counter

myC = Counter("Hii") # passing a string gives Counter({'i': 2, 'H': 1})
myC = Counter(['H', 'i', 'i'])  # passing a list gives Counter({'i': 2, 'H': 1})

# OPERATIONS
sorted(myC.elements()) # ['H', 'i', 'i']
myC.most_common() # ordered by most common [('i', 2), ('H', 1)]
myC.most_common(1) # the (two) most common [('i', 2)]
myC['b'] = 2 # reassign/insert
myC.clear() # clear 
```

## Tuple

immutable and hashable!

```python 
myT = (1, 2, 3) 
myT[0] # 1
myT[-1] # 3
# myT[0] = 0 # we cannot do this!!! tuples are immutable

myMap[(2, 3)] = 7 # use tuple as key of an hashmap, list as a key won't work! (not hashable)

# creating a list of tuples (characters, actors)
characters = ["Iron Man", "Spider Man", "Captain America"]
actors = ["Downey", "Holland", "Evans"]
myT = list(zip(characters, actors))
```

### namedtuple

easy-to-create, lightweight object types. Can be referenced using object-like variable dereferencing or the standard tuple syntax. They can be used similarly to `struct` or other common record types, except that they are immutable

```python
pt1 = (1.0, 5.0)
pt2 = (2.5, 1.5)

from math import sqrt
line_length = sqrt((pt1[0]-pt2[0])**2 + (pt1[1]-pt2[1])**2)
```

Using a named tuple it becomes more readable:

```python
from collections import namedtuple

Point = namedtuple('Point', 'x y')
pt1 = Point(1.0, 5.0)
pt2 = Point(2.5, 1.5)

from math import sqrt
line_length = sqrt((pt1.x-pt2.x)**2 + (pt1.y-pt2.y)**2)
```


## Priority queue
a.k.a. heap

Binary heap is a complete BT where every parent has its value greater (or equal) then all its descendent
**NB**: by default python heap is a minheap

### minheap

```python
import heapq

myMH = [] # declare heap (it is a simple list!)
heapq.heappush(myMH, 3) # insert O(logN) 
myMH[0] # peak min O(1)
v = heapq.heappop(myMH)) # pop min O(logN)
```

**NB**: if the elements in the heap are custom objects and I want to set the priority based on an object attribute (e.g. attribute age for a custom object User), then I can heappush a tuple (age, object) 

### maxheap

```python
import heapq

myMH = []
heapq.heappush(myMH, 3 *-1) # insert element (negated!), O(logN) 
myMH[0] *-1 # peak max (negate!), O(1)
v = heapq.heappop(myMH) *-1 # pop max (negate!), O(logN)
```

### heapify

```python
myMH = [2, 1, 8, 4, 5]

# for MIN heap!
heapq.heapify(myMH) # O(n) time
while myMH: print(heapq.heappop(myMH))

# for MAX heap!
myMH = [-i for i in arr] # negate each elemet!
heapq.heapify(myMH) # O(n) time
while len(myMH): print(-1 * heapq.heappop(myMH)) # remember to negate!
```

### heap of lists

```python
arr = [[2, 4], [1, 3], [8, 4], [4, 1], [5, 7]]
minHeap = arr
heapq.heapify(minHeap) # list is ordered according to the default key (the first element of each list!)
while minHeap: print(heapq.heappop(minHeap)) # >>> [1, 3] [2, 4] [4, 1] [5, 7] [8, 4]
```


# Custom Data Structures

## Liked list

A node with max 1 children. 

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        res = ''
        while self:
            res += f'{str(self.val)} -> '
            self = self.next
        return res
```

reverse a linkedList

```python
def reverse(head): 
    prev = None 
    current = head 

    while current: 
        next_node = current.next 
        current.next = prev 
        prev = current 
        current = next_node 
        
    return prev
```

## Binary tree

A node with max 2 children. 

**depth**: tree root with no children has depth 1
**height**: tree root with no children has height 0
**balanced**: 
	- height of left subt and height of right subt do not differ more then 1
    - left subt is balanced and right subt is balanced
**complete**:
	- all levels but the last are completely filled
	- in the last level nodes are as left as possible
	**NB**: height is always logn, arrays representation does not have gaps between elements
***Heap***:
	- it is a complete BT and 
	- every parent has its value greater (or equal) then all its descendent
***Binary Search Tree***:
	- the left subt contains only nodes with keys  *less than*  the node's key
	- the right subt contains only nodes with keys  *greater than* the node's key.
	- both the left and right subt must also be BST

```python
from collections import deque

class btNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

    def __str__(self):
        queue = deque()
        queue.append(self)

        s = "["
        while queue:
            n = queue.popleft()
            s += f"{n.val}, "
            if n.left: queue.append(n.left)
            if n.right: queue.append(n.right)
        return s[:-2] + "]"
```

### Bredth first search BSF
visiting in BFS / levelorder

```python
qu = deque(root)
while qu:
	for i in range(len(qu)):
		n = qu.popleft()
		if n.left: qu.append(n.left)
		if n.right: qu.append(n.right)

	level += 1
```

### Depth first search DSF 
visiting in DFS using a **stack** gives **pre-order**

```python
st = [root]
while st:
	n = st.pop()
	if n.left: st.append(n.left)
	if n.right: st.append(n.right)
```

### recursive DFS
visiting in DFS using recursion can give **(pre/in/post)-order**

```python
def preOrder(root):
	if not root: return 
	print(root.val)
	preOrder(root.left)
	preOrder(root.right)
	
def inOrder(root):
	if not root: return 
	inOrder(root.left)
	print(root.val)
	inOrder(root.right)
	
def postOrder(root):
	if not root: return 
	postOrder(root.left)
	postOrder(root.right)
	print(root.val)	
```

## Trie or Prefix tree

A way to efficiently store and retrieve a set of strings. "*and*" and "*ant*" will share *root* -> *a* -> *n* 

```python
class TrieNode:
	def __init__(self):
		self.children = {} # 26 letters hashmap
		self.endOfWord = False

class Trie:
	def __init__(self):
		self.root = TrieNode() # empty root node
		
	def insert(self, word: str) -> None:
		current = self.root 
		for c in word:
			# hm doesn't have already that letter
			if c not in current.children:
				current.children[c] = TrieNode()
			current = current.children[c]
		current.endOfWord = True
			
	def search(self, word: str) -> bool:
		current = self.root 
		for c in word:
			if c not in current.children:
				return False
			current = current.children[c]
		
		return current.endOfWord
	
	def startsWith(self, prefix: str) -> bool:
		current = self.root 
		for c in prefix:
			if c not in current.children:
				return False
			current = current.children[c]
		
		return True
```


## Graphs

- **directed graph**: can be represented with an `adjacency map` under the form of an hashmap ``{node index : [neighbor nodes indices]}`` where the key is a node index and the value is the list of neighbors indices that the node points to
	- DAG: directed acyclic graph

- **undirected graph**: can be represented with an array edges [a, b], or with an adjacency list, in case that the `number of unique edges == number of nodes` for sure we have a cycle!

```python
class Node:
	def __init__(self, val=0, neighbors=None):
		self.val = val
		self.neighbors = neighbors if neighbors is not None else []

    def __str__(self):
	    # create a map of existing nodes
        visited = {} 
        def dfs(node):
            if node.val in visited: 
                return
            visited[node.val] = node
            for nei in node.neighbors:
                dfs(nei)
        
        dfs(self)
        if len(visited) <= 1: return "[[]]"

        s = "["
        for node in visited.values():
            s += "["
            for nei in node.neighbors:
                s += f"{nei.val}, "
            s = s[:-2] + "], "

        return s[:-2] + "]"
```

### graph algoritms

- **DFS**: $O(n)$ it traverse the graph using recursion and it uses an `hashset` to detect cycles. It can be traversed non recursively using a `stack`
- **BFS**: $O(n)$ it traverse the graph using a `queue` and it uses an `hashset` to detect cycles. The traversal is done layer by layer 
- **Number of Connected component in UG** (undirected graph): $O(E+V)$ if it is expressed as an array of edges, E to read all the edged to transform it into an adjacency list. Then we apply DFS on every vertex checking if the vertex has already been visited (same connected component)
	- **Union-Find**: $O(nlogn)$ used to calculate the number of connected components or to union together disjonit sets of nodes (connected components) and combine them together efficiently, it requires a `forest of trees`.  **HOWTO**: we maintain a `parent array` initially with the index of the nodes (each node initially is parent of itself), and a `rank array` representing for each node the size of the connected component, initially each node is set to 1 (each node initially has rank 1). Then we start reading the edges array given as input and we start to connect the nodes (higher rank nodes become parents of lower rank ones). **NB**: When connecting two nodes, we first need to find the ancestors of both nodes, then we connect the anchestors together. Connecting nodes means update the values of the parent array and relative rank one. During this process, each time we make a union we decrement the number of vertices. The result is the number of connected components!
- **Topological sort**: $O(E+V)$ used in DAG (directed acyclic graph) to read the nodes in a correct sequence, it uses an `hashset` to detect cycles as it uses DFS, optionally a `stack` if DFS is not written recursively and possibly another hashset to determine the already processed nodes. **HOWTO**: turn the edges array into an adjacency list, then run DFS to each node, avoiding repeated nodes saved into the hashset and break as soon as a cycle is detected (through the uso of another hashset). If we have a cycle then there is no possible solution
- **Dijkstra**: $O(ElogV)$ used to find the shortest path from a vertex to all the others, it uses a `min-heap` (a.k.a. `priority queue`) because it looks at the minimum edge E and an `hashset` to look for cycles. **HOWTO**: we insert the starting node inside a minheap with weight = 0, then we pop it, we check in the hashset if node was already seen, if not we add it to the hashset and we process all its adjacent nodes (BFS). That means we push neighboars into the heap with updated weights (neighboar weight = parent weight + neighboar weight). The heap elements are tuples (weight, node), so they will be popped according to the weight.
- **Minimum spanning tree** 
	- **Prim's Kruskal**: $O(n^2logn)$ used to find the minimum spanning tree. At the beginning we have vertices without edges, we want to find the most efficient way to connect all vertices without forming cycles, i.e. V-1 edges. Basically we start at any single node and we apply BFS checking not to repeat nodes using an `hashset` and checking the frontier of nodes using a `minheap` in order to start adding nodes from the minimum possible cost ones first. We stop when the number of nodes in the hashset is equal to the total number of nodes. **HOWTO**: we start from a node n, add it to the hashset visit, add it to the minheap frontier with null weigth (0, n). We then pop it out from the frontier, add it to the hashset, increment a cost variable by the weight of the popped node, then we add all node's neighboars to the frontier (checking the given adjacency list). We then continue to 1. pop the minimum from the frontier, 2. if in hashset continue 3. add it to the hashset, 4. update the cost variable and 5. add neighboars back into the frontier, till the hashset size equals the total number of nodes.
- **Floyd warshall's**: 


# Math 

```python
import math 

ITERATIONS = 1_000_000 # _ here is just to make the number more readable

# ROUND & CAST DECIMAL NUMBERS
round(n) # is a function to round a float, 
int(n) # cast a float to an integer, get rid of the decimal part by truncating it
int(-3.6) # -3
round(-3.6) # -4 

math.fmod(8, 7) # division remainder or modulo >>> 1.0
math.floor(3 / 2) # 1
math.ceil(3 / 2) # 2
math.sqrt(9) # 3.0
math.pow(2, 3) # 8.0
3 ** 2 # same as math.pow(3, 2) gives 9

5 / 2 # decimal division 2.5
5 // 2 # integer division 2
-3 // 2 # Issue: it rounds towards zero to -2
int(-3 / 2) # workaround: decimal division and cast to int, gives -1

10 % 3 # modular reminder, gives 1
-10 % 3 # Issue: returns 1
math.fmod(-10, 3) # workaround: use math fmod, gives -1

arr = [4, 1, 3, 1]
sum(arr) # returns 9, the sum of all elements of the array

# PREFIX SUM
[ sum(arr[0:i+1]) for i in range(len(arr)) ] # >>> [4, 5, 8, 9]

# euclidean distance
math.dist((1, 2), (3, 4)) # it works also with 2 lists

# INFINITY
float("inf") # positive infinity
float("-inf") # negative infinity
```

## min max

```python
nums = [3, 5, 9, 1, -5]
min(nums) # >>> -5
max(nums) # >>> 9
nums.index(min(nums)) # index of min num >>> 4
nums.index(max(nums)) # index of max num >>> 2

min("abcdefghijklmnopqrstuvwxyz") # >>> 'a'
min("aA") # >>> 'A' because ord('A') = 65 and ord('a') = 97

max(["Pythonista","world", "Hello", "and", "welcome"]) # >>> 'world'

prices = {"pineapple": 0.89, "apple": 1.57}
min(prices) # min key by default >>> 'apple' 
min(prices.values()) # >>> 0.89

min(["20", "3", "35", "7"], key=int) # >>> 3 because we pass the build-in function int()

min([], default=42) # >>> 42 because the list is empty!

letters = ["A", "B", "C", "X", "Y", "Z"]
min(letter.lower() for letter in letters) # >>> 'a'

point_pairs = ( ((1, 2), (2, 3)), ((4, 5), (5, 5)) )
# lambda unpacks pairs into 2 coordinates
min(point_pairs, key=lambda points: math.dist(*points))
```

## math problems

### factorial

```python
def factorial(n): 
	if n == 0 
		return 1
	return n * factorial(n - 1)
```

using **memoization** (an optimization technique used to speed up programs by storing/caching the results of expensive function calls into arrays/sets/maps and retrieve the result when the same inputs occurs again)

```python
def factorial(n, memo={}):
    if n in memo:
        return memo[n]
    if n == 0:
        return 1
    result = n * factorial(n-1, memo)
    memo[n] = result
    return result
```

### prime number

```python
def primeNumber(n):
    if n <= 1:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    w = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += w
        w = 6 - w  # Switch between 2 and 4 for optimization
    return True
```

### great common divisor GCD

the greatest common divisor of two numbers does not change if the larger number is replaced by its difference with the smaller number.

```python
def gcd(a, b):
	if b == 0: return a  
	return gcd(b, a % b)
```

### least common multiple LCM

```python
def lcm(x, y): 
	return abs(x * y)
```

### fibonacci 

```python
def fibonacci(n):
    fib_series = [0, 1]

    while len(fib_series) < n:
        next_term = fib_series[-1] + fib_series[-2]
        fib_series.append(next_term)

    return fib_series[:n]

def fibonacci_recursive(n, series=[0, 1]): 
	if n <= len(series): 
		return series[:n] 
	else: 
		next_term = series[-1] + series[-2] 
		return fibonacci_recursive(n, series + [next_term])
```

### Newton square root of a number

```python
def newton_square_root(number, epsilon=1e-6, max_iterations=100):
    """
    Calculate the square root of a number using Newton's method.
    
    :param number: The number for which to find the square root.
    :param epsilon: The desired accuracy.
    :param max_iterations: Maximum number of iterations.
    :return: Approximate square root.
    """
    guess = number / 2.0  # Initial guess can be any positive value
    for _ in range(max_iterations):
        guess = 0.5 * (guess + number / guess)  # Newton's method formula
        if abs(number - guess**2) < epsilon:
            break
    return guess
```

# Numpy

NumPy aims to provide an array object that is up to 50x faster than traditional Python lists. NumPy arrays are stored at one continuous place in memory unlike lists and is optimized to work with latest CPU architectures.

An array object in numpy is called **ndarray** and can be created passing a list or a tuple to the numpy function **array()**

## initialization

```python
import numpy as np

##### initialization
np.array(43) # 0d array, i.e. scalar >>> 43 
np.array([43]) # 1d array >>> [43]
np.array([1, 2, 3, 4]) # 1d using list >>> [1 2 3 4]
np.array((1, 2, 3, 4)) # 1d using tuple >>> [1 2 3 4]
np.array([1, 2], dtype=np.float32)

np.zeros((2, 1)) # >>> [[ 0.], [ 0.]]
np.ones(3) # >>> [1., 1., 1.]
np.ones((2, 2)) # >>> [[1., 1.], [1., 1.]]
np.identity(3, dtype=int) # identity integers matrix of size 3
# >>> [[1 0 1]
# >>>  [0 1 0]
# >>>  [0 0 1]]

np.arange(3) # >>> [0, 1, 2]
np.arange(0, 10, 2, int) # start, end, increment, type >>> [0, 2, 4, 6, 8]

# initialization using datatype
datatype = [('name', 'U7'), ('age', int), ('height', int)]
people = [('Alice', 25, 170), 
		  ('Bob', 35, 180), 
		  ('Charlie', 35, 175)]
array = np.array(people, dtype = datatype) 

##### dimension
np.array(43) # 0-D array, i.e. scalar
np.array([1, 2, 3, 4]) # 1D array
np.array([[1, 2, 3], [4, 5, 6]]) # 2D array
a = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]]) # 3D array
a.ndim # number of dimensions >>> 3

##### accessing elements
arr = np.array([[0, 2, 3], [4, 5, 6]])
arr[1, 2] # >>> 6
arr[1][2] # >>> 6

##### iterating
arr = np.array([1, 2, 3])
for x in arr: 
	print(x)
for i, x in np.ndenumerate(arr):
	print(i, x)
	
arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])  
for x in np.nditer(arr):  # iterate on every scalar, regardless of the dimensionality
	print(x)

##### type
arr = np.array((0, 1, 2, 3))
arr.dtype # get the data type >>> int64
arr.astype(bool) # >>> [False True True True]
```


## shape reshape flatten copy

```python
# shape
arr = np.array([[1, 2], [3, 4], [5, 6]])
arr.shape # >>> (3, 2)
# reshape 
arr = np.array([1, 2, 3, 4, 5, 6])
arr.reshape(3, 2) # >>> [[1, 2], [3, 4], [5, 6]]
arr.reshape(3, -1) # -1 means guess the dimension >>> [[1, 2], [3, 4], [5, 6]]
# flattening 
arr.reshape(-1) # from nd to 1d >>> [1, 2, 3, 4, 5, 6]
arr.flatten() # flatten >>> [1, 2, 3, 4, 5, 6]

##### deep/shallow copy
x = arr.copy() # deep copy 
x.base # check if the array owns the data >>> None
x = arr.view() # shallow copy, i.e. reference 
x.base # x refers to arr >>> [[0, 2, 3], [4, 5, 6]]
```

## concatenate stack split 

```python
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])

##### concatenate (axis 0 = rows, 1 = columns, -1 = last)
np.concatenate((arr1, arr2), axis=0) # join row wise 
# >>> [[1, 2], [3, 4], [5, 6], [7, 8]]
np.concatenate((arr1, arr2), axis=1) # join col wise 
# >>> [[1, 2, 5, 6], 
# >>>  [3, 4, 7, 8]]

##### stack a sequence of arrays along a new axis (axis 0 = rows, 1 = columns, -1 = last)
np.stack((arr1, arr2), axis=0) # stack new axis row wise
# >>> [[[1, 2], [3, 4]],
# >>>  [[5, 6], [7, 8]]]
np.stack((arr1, arr2), axis=1) # stack new axis col wise
# >>> [[[1, 2], [5, 6]],
# >>>  [[3, 4], [7, 8]]]
np.stack((arr1, arr2), axis=-1) # stack new axis 3rd dim wise
# >>> [[[1, 5], [2, 6]],
# >>>  [[3, 7], [4, 8]]]

##### split
arr = np.array([1, 2, 3, 4, 5, 6])
np.split(arr, 3) # >>> [[1, 2], [3, 4], [5, 6]]
```

## search filter

```python
##### search
arr = np.array([1, 2, 3, 4, 5, 4, 4])  
np.where(arr == 4) # indices list >>> (array([3, 5, 6]),) 

##### filter
arr = np.array([41, 42, 43, 44])
arr[arr > 42] # >>> [43, 44]
arr[[True, False, True, True]] # >>> [41, 43, 44]
```

## sorting

```python
##### sorting
arr = np.array([3, 2, 0, 1])
np.sort(arr) # default axis is -1, i.e. last dimension >>> [0, 1, 2, 3]

array = np.array([[3, 10, 2], 
                  [1, 5, 7], 
                  [2, 7, 5]])

np.sort(array, axis=0) # sort row wise
# >>> [[ 1  5  2]
# >>>  [ 2  7  5]
# >>>  [ 3 10  7]]

np.sort(array, axis=1) # sort column wise, same as axis=-1
# >>> [[ 2  3 10]
# >>>  [ 1  5  7]
# >>>  [ 2  5  7]]

#### sorting with order
datatype = [('name', 'U7'), ('age', int), ('height', int)]
people = [('Alice', 25, 170), 
		  ('Bob', 35, 180), 
		  ('Charlie', 35, 175)]
array = np.array(people, dtype = datatype) 

np.sort(array, order='height') # sorting based on height
# >>> [('Alice', 25, 170) ('Charlie', 35, 175) ('Bob', 35, 180)]

np.sort(array, order='age', 'height') # sorting first on age, then on height
# >>> [('Alice', 25, 170) ('Charlie', 35, 175) ('Bob', 35, 180)]
```

## operations

```python
# squeeze
a = np.array([[[0], [1], [2]]]) # ndim = 3
a.squeeze() # Remove axes of length one ndim = 1 >>> [0, 1, 2] 
# transpose
a = np.array([[1, 2], [3, 4]])
a.transpose() # Returns an array with axes transposed >>> [[1, 3], [2, 4]]
```

# Matrix linear algebra

- **scalar**: if vector has 1 row and 1 column 
- **zero matrix**: all elements are 0
- **identity matrix** $I$: a square matrix with all 1 on the diagonal, all the rest 0. $M*I = M = M*I$ 
- **diagonal matrix**: elements only on the diagonal, all rest is 0
- **inverse matrix** $A^{-1}$  properties:
	- $A*A^{-1} = I$
	- $(AB)^{-1} = A^{-1}B^{-1}$
	- $(A^T)^{-1} = (A^{-1})^T$

## sum 

to add matrices they need to have the same dimension
 
## inner product

$u = \begin{pmatrix} u_1 \\\ u_2 \\\ u_3 \end{pmatrix}$, $v = \begin{pmatrix} v_1 \\\ v_2 \\\ v_3 \end{pmatrix}$

in general product of two vectors $\vec{u}$ and $\vec{v}$ is possible if the number of columns in $u$ are equal to the number of rows in $v$.
The resulting matrix has $u$ number of rows and $v$ number of columns


### dot product

the dot product operates on vectors

$u^T = \begin{pmatrix} u_1 \ u_2 \ u_3 \end{pmatrix}$
$v^T = \begin{pmatrix} v_1 \ v_2 \ v_3 \end{pmatrix}$

**dot product**, a.k.a. **inner product** is:
$$
u^T*v = u_1*v_1 + u_2*v_2 + u_3*v_3
$$

**NB**: the result is a scalar as the resulting matrix has 1 row and 1 column
if dot product = 0 then $u$ and $v$ are **orthogonal** 

**norm** is: 
$$
||u|| = (u^T*u)^{1/2} = \sqrt{u_1^2 + u_2^2 + u_3^2}
$$

if norm of a vector = 1, then the vector is **normalized**

### matmul
While **matmul** combines matrices, the **dot product** operates on vectors. 

- If performance is a primary concern, dot may be the better choice. 
- if precision is a primary concern, Matmul allows for more complex operations
- Matmul might be optimized for certain hardware or software libraries

Python example of **dot product** and **matmul**

```python 
k = 3 # scalar 
a = np.array([[1, 2]]) # 1 by 2 matrix
b = np.array([[5, 6], # 2 by 2 matrix
			  [7, 8]])

np.dot(k, a) # scalar product >>> [[3 6]]
np.dot(a, k) # scalar product >>> [[3 6]]
np.dot(a, b) # dot product result is 1 by 2 matrix >>> [[19 22]]
np.matmul(a, b) # matmul result is 1 by 2 matrix >>> [[19 22]]
```

## outer product
not really used 

**outer product** is:
$$
u*v^T = \begin{pmatrix} u_1v_1 \ u_1v_2 \  u_1v_3 \\ u_2v_1 \ u_2v_2 \ u_2v_3 \\ u_3v_1 \ u_3v_2 \ u_3v_3 \end{pmatrix}
$$

**NB**: the result is a 3x3 matrix 


# Pandas

## Series

it is a 1d data structure, can be seen as columns of a table. Initialized using:

1. list with optional index list parameter to specify the indices
2. dictionary where keys become the indices

```python
import pandas as pd

# using a list
pd.Series([9, 8, 5]) # indices automatically assigned
# >>> 0  9
# >>> 1  8
# >>> 2  5
pd.Series([9, 8, 5], index = ['x', 'y', 'z']) # indices specified using index
# >>> x  9
# >>> y  8
# >>> z  5

# using a dictionary, i.e. dictionary keys become the indices
pd.Series({'x':9, 'y':8, 'z':5}) 
# >>> x  9
# >>> y  8
# >>> z  5
```

## dataframe

it is a 2d data structure like a table with rows and columns (Series is like a column, a DataFrame is the whole table). Initialized using:

1. from a file
2. list of list
3. dictionary: keys become the labels for the table columns, values are iterable objects
4. list of dictionaries

**NB**: optional index list parameter, optional columns parameter with the name of columns

```python
##### from a file
pd.read_csv('data.csv') # comma separated CSV file 
pd.read_json('data.json') # json are like python dictionaries 

##### using list of list, i.e. list of rows
pd.DataFrame([[21, 54], [76, 43], [98, 93]], columns=['fild1', 'field2'])
# >>>  filed1 field2 
# >>> 0    21    54
# >>> 1    76    43
# >>> 3    98    93

##### using dictionary, i.e. key is the column label, value is the list of column values
pd.DataFrame({'x':[9], 'y':[8], 'z':[1]}) # automatic indices 
# >>>    x  y  z
# >>> 0  9  8  1
pd.DataFrame({'name':['mike', 'jack'], 'age':[45, 29]}, index=['1st', '2nd']) 
# >>>      name  age
# >>> 1st  mike   45
# >>> 2nd  jack   29

##### using a list of dictionaries
pd.DataFrame([{'name':'mike', 'age':45}, {'name':'jack', 'age':29}], index=['1st', '2nd'])
# >>>      name  age
# >>> 1st  mike   45
# >>> 2nd  jack   29
```

## info

the describe() method will print a summary of the data:

- **count** how many rows have non-missing values
- **mean** the average
- **std** the standard deviation spread out of the values
- **min** and **max** are the minimum and maximum
- **25%**, **50%**, **75%** are the percentiles

```python
df.describe()
df.columns # print the list of the colum names
```

## retrieving data

```python
##### to get a dataframe column
df['name'] # this becomes a Series!
# >>> 1st  mike
# >>> 2nd  jack

df.name


##### to get a dataframe row
# single row 2nd
df.loc['2nd'] # this becomes a Series!
# >>> name  jack
# >>> age   29
# single row 1st, column age
df.loc['1st', 'age'] # >>> 45
# multiple rows: list of indices, indices range
df.iloc[[1, 3, 5]] # rows at index 1, index 3, index 5
df.iloc[0:3] # rows with inex in range(0, 3)

##### cycle over all rows
for r in df.index:
	print(df.loc[r])

##### filter data
df.nlargest(5, 'age') # retrieve 5 largest in col 'age'
df.nsmallest(5, 'age') # retrieve 5 smallest in col 'age'

df[df['name'].str.contains('j')] # dataframe where name contains 'j'
df[~df['name'].str.contains('c')] # dataframe where name does NOT contain 'c'
df[df['name'] == 'mike'] # dataframe where name is mike
df[df['age'] == 29] # dataframe where age is 29
df[~df['age'].isnull()] # dataframe where age is not null, i.e. numpy.NAN

df.where( (df['Duration'] ==  60) & (df['Calories'] ==  340) )
```

## analyzing data

```python
df = pd.DataFrame({'x':[9, 4], 'y':[8, 2], 'z':[1, None]}, index=['a', 'b'])  
df.head() # optional specify the num of rows
df.tail() # optional specify the num of rows
df.info() # num of rows/cols, memory usage, num of null/non-null values per column
df.dtypes # shows the type for each column
df.shape # shows num or rows and cols
```

### some statistic

**Distributions**:
- **NORMAL or GAUSSIAN**: a symmetric bell-shaped curve, i.e. the birthweight of new babies
- **UNIFORM**: constant curve. All outcomes are equally likely, i.e. the toss of a dice
- **BINOMIAL**:
- **POISSON**:
- **EXPONENTIAL**:


**mean**: it is the matematical average of all dataset values

$\mu = \frac{\sum_{i=1}^Nx_i} {N}$

**median**: the value in the middle after sorting all values

```
Odd N: Median = Value at position (N+1)/2
Even N: Median = (Value at position N/2 + Value at position (N/2)+1) / 2
```

**mode**: the most frequent value
**variance**: is a measure of the dispersion or spread of a set of data points in a dataset. In statistics, it quantifies the amount of variation or dispersion from the mean (average) of a dataset.

$\sigma^2 = \frac{\sum_{i=1}^N (x_i-\mu)^2} {N}$

**standard deviation**:  is another measure of the dispersion or spread of a set of data points in a dataset, similar to variance

$\sigma = \sqrt{ \frac{\sum_{i=1}^N (x_i-\mu)^2} {N} }$

**NB**: the square root of the variance, which is the standard deviation, is often preferred for describing the spread of data because it's in the same units as the original data

```python
# some statistic
df['z'].mean() # the average value (the sum of all values divided by number of values)
df['z'].median() # the value in the middle, after you have sorted all values ascending
df['z'].mode() # the value that appears most frequently

# measure the amount of variation or dispersion from the mean (average)
df['z'].std() # standard deviation: square root of variance
df['z'].var() # variance: square of the standard deviation 
```

## cleaning data

rows containing one or more **empty cells**, i.e. null values, are usually removed!

```python
# delete problematic rows
df.dropna() # creates a new dataframe without rows containing empty cells
df.dropna(inplace = True) # removes empty cells rows from the original dataframe

# fix problematic cells
df.fillna(666, inplace = True) # replace all dataframe empty cells with 666
df['z'].fillna(0, inplace = True) # replace empty cells in col 'z' with 0
df['z'].fillna(df['z'].mean(), inplace=True) # replace col 'z' empty cells with 'z' avg 
df['A'].clip(-2, 7, inplace=True) # trim col 'A' value in range [-2:7]
```

cells with **wrong data** or **wrong data format** are solved either removing rows or converting problematic cells

```python
df = df.astype(int) # convert all data to int
pd.to_datetime(df['Date']) # convert all non-datetime cells in column Date to datetime format

# write 0 in all rows where 'z' > 0
for r in df.index:  
	if df.loc[r, 'z'] > 0:  
		df.loc[r, 'z'] = 0

# drop all rows where 'z' > 0
for r in df.index:  
	if df.loc[r, 'z'] > 0:  
		df.drop(r, inplace = True)
```

show and remove **duplicates**

```python
df.duplicated() # returns True/False (duplicated) for each row
df.duplicated().value_counts() # returns series containing count of unique values
[i for i, v in enumerate(df.duplicated()) if v == True] # list of indices of duplicated
df.drop_duplicates(inplace = True) # remove duplicated rows
```

## correlation and plot

data.csv
```csv
Duration,Pulse,Maxpulse,Calories
60,110,130,409.1
60,117,145,479.0
60,103,135,340.0
```

correlation measure the relationship between every columns (value [-1:1]). Good correlations need to have at least 0.6 or -0.6 value.
If two columns have good correlation then it make sense to plot them to see if we have a linear relationship or exponential, or ..

```python
df.head(3)
#    Duration  Pulse  Maxpulse  Calories
# 0        60    110       130     409.1
# 1        60    117       145     479.0
# 2        60    103       135     340.0

df.corr()
#           Duration     Pulse  Maxpulse  Calories
# Duration  1.000000 -0.155408  0.009403  0.922721
# Pulse    -0.155408  1.000000  0.786535  0.025120
# Maxpulse  0.009403  0.786535  1.000000  0.203814
# Calories  0.922721  0.025120  0.203814  1.000000
```

### plot all columns 

```python
import matplotlib.pyplot as plt  
  
df = pd.read_csv('data.csv', names=['tempo', 'polso', 'polso_max', 'calorie'])  

# plots all the columns in different color, x: rows, y: value range 
df.plot()  
plt.show()
```

### plot x y

A scatter plot needs an x-axis parameter and a y-axis parameter.
**NB**: use parameters that have good correlation, i.e. > 0.6 or < -0.6

```python
df.plot(kind = 'scatter', x = 'Duration', y = 'Calories')
plt.show() # points are scattered around a line that shows linear relation, i.e. the longer the duration of the excercise, the higher the calories burned
```

### plot histogram

to plot an histogram we just need 1 column, the other one will be the frequency 

```python 
df["Duration"].plot(kind = 'hist')
plt.xlabel('duration')
plt.show() # it represents the distribution of data of a specific column
```


# Standard input

```python
name = input("Please enter your name: ") # Wait for the user to enter some input
print(f"Hello, {name}!")
```

**NB**: It's important to note that `input()` always returns a string!

```python
num = input() # wait for the user to enter something
num = int(num) # convert string to int!
print(f"square of {num} is {num**2}")
```

# Input file stream

## reading a file

using a file pointer `fp`

```python
with open('filename.txt') as fp:
    for line in fp:
        print(line)
```

read file line by line

```python
with open('example.txt', 'r') as file:
    line = file.readline()  # Read the first line
    while line:
        print(line.strip())  # .strip() removes the newline character
        line = file.readline()  # Read the next line
```

## writing a file

write line by line

```python
with open('output.txt', 'w') as file:
    file.write('Hello, world!\n')
    file.write('This is a new line.\n')
```

write a list of lines

```python
lines = ['Line 1\n', 'Line 2\n', 'Line 3\n']
with open('output.txt', 'w') as file:
    file.writelines(lines)
```
**NB**: each line includes the newline character `\n`


# Try except raise

**try**, **except**, **else** and/or **finally**:

```python
try:  
	print(f) # x is not defined >>> NameError: name 'f' is not defined
except NameError:  # we handle the specific NameError exception
	print("Variable x is not defined")  
except:  # we can add as many except as we need
	print("Something else went wrong")
else:
	print('something else') # executed if no errors were raised
finally:
	print('do something at the end') # executed regardless if an error is rised or not
```

**raise**: you can choose to throw an exception if a condition occurs

```python
x = "hello"

if not isinstance(x, int):
	raise TypeError("Only integers are allowed!")
```

# Concurrency vs Parallelism

Python supports **multithreading** however due to Python's Global Interpreter Lock (GIL), which ensures that only one thread executes Python bytecode at a time, multithreading in Python is not always effective for CPU-bound tasks.
Multithreading in Python is often more suitable for concurrency I/O-bound tasks where threads spend a significant amount of time waiting for external resources such as network or disk I/O.

## multi threading

```python
import threading

def print_numbers():
    for i in range(5):
        print(i)

if __name__ == "__main__":
    thread = threading.Thread(target=print_numbers)
    thread.start()
	thread.join(); # tells main thread to wait the end of thread before proceeding
```

## multi processing

If you need true parallelism, especially for CPU-bound tasks, you might want to consider using the **multiprocessing** module, which allows you to create multiple processes, each with its own Python interpreter and memory space.

```python
import multiprocessing

def square(x):
    return x ** 2

if __name__ == '__main__':
    data = [1, 2, 3, 4, 5]
    with multiprocessing.Pool(processes=3) as pool:
        result = pool.map(square, data)
    print(result)  # Output: [1, 4, 9, 16, 25]
```

## map reduce

```python
from collections import defaultdict
from multiprocessing import Pool
import numpy as np

num_processes = 3 # specify the number of processes to use

# Generate 10 random integers between 0 and 200
data = np.random.randint(0, 201, size=10)

# Define the mapper function: the task I want to solve using mutithreading
def mapper(item):
    # if number is even create pair [0, n], else pair [1, n]
    return (item % 2, item)

# Define the reducer function: combine the computed results
def reducer(items):
    result = defaultdict(list) # prepare an empty dictionary
    for key, value in items: # for every pair
        result[key].append(value) # append to list at either key:0 or key:1
    return result.items()

if __name__ == '__main__':
    # Map phase
    with Pool(processes=num_processes) as pool: # solve the task using a pool processes
        mapped_data = pool.map(mapper, data)

    # Reduce phase
    reduced_data = reducer([item for item in mapped_data])

    # Output the result
    print(dict(reduced_data))
```

# Other

## binary representation

A | B |*and*| *or* | *xor* | nand
-|-|-|-|-|-
0|0|0|0|1|1
0|1|0|1|0|1
1|0|0|1|0|1
1|1|1|1|1|0

### tricks
- if n is a power of 2, its binary representation contains only a 1
	- 2 -> 10
	- 4 -> 100
	- 8 -> 1000
- every time we do ``n & (n - 1)`` we basically remove the first 1 we encounter - starting from the less significant bit (right most) - from the n binary representation.
- in particular, if n is a power of 2, the binary representation has only a 1 and so  ``n & (n - 1) = 0``
- XOR of 2 equal numbers will produce 0
- ``n >> i`` (shift right) by $i$ times means cut $i$ bits from the end (right-most), so it means to divide by two i times
- ``n & 1`` gives us the least significant bit (right most) as well as ``n % 2``

```python
##### declare a variable 
# we can declare a variable using binary notation 0b
b = 0b1000 # !!! same as writing b = 8

print(b) # prints the decimal value >>> 8
print(bin(b)) # prints the binary value >>> 0b1000 
```


## binary search

```python
A = [-1, 0, 3, 5, 9, 12]
target = 9

def bsearch(A, target):
	l,r = 0, len(A)-1
	while l <= r:
		mid = l + (r-l)//2
		if A[mid] == target:
			return mid
		if A[mid] < target:
			l = mid + 1
		else:
			r = mid - 1
	return -1
```

or simply using the **bisect** library

```python
A, target = [1, 2, 4, 4], 4
from bisect import bisect_left, bisect_right

# FIRST occurence of target 4
i = bisect_left(A, target) 
i = i if i != len(A) and A[i] == target else -1

# LAST occurence of target 4
i = bisect_right(A, target) 
i = i-1 if i != 0 and A[i-1] == target else -1
```