PERMUTATIONS WITH REPETITION

THEOREM 1: The number of r-permutations of a set of n objects with repetitions allowed is nr.

EXAMPLE 1: How many strings of length n can be formed from the English alphabet?  26n

COMBINATIONS WITH REPETITION

THEOREM 2:       There are C(n+r-1, r)
r-combinations from a set with n elements when repetition of elements is allowed.

EXAMPLE 5: Suppose that a cookie shop has four different kinds of cookies.  How many different ways can six cookies be chosen?  Assume that only the type of cookie, and not the individual cookies or the order in which they are chosen, matters.

Solution:       C(4+6-1, 6) = C(9,6) = 84.


TYPE | REPETITION ALLOWED? | FORMULA
-- | -- | --
r permutation|No|n!/(n-r)!|
r-combination| No | n!/[r!(n-r)!] 
r-permutation |Yes| nr| 
r-combination | Yes|(n+r-1)!/[r!(n-1)!]

**PERMUTATIONS OF SETS WITH INDISTINGUISHABLE OBJECTS**  
THEOREM 3:   The number of different permutations of n objects, where there are n1 indistinguishable objects of type 1, where there are n2 indistinguishable objects of type 2,…, and nk indistinguishable objects of type k, is
n!/[n1!n2!….nk!]
 
DISTRIBUTING OBJECTS INTO BOXES

THEOREM 4:   The number of ways to distribute n distinguishable objects into k distinguishable boxes so that ni objects are placed into box i, i = 1,2,…,k, equals  n!/[n1!n2!….nk!]




## Links

http://www.pitt.edu/~bonidie/cs441/lecture21.pdf

http://www.cs.iit.edu/~wan/cs330/Chapter6-counting.pdf

http://www.maths.unp.ac.za/coursework/Math236/2013/Slides/Slide%2011.pdf