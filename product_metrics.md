Q. How would you design a metric to compare rankings of lists of shows for a given user?

A. 
1) Develop a list of shows/movies that are representative of different taste categries 
2) Obtain ranking of the items in the list from 2 users
3) Use Spearman's rho (or other test that works with rankings) to assess dependence/conguence between the 2 people's rankings.
4) Look at the mean average precision of the movies that the users watch out of the rankings. So if out of 10 recommended movies one user prefers the third and the other user prefers the sixth, the recommendation engine of the user who preferred the third would be better.


Q. 
