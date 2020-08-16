
Q. There is a fair coin (one side heads, one side tails) and an unfair coin (both sides tails). You pick one at random, flip it 5 times, and observe that it comes up as tails all five times. What is the chance that you are flipping the unfair coin?(Facebook)

A.  This is good fundamental question. You can solve it using probability.


Q. Say we have X ~ Uniform(0, 1) and Y ~ Uniform(0, 1). What is the expected value of the minimum of X and Y?(Google)

A. https://www.quora.com/Say-we-have-X-Uniform-0-1-and-Y-Uniform-0-1-What-is-the-expected-value-of-the-minimum-of-X-and-Y

https://math.stackexchange.com/questions/197299/expected-value-of-maximum-of-two-random-variables-from-uniform-distribution

Q. Say we are given a list of several categories (for example, the strings: A, B, C, and D) and want to sample from a list of such categories according to a particular weighting scheme. Such an example would be: for 100 items total, we want to see A 20% of the time, B 15% of the time, C 35% of the time, and D 30% of the time. How do we simulate this? What if we care about an arbitrary number of categories and about memory usage?

A. Since version 1.7.0, NumPy has a choice function that supports probability distributions.

from numpy.random import choice
draw = choice(list_of_candidates, number_of_items_to_pick,
              p=probability_distribution)
Note that probability_distribution is a sequence in the same order of list_of_candidates. You can also use the keyword replace=False to change the behavior so that drawn items are not replaced.

---
Q. What is the expected number of coin flips needed to get two consecutive heads?

A. Recommend All the answers in below
[link](https://www.quora.com/What-is-the-expected-number-of-coin-flips-until-you-get-two-heads-in-a-row) 

Q. Say you are given an unfair coin, with an unknown bias towards heads or tails. How can you generate fair odds using this coin?

Q. Three ants are sitting at the corners of an equilateral triangle. Each ant randomly picks a direction and starts moving along the edge of the triangle. What is the probability that none of the ants collide? Now, what if it is k ants on all k corners of an equilateral polygon?

A. Since every ant has two choices (pick either of two edges going through the corner on which ant is initially sitting), there are total 23 possibilities.

Out of 23 possibilities, only 2 don’t cause collision. So, the probability of collision is 6/8 and the probability of non-collision is 2/8.

Q. How many cards would you expect to draw from a standard deck before seeing the first ace?

A. https://math.stackexchange.com/questions/245354/expected-value-of-sums


Q. Estimate the disease probability in one city given the probability is very low national wide. Randomly asked 1000 person in this city, with all negative response(NO disease). What is the probability of disease in this city?   
Q. 
