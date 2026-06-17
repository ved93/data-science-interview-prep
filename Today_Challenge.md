

Q. How can you decide how long to run an experiment? What are some problems with just using a fixed p-value threshold and how do you work around them?

A. There are few ways to answer this question:

1. Keep running your experiment till you get 90%-95% statistical significance.
2. calculate effect size for your experiment using tools like [optimizely](https://www.optimizely.com/sample-size-calculator/), [experimentcalculator](https://www.experimentcalculator.com/) 
3. Atleast have 1000 conversions

If we use just fixed p-value threshold, then it might results into p-value hacking. To work around them we can calculate effect size separately.

---
Q. A coin was flipped 1000 times, and 560 times it showed up heads. Do you think the coin is biased? Why or why not?(Google)

A. The variance for # of heads in 1000 flips of a fair coin would be (0.5)(1–0.5)(1000) = 250 and the standard deviation is the square root of the variance: √250 = 15.81+. And of course the mean would be (0.5)(1000) = 500.

So 560 is (560–500)/15.81 = +3.794… standard deviations.

A 95% confidence interval is ±1.96 standard deviations, which would be ±30.99 or between 469.01 and 530.99. So 560 heads is a BIG outlier. The coin probably is biased.

On the other hand, 56 heads in 100 trials - the same proportion with a smaller sample - would only be +1.2 standard deviations (mean is 50, standard deviation is 5.) So that would be too small of a sample to conclude that the coin is biased.

---
Q. Uber. Say you need to produce a binary classifier for fraud detection. What metrics would you look at, how is each defined, and what is the interpretation of each one?

A. I have worked a bit in the fraud domain, and we definitely look at ROC AUC as our primary metric. The fact that it's not sensitive to class imbalance can be a feature, not a bug. Consider retraining models on a monthly basis, and trying to compare performance across time. PR-AUC will be driven by a combination of model performance and underlying fraud rate, whereas ROC-AUC is robust to variable fraud rate.

Second, the business typically makes a decision based on the impact to good customers, or in other words, FPR. Then, the important question becomes: at this given FPR, how much of the fraud am I capturing? This is precisely what the ROC curve tells us. Also note the host said they care more about partial ROC AUC, and this is likely for the same reason: they care about very low FPR, so only the area under this section of the curve is most relevant.

That said, if you instead have a model that's evaluating e.g. every hour and sending accounts for human investigation, then your primary bottle-neck is investigator bandwidth, and in this case, you might focus on Precision/Recall metrics as you will likely have a target precision.

---
Q. Facebook.Imagine the social graphs for both Facebook and Twitter. How do they differ? What metric would you use to measure how skewed the social graphs are?

A. First you should recognize that Twitter is *following* vs. a FB friendship (connections are 2-way street). Second part has to do with comparing the "equality" of Twitter vs FB social graph. In TW, you have a small % with a TON of connections (and then a long tail), and FB you have a much less extreme version of that. Think how you would plot out distribution of connections per user and how FB/TW are different.

---
Q. What does it mean for an estimator to be unbiased? What about consistent? Give examples of an unbiased but not consistent estimator, as well as a biased but consistent estimator.

A. https://stats.stackexchange.com/questions/31036/what-is-the-difference-between-a-consistent-estimator-and-an-unbiased-estimator

---
Q. There are two games involving dice that you can play. In the first game, you roll two die at once and get the dollar amount equivalent to the product of the rolls. In the second game, you roll one die and get the dollar amount equivalent to the square of that value. Which has the higher expected value and why?

A. 

---
Q. Google. Say you are running a multiple linear regression and believe there are several predictors that are correlated. How will the results of the regression be affected if they are indeed correlated? How would you deal with this problem?

A. Interpretability of coefficients wont make sense and coefficients will be unstable

---
Q. Uber.Say you are given a random Bernoulli trial generator. How would you generate values from a standard normal distribution?

A.

---
Q. What are MLE and MAP? What is the difference between the two?  
A. [Check here](https://www.quora.com/What-is-the-difference-between-Maximum-Likelihood-ML-and-Maximum-a-Posteriori-MAP-estimation)  

Q. Why does gradient point the direction of steepest ascent?   
A. https://www.khanacademy.org/math/multivariable-calculus/multivariable-derivatives/gradient-and-directional-derivatives/v/why-the-gradient-is-the-direction-of-steepest-ascent

https://www.quora.com/Can-you-explain-intuitively-or-with-an-example-why-the-gradient-points-to-the-direction-of-steepest-ascent  
https://www.quora.com/What-is-an-intuitive-explanation-for-why-the-gradient-points-in-the-direction-of-steepest-ascent  
https://betterexplained.com/articles/vector-calculus-understanding-the-gradient/   
https://math.stackexchange.com/questions/223252/why-is-gradient-the-direction-of-steepest-ascent
https://www.khanacademy.org/math/multivariable-calculus/multivariable-derivatives/gradient-and-directional-derivatives/v/directional-derivative

Q. what is poisson distribution?  
A. The Poisson distribution is the discrete probability distribution of the number of events occurring in a given time period, given the average number of times the event occurs over that time period. A certain fast-food restaurant gets an average of 3 visitors to the drive-through per minute.
The number of cases a doctor can handle in a day is a positive number, this can be modelled by a Poisson distribution.  
*Additional notes*:
Normal distribution can be used when we have a real number taking values between negative and positive infinity. Clearly this is not the case for the number of cases taken by a doctor per day.  
Bernoulli distribution is used to model binary random variables, for instance the result of a coin toss. Hence, it cannot be used to model a random variable that is not binary.


Q. You are doing an experiment to determine whether a new coffee recipe you invented, that is more healthy is actually likable by people. You want to make sure people like this coffee atleast as much as the previous coffee by looking at the average rating they give. Which kind of test would make more sense in this setting ?  
A. If you do a two sided test, your null hypothesis will be, people like the old recipe as much as the newer recipe. If you measure the ratings and compute the p value, you will be in a position to reject the null hypothesis that people like the old recipe as much as the newer one.

With a one sided test, the null hypothesis will be : people like the previous recipe better than the current recipe. If you are able to get an appropriate p value with the adequate sample size, you can conclude that the people do not like the previous coffee more than the current coffee. Note that you still cannot conclude that they like the new one more.
https://stats.idre.ucla.edu/other/mult-pkg/faq/general/faq-what-are-the-differences-between-one-tailed-and-two-tailed-tests/
