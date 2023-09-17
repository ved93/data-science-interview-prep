
Q.1 There is a fair coin (one side heads, one side tails) and an unfair coin (both sides tails). You pick one at random, flip it 5 times, and observe that it comes up as tails all five times. What is the chance that you are flipping the unfair coin?(Facebook)
A.  This is good fundamental question. You can solve it using probability.


Q.2 https://www.toppr.com/ask/question/eight-players-p1-p2-p3-p8-play-a-knockout-tournament-it-is-known/

https://www.openbookpublishers.com/htmlreader/978-1-78374-142-7/Chapters/P65.html#:~:text=It%20is%20organised%20as%20a,start%20of%20the%20%EF%AC%81rst%20round.

Q.3 Balls and Boxes problem. Find number of  ways  
Five balls are to be placed in three boxes in how many diff. ways can be placed the balls so that no box remains empty if (i) balls and boxes are diff, (ii) balls identical and boxes diff. (iii) balls diff and boxes identical (iv) balls as well as boxes are identical  

https://www.hitbullseye.com/Quant/Permutation-and-Combination-Concept.php

Q.4. Two persons A and B agree to meet at a place between 11 to 12 noon. The first one to arrive waits for 20 minutes and then leave. if the time of their arrival be independent and at random, then the probabity that A and B meet is  
A. https://www.quora.com/A-and-B-decide-to-meet-between-1-pm-and-2-pm-on-a-given-day-Whoever-arrives-first-will-not-wait-for-the-other-for-more-than-15-minutes-Whats-the-probability-that-they-will-meet-that-day-and-why/answer/HV-Mishra

https://www.geeksforgeeks.org/probability-that-two-persons-will-meet/


Q.5. Amazon. Expected time to reach earth by demogorgans. There are three paths. One path leads to earth in one day. Other one takes one day and reach at the same spot. third one takes 2 days and reach the same spots.


Q.6. Say we have X ~ Uniform(0, 1) and Y ~ Uniform(0, 1). What is the expected value of the minimum of X and Y?(Google)

A. https://www.quora.com/Say-we-have-X-Uniform-0-1-and-Y-Uniform-0-1-What-is-the-expected-value-of-the-minimum-of-X-and-Y

https://math.stackexchange.com/questions/197299/expected-value-of-maximum-of-two-random-variables-from-uniform-distribution

Q.7. Say we are given a list of several categories (for example, the strings: A, B, C, and D) and want to sample from a list of such categories according to a particular weighting scheme. Such an example would be: for 100 items total, we want to see A 20% of the time, B 15% of the time, C 35% of the time, and D 30% of the time. How do we simulate this? What if we care about an arbitrary number of categories and about memory usage?

A. Since version 1.7.0, NumPy has a choice function that supports probability distributions.

from numpy.random import choice
draw = choice(list_of_candidates, number_of_items_to_pick,
              p=probability_distribution)
Note that probability_distribution is a sequence in the same order of list_of_candidates. You can also use the keyword replace=False to change the behavior so that drawn items are not replaced.

---
Q.8. What is the expected number of coin flips needed to get two consecutive heads?

