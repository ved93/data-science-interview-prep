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
Q. Given a function with inputs — an array with N randomly sorted numbers, and an int K, return output in an array with the K largest numbers.

Q. check empty list  
```
if not list:
    print('its empty')

```

Q. Asked by Paytm. You have been given two metrics. Write a code to identify if thet are symmetric metrics.  
A. My soln. Need to refine
``` 
mat = np.matrix(2,3,1)
flag = 0
for i in range(2,mat.shape[0]):
    for j in range(1,mat.shape[0]):
        if mat[i][j] = mat[j][i]:
            print()
            flag = 1
        else:
            flag =0
            print('not symmetric')
        
if flag == 1:
    print('symmetric')        
``` 

Q. Asked by Delhivery. Write a programme to write factorial. Implement both recursion and dynamic programming soln.

Q. Paytm. Count digit's(0-9) occurence in numbers from 1 to 100.  
```
store_num = []
for i in range(1,101):
    store_num.extend(list(str(i)))
#     list(str(i))
Counter(store_num)
```

Q. Ericsson. Write a programme to check two sorted array to merge into one. Just a simple idea.
```
# A
# B

# C= []
# i = 0
# j = 0

for k in range(len(A+B)):
    if A[i] <= B[j]:
        C[k] = A[i]
        i= i+1
    else:
        C[k] = B[j]
        j = j+1

    if len(A) <= i:
        C.append(B[j+1:])
    if len(B) <= j:
        C.append(A[i+1:])     
```

Q. Ericsson. estimate the value of pi to the closest approximate value, you can use random number generator function as many times as required.   
https://www.geeksforgeeks.org/estimating-value-pi-using-monte-carlo/

Q. Design a parking system for airport, there are fixed no of slots for each type of vehicle and each #vehicle has a type and number. The amount charged is based on price per type per min. So when a #vehicle enters, it plate number is noted and if there is an available slot for that vehicle its #allowed to be parked.?

Q. There are 100 ropes in a bag. In each step, two rope ends are picked at random, tied together and put back into a bag. The process is repeated until there are no free ends.
What is the expected number of loops at the end of the process?   
A. https://math.stackexchange.com/questions/2209/expected-number-of-loops

```
import numpy as np
import random 



# print(random.randint(1,200))
l = {}
last_end = 0
loop = 0

num_list=list(range(0,200))

print(random.choices(num_list,k=2))

last_end,last_str = 0,0
m =0
for i in range(1,101):
  # endp=random.randint(1,200)
  # strp=random.randint(1,200)
  ends=random.sample(num_list,k=2)
  

  print(ends)
  num_list.remove(ends[0])
  num_list.remove(ends[1])

  if last_str in ends and last_end in ends:
    print('was here')
    loop = loop+1

  elif last_str in ends or last_end in ends:
    if   last_str in ends:
      l[m]=[last_str,last_end]





  if ends[0] % 2 == 0:
    last_str = ends[0]-1
  else:
    last_str = ends[0]+1


  if ends[1] % 2 == 0:
    last_end = ends[1]-1
  else:
    last_end = ends[1]+1


  l[m]=[last_str,last_end]
  m= m+1
    
    

  # last_str = ends[0]
  # last_end = ends[1]

print(loop)

```


Q. 


Q. Check permutation of string can become a palindrome?  
Q. 

'''
Given a sorted integer array nums, where the range of elements are in the inclusive range [lower, upper]
 return its missing ranges.

    Example:

    Input: nums = [0, 1, 3, 50, 75], lower = 0 and upper = 99,
    Output: ["2", "4->49", "51->74", "76->99"]
'''



def append_elem(lst, out):
  #print(lst)
  if len(lst) == 0:
    pass
  elif len(lst) == 1:
      out.append(lst[0])
  else:
    out.append('{0}->{1}'.format(min(lst), max(lst)))
    
  #print(out)
  return out


def missing_num_2(a, l, u):
  output = []
  tmp_lst = []
  
  for i in range(l, u+1):
    #print(i)
    if i not in a:
      #print(i)
      tmp_lst.append(i)
    else:
      #print(tmp_lst)
      output = append_elem(tmp_lst, output)
      tmp_lst = []
        
  if len(tmp_lst) != 0:
    output = append_elem(tmp_lst, output)
    
  return output



print(missing_num_2([0, 1, 3, 50, 75],0,99) )   

'''
def missing_num(a,l,u):
  b = []
  for i in range(l,len(a)):
    if a[i] == l:
      l=l+1
      continue
    else:
      
          #     if i+1 == len(a):
          # r='{}->{}'.format(l,a[i+1]-1)
          # # print(r)
          # b.append(r)
          
          # return b
      
      if a[i+1] != (l+1):
        r='{}->{}'.format(l,a[i+1]-1)
        # print(r)
        b.append(r)
        
      else:  
        b.append(str(l))
      l = l+1
  
  return b
       

print(missing_num([0, 1, 3, 50, 75],0,99) )      '''







### Solutions

