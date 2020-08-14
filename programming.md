Q. Given a number n, return the number of lists of consecutive positive integers that sum up to n.
For example, for n = 9, you should return 3 since the lists are: [2, 3, 4], [4, 5], and [9]. Can you do it in linear time?

A. This is tricky problem. Search on leetcode for the solution


Q. This problem was asked by Stripe.

Write a program to generate the partitions for a number n. A partition for n is a list of positive integers that sum up to n. For example: if n = 4, we want to return the following partitions: [1,1,1,1], [1,1,2], [2,2], [1,3], and [4]. Note that a partition [1,3] is the same as [3,1] so only the former is included.

Q. why do we use defaultdict?  
A. A common problem that you can face when working with Python dictionaries is to try to access or modify keys that don’t exist in the dictionary. This will raise a KeyError and break up your code execution. To handle these kinds of situations, the standard library provides the Python defaultdict type, a dictionary-like class that’s available for you in collections.  
The Python defaultdict type behaves almost exactly like a regular Python dictionary, but if you try to access or modify a missing key, then defaultdict will automatically create the key and generate a default value for it. This makes defaultdict a valuable option for handling missing keys in dictionaries.
```
# Defining a dict 
d = defaultdict(list) 
def_dict['one'] = 1  # Add a key-value pair
def_dict['missing']  # Access a missing key returns an empty list
def_dict['another_missing'].append(4)  # Modify a missing key

# Defining the dict 
# The default value is 0 
d = defaultdict(int) 
a_dct = defaultdict(float)   # The Default Value is "0.0"
a_dct = defaultdict(str)   # The Default Value is ""

# dict with lambda func which returns 100
d = defaultdict(lambda : 100)
 ```
