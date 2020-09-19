Q. How would you design a metric to compare rankings of lists of shows for a given user?

A. 
1) Develop a list of shows/movies that are representative of different taste categries 
2) Obtain ranking of the items in the list from 2 users
3) Use Spearman's rho (or other test that works with rankings) to assess dependence/conguence between the 2 people's rankings.
4) Look at the mean average precision of the movies that the users watch out of the rankings. So if out of 10 recommended movies one user prefers the third and the other user prefers the sixth, the recommendation engine of the user who preferred the third would be better.


Q. How can you decide how long to run an experiment? What are some problems with just using a fixed p-value threshold and how do you work around them?

A. https://www.optimizely.com/sample-size-calculator/

https://www.experimentcalculator.com/

https://help.optimizely.com/Analyze_Results/How_long_to_run_an_experiment

Q. Uber. You’re on the data science team and are responsible for figuring out surge pricing. Why does it need to exist and what metrics and data should you track?

A. It needs to exist to balance the demand-supply  
 equation. Surge pricing motivates driver to go the   surge areas hence results in balancing the supply in high demand area. We need to track conversions in surge price points.


