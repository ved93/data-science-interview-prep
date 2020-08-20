Q. The probability that item an item at location A is 0.6, and 0.8 at location B. What is the probability that item would be found on Amazon website?   
```
P(A or B) = P(A) + P(B) — P(A and B)
P(A or B) = 0.6 + 0.8 - (0.6*0.8)
P(A or B) = 0.92
```
Q: What is boosting?  
Boosting is an ensemble method to improve a model by reducing its bias and variance, ultimately converting weak learners to strong learners. The general idea is to train a weak learner and sequentially iterate and improve the model by learning from the previous learner. 

Q. Lists are for homogeneous data and tuples are for heterogeneous data… why?
https://stackabuse.com/lists-vs-tuples-in-python/


Q. Describe Tree, SVM and Random forest. Talk about their advantage and disadvantages.  
A. *Decision Trees*: a tree-like model used to model decisions based on one or more conditions.  
Pros: easy to implement, intuitive, handles missing values  
Cons: high variance, inaccurate  
*Support Vector Machines*: a classification technique that finds a hyperplane or a boundary between the two classes of data that maximizes the margin between the two classes. There are many planes that can separate the two classes, but only one plane can maximize the margin or distance between the classes.  
Pros: accurate in high dimensionality  
Cons: prone to over-fitting, does not directly provide probability estimates  
*Random Forests*: an ensemble learning technique that builds off of decision trees. Random forests involve creating multiple decision trees using bootstrapped datasets of the original data and randomly selecting a subset of variables at each step of the decision tree. The model then selects the mode of all of the predictions of each decision tree.  
Pros: can achieve higher accuracy, handle missing values, feature scaling not required, can determine feature importance.  
Cons: black box, computationally intensive