A. Recommend All the answers in below
[link](https://www.quora.com/What-is-the-expected-number-of-coin-flips-until-you-get-two-heads-in-a-row) 

Q.9. Say you are given an unfair coin, with an unknown bias towards heads or tails. How can you generate fair odds using this coin?

Q.10. Three ants are sitting at the corners of an equilateral triangle. Each ant randomly picks a direction and starts moving along the edge of the triangle. What is the probability that none of the ants collide? Now, what if it is k ants on all k corners of an equilateral polygon?

A. Since every ant has two choices (pick either of two edges going through the corner on which ant is initially sitting), there are total 23 possibilities.

Out of 23 possibilities, only 2 don’t cause collision. So, the probability of collision is 6/8 and the probability of non-collision is 2/8.

Q.11. How many cards would you expect to draw from a standard deck before seeing the first ace?

A. https://math.stackexchange.com/questions/245354/expected-value-of-sums


Q.12. Estimate the disease probability in one city given the probability is very low national wide. Randomly asked 1000 person in this city, with all negative response(NO disease). What is the probability of disease in this city?   

Q.13. Suppose it is 8:00 AM and a flight is expected to land around then. The announcement says that the expected time to land anytime between 8:00 AM and 9:00 AM with uniform probability. You want to draw a plot of the probability of the flight landing before specific time t (Where t is some value between 8:00 AM and 9:00 AM). i.e t is on the X axis and the probability of the flight landing before t is on the Y axis.
What are some properties of this plot ?  
A. Note that the random variable corresponding to the time of the landing of the flight is a continuous random variable taking values between 8:00 AM and 9:00 AM.

The probability of the flight landing before a certain time is modelled by the cumulative distribution function. The CDF of a uniform distribution is a (a) continuous (b) non decreasing function.

Note that the CDF is 0 before 8AM and 1 after 9AM. You can interpret this as follows : The probability that the flight lands before 9:00 AM or any time after 9:00 AM is 1.

Also note that for a uniform distribution, the CDF is a straight line with an increasing slope.


Q.14. Suppose you are trying to determine the bias (p) of a coin. You model the outcome of a coin toss using the Bernoulli distribution with parameter p (probability of heads also called bias). p has a beta prior beta(1,1) which is similar to a uniform distribution from 0 to 1. You now compute the posterior after looking at 1000 tosses out of which 502 are heads and 498 are tails. Which of the following could be the posterior estimate of p ?
A. Lavanya. Before observing the data, we have a uniform prior on p between 0 and 1, which is means if we were to pick a value for p, 0.5 is the most meaningful value. Further a beta(1,1) is a rather uninformative weak prior, which means the posterior is heavily influenced by the 1000 data points and only mildly influenced by the prior.

Hence, after observing 502 heads and 498 tails, we would expect the posterior estimate (mean of the posterior) to be close to 502/1000. The precise value would be (502+1)/(498+1) which can be rounded off to .502

Take a look at the following link for more information : https://towardsdatascience.com/visualizing-beta-distribution-7391c18031f1


Q.15. prob of getting 3 heads in a sequence when a fair coin is tossed 5 times  
A. 
```
Total number of possible events = 2^5 = 32
Frequency of exactly 3 heads (HHHT*, THHHT, *THHH) = 2+1+2 = 5
Frequency of exactly four consecutive heads (HHHHT, THHHH) = 2
Frequency of five consecutive heads = 1
Frequency of required events = 5+2+1 = 8
Required probability = 8/32 = 1/4
```
https://www.quora.com/What-is-the-probability-of-getting-5-consecutive-heads-in-10-tosses-of-a-fair-coin

Q.16. An exit poll in an election is a survey taken of voters just after they have voted. One major use of exit polls has been so that news organizations can try to figure out as soon as possible who won the election, before the votes are officially counted. This has been notoriously inaccurate in various elections, sometimes because of selection bias: the sample of people who are invited to and agree to participate in the survey may not be similar enough to the overall population of voters.

Consider an election with two candidates, Candidate A and Candidate B. Every voter is invited to participate in an exit poll, where they are asked whom they voted for; some accept and some refuse. For a randomly selected voter, let  𝐴  be the event that they voted for A, and  𝑊  be the event that they are willing to participate in the exit poll. Suppose that  𝑃(𝑊|𝐴)=0.7  but  𝑃(𝑊|𝐴𝑐)=0.3 . In the exit poll,  60%  of the respondents say they voted for A (assume that they are all honest), suggesting a comfortable victory for A. Find  𝑃(𝐴) , the true proportion of people who voted for A.  
A. 

Q.17. Probability :Knock Out Tournament Of Ranked Players  
https://math.stackexchange.com/questions/1569352/probability-knock-out-tournament-of-ranked-players   

Q.18. Eight players P1,P2,..........P8 play a knockout tournament. It is known that whenever the players Pi and Pj play , the player Pi will win if i<j.
Assuming that the players are paired at random in each round, what is the probability that the players P4 reaches the final?  
A. https://www.toppr.com/ask/question/eight-players-p1-p2-p3-p8-play-a-knockout-tournament-it-is-known/


Q.19. https://math.stackexchange.com/questions/2757101/knockout-tournament-probability
https://math.stackexchange.com/questions/378084/a-probability-problem-involving-a-tournament
https://math.stackexchange.com/questions/911296/probability-in-a-knock-out-tournament  
https://doubtnut.com/ncert-solutions/class-12-maths-chapter-13-probability-1   
https://doubtnut.com/ncert-solutions/class-12-maths-chapter-12-linear-programming-1  
https://www.youtube.com/c/MathSolutionsForYou/playlists

Q.20. I play a gambling game in which I will win k−2 dollars with probability 12k for any k∈ℕ, that is,  
with probability 12, I lose 1 dollar;  
with probability 14, I win 0 dollar;  
with probability 18, I win 1 dollar;  
with probability 116, I win 2 dollars;  
with probability 132, I win 3 dollars;  
⋯
What is the probability that I win more than or equal to 1 dollar and less than 4 dollars? What is the probability that I win more than 2 dollars?
A. https://www.probabilitycourse.com/chapter1/1_3_4_discrete_models.php

:goal:

Q.21. Consider a sample space that is the rectangular region  [0,1]×[0,2] , i.e., the set of all pairs  (𝑥,𝑦)  that satisfy  0≤𝑥≤1  and  0≤𝑦≤2 . Consider a “uniform" probability law, under which the probability of an event is half of the area of the event. Find the probability of the following events:  
a) The two components  𝑥  and  𝑦  have the same values.  
b) The value,  𝑥 , of the first component is larger than or equal to the value,  𝑦 , of the second component.   
c) The value of  𝑥2  is larger than or equal to the value of  𝑦 .

