
https://gto76.github.io/python-cheatsheet/

1. Create a list with zero or None. `l = [None]*n`
2. Sort a dictionary on the basis of values and return keys
`bst_ind =sorted(res, key = res.get, reverse =True)`  
`tp =sorted(d.items(), key = lambda k : (k[1],k[0]), reverse=True)`
   
3. Get a key from value in dictionary. Convert into key list and value list then get index of particular value from list.Use that index in key list to get the key    

`list out keys and values separately 
key_list = list(my_dict.keys()) 
val_list = list(my_dict.values()) 
print(key_list[val_list.index(100)]) 
print(key_list[val_list.index(112)])`

4. Using previous and current values is also a good way to solve problems. i.e. Fibonacci problems
5. 
6. Dont hesitate to use brute force solution. Just tell in advance.
7. Two sum and its different variants are good for multiple problems. Write twom pointers solution for wto sum problem. 
8. A quick sort/merge sort have complexity nlogn
9.  If an array is sorted then two-pointer sol is good.
10. hash-map is good concepts to look up values
11. Two-pointers method's complexity is O(n)
12. if youn have sorted list/array, think of using 2 pointers method
13. 3 sum can be easily converted to 2 sum. Use these heuristics.
14. Dont forget extreme cases
15. Accessing qa func from a class.Then use self.func
16. If you need to count ways then think of dp and recursion
17. Recursion is weak part. Solve some problems(Fibonacci,Factorial etc) on recursion and read the blog.
18. Revisit Binary search algo and think about use-cases. Two pointer method. Just write the code for it.
19. Write a program for merge sort.
20. two sum problem's 2 pointer solution is good. Implement by yourself bcz it has details whihc you tend to ignore if you dont implement gtourself.
21. If you are repeatedly partitioning your data by some factor, timecomplexity is going to be log n. i.e. 
    ```
    for i in range(0,n,step = 2*i):
    ```
    Time Complexity of a loop is considered as O(Logn) if the loop variables is divided / multiplied by a constant amount.
22. There are two ways to use divide and conquer or reducing the problem  
    1. Use of left and right with while loop 
    2. Use recursion   
23. ede 







### Input methods in python



```
def create_array(size):
    return [random.choice(list(range(10))) for _ in range(size)]

seq = create_array(100000)
```




### Links to revisit

1. Visualisation of recursion Fibonacci *Highly recommended* https://www.cs.usfca.edu/~galles/visualization/DPFib.html
2. [Recursion-How to think](https://medium.com/@daniel.oliver.king/getting-started-with-recursion-f89f57c5b60e)  
3. https://www.khanacademy.org/computing/computer-science/algorithms/recursive-algorithms/a/recursion
4. https://indepth.dev/dijkstra-was-right-recursion-should-not-be-difficult/
5. https://leetcode.com/problems/min-cost-climbing-stairs/discuss/657490/Python-solution-from-a-beginner-(some-easy-steps-to-follow-to-solve-dp)
6. [Dynamic Programming](https://leetcode.com/discuss/general-discussion/475924/my-experience-and-notes-for-learning-dp)
7. [Dynamic Programming pattern](https://leetcode.com/discuss/general-discussion/458695/dynamic-programming-patterns)
8. https://leetcode.com/problems/house-robber/discuss/156523/From-good-to-great.-How-to-approach-most-of-DP-problems.
9. https://leetcode.com/problems/longest-palindromic-subsequence/discuss/222605/dp-problem-classifications-helpful-notes
10. https://softwareengineering.stackexchange.com/questions/146021/determining-if-an-algorithm-is-o-log-n
11. 