Q.22. Let the sample space be the set of positive integers and suppose that  𝐏(𝑛)=1/2𝑛 , for  𝑛=1,2,… . Find the probability of the set  {3,6,9,…} , that is, of the set of of positive integers that are multiples of  3 .   

Q.23 untill head or success, find expected number of trials
https://www.quora.com/A-coin-is-tossed-until-a-head-appears-what-is-the-expected-number-of-tosses

https://www.quora.com/What-is-the-expected-number-of-coin-flips-until-you-get-two-heads-in-a-row

https://math.stackexchange.com/questions/192177/how-many-times-to-roll-a-die-before-getting-two-consecutive-sixes

https://math.stackexchange.com/questions/1155104/expected-number-of-coin-tosses-to-land-n-heads  

https://mas-dse.github.io/DSE210/slides%20and%20worksheets/Class%202.pdf

https://math.stackexchange.com/questions/3567745/expectation-problem-1

https://www.statisticshowto.com/probability-and-statistics/expected-value/


### Solutions

21. a) This event is a line, and since a line has zero area, the probability is zero.
b) This event is a triangle with vertices at  (0,0) ,  (1,0) ,  (1,1) . Its area is  1/2 , and therefore the probability is  1/4 .
c) This event corresponds to the region below the curve  𝑦=𝑥2 , where  𝑥  ranges from 0 to 1. The area of this region is
∫10𝑥2𝑑𝑥=𝑥33∣∣∣10=13, 
and therefore the corresponding probability is  1/6 .

22. Using countable additivity, and with 𝛼=2−3=1/8, the desired probability is

1/2ˆ3+1/2ˆ6+1/2ˆ9+⋯=𝛼+𝛼ˆ2+𝛼ˆ3+⋯= 𝛼/1−𝛼=(1/8)/(1−(1/8))=1/7.